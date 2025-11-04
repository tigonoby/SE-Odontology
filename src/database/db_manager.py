"""
Gestor de Base de Datos
Maneja la conexión y operaciones con MySQL/SQLite
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path
import os


class DatabaseManager:
    """
    Gestor de base de datos para el sistema experto
    Usa SQLite por defecto (más fácil, sin necesidad de servidor)
    Puede migrar a MySQL fácilmente si se necesita
    """
    
    def __init__(self, db_path=None):
        """
        Inicializa el gestor de base de datos
        
        Args:
            db_path: Ruta al archivo de base de datos SQLite
                    Si es None, usa 'data/odontologia.db'
        """
        if db_path is None:
            # Crear carpeta data si no existe
            base_dir = Path(__file__).parent.parent.parent
            data_dir = base_dir / 'data'
            data_dir.mkdir(exist_ok=True)
            db_path = data_dir / 'odontologia.db'
        
        self.db_path = str(db_path)
        self.connection = None
        self.cursor = None
        
        # Inicializar base de datos
        self._init_database()
    
    def _init_database(self):
        """Inicializa la base de datos y crea las tablas si no existen"""
        self.connect()
        self._create_tables()
        self.disconnect()
    
    def connect(self):
        """Establece conexión con la base de datos"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Para acceder por nombre de columna
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            print(f"Error conectando a la base de datos: {e}")
            return False
    
    def disconnect(self):
        """Cierra la conexión con la base de datos"""
        if self.connection:
            self.connection.commit()
            self.connection.close()
            self.connection = None
            self.cursor = None
    
    def _create_tables(self):
        """Crea las tablas necesarias en la base de datos"""
        
        # Tabla de pacientes
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                edad INTEGER,
                telefono TEXT,
                email TEXT,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notas TEXT
            )
        """)
        
        # Tabla de diagnósticos
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS diagnosticos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER NOT NULL,
                fecha_diagnostico TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                diagnostico_principal TEXT NOT NULL,
                confianza_principal REAL NOT NULL,
                gravedad TEXT,
                urgencia TEXT,
                descripcion TEXT,
                diagnosticos_alternativos TEXT,
                num_sintomas_evaluados INTEGER,
                usa_logica_fuzzy BOOLEAN,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
            )
        """)
        
        # Tabla de síntomas (detalle de cada diagnóstico)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sintomas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                diagnostico_id INTEGER NOT NULL,
                nombre_sintoma TEXT NOT NULL,
                valor_sintoma TEXT NOT NULL,
                tipo_sintoma TEXT,
                FOREIGN KEY (diagnostico_id) REFERENCES diagnosticos(id)
            )
        """)
        
        # Tabla de recomendaciones
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recomendaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                diagnostico_id INTEGER NOT NULL,
                recomendacion TEXT NOT NULL,
                orden INTEGER,
                FOREIGN KEY (diagnostico_id) REFERENCES diagnosticos(id)
            )
        """)
        
        self.connection.commit()
    
    def guardar_paciente(self, nombre, edad=None, telefono=None, email=None, notas=None):
        """
        Guarda o actualiza un paciente en la base de datos
        
        Args:
            nombre: Nombre del paciente
            edad: Edad del paciente (opcional)
            telefono: Teléfono (opcional)
            email: Email (opcional)
            notas: Notas adicionales (opcional)
        
        Returns:
            ID del paciente guardado
        """
        self.connect()
        
        # Buscar si el paciente ya existe
        self.cursor.execute("SELECT id FROM pacientes WHERE nombre = ?", (nombre,))
        resultado = self.cursor.fetchone()
        
        if resultado:
            # Actualizar paciente existente
            paciente_id = resultado['id']
            self.cursor.execute("""
                UPDATE pacientes 
                SET edad = ?, telefono = ?, email = ?, notas = ?
                WHERE id = ?
            """, (edad, telefono, email, notas, paciente_id))
        else:
            # Insertar nuevo paciente
            self.cursor.execute("""
                INSERT INTO pacientes (nombre, edad, telefono, email, notas)
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, edad, telefono, email, notas))
            paciente_id = self.cursor.lastrowid
        
        self.connection.commit()
        self.disconnect()
        
        return paciente_id
    
    def guardar_diagnostico(self, paciente_nombre, resultado_diagnostico, sintomas_dict):
        """
        Guarda un diagnóstico completo en la base de datos
        
        Args:
            paciente_nombre: Nombre del paciente
            resultado_diagnostico: Diccionario con el resultado del diagnóstico
            sintomas_dict: Diccionario con los síntomas evaluados
        
        Returns:
            ID del diagnóstico guardado
        """
        self.connect()
        
        # Obtener ID del paciente (debe existir ya)
        self.cursor.execute("SELECT id FROM pacientes WHERE nombre = ?", (paciente_nombre,))
        resultado = self.cursor.fetchone()
        
        if not resultado:
            # Si no existe, crearlo
            self.cursor.execute("""
                INSERT INTO pacientes (nombre)
                VALUES (?)
            """, (paciente_nombre,))
            paciente_id = self.cursor.lastrowid
        else:
            paciente_id = resultado['id']
        
        # Extraer información del diagnóstico principal
        principal = resultado_diagnostico.get('principal', {})
        
        if not principal:
            self.disconnect()
            return None
        
        diagnostico_principal = principal.get('nombre', 'Desconocido')
        confianza = principal.get('confianza', 0.0)
        gravedad = principal.get('gravedad', 'desconocida')
        urgencia = principal.get('urgencia', 'desconocida')
        descripcion = principal.get('descripcion', '')
        
        # Convertir diagnósticos alternativos a JSON
        diagnosticos_alt = resultado_diagnostico.get('diagnosticos', [])
        if len(diagnosticos_alt) > 1:
            alternativos = [
                {
                    'nombre': d['nombre'],
                    'confianza': d['confianza_porcentaje']
                }
                for d in diagnosticos_alt[1:4]  # Hasta 3 alternativos
            ]
            diagnosticos_alt_json = json.dumps(alternativos)
        else:
            diagnosticos_alt_json = None
        
        # Insertar diagnóstico
        self.cursor.execute("""
            INSERT INTO diagnosticos (
                paciente_id, diagnostico_principal, confianza_principal,
                gravedad, urgencia, descripcion, diagnosticos_alternativos,
                num_sintomas_evaluados, usa_logica_fuzzy
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            paciente_id,
            diagnostico_principal,
            confianza,
            gravedad,
            urgencia,
            descripcion,
            diagnosticos_alt_json,
            resultado_diagnostico.get('sintomas_evaluados', 0),
            resultado_diagnostico.get('usa_logica_fuzzy', False)
        ))
        
        diagnostico_id = self.cursor.lastrowid
        
        # Guardar síntomas
        for nombre_sintoma, valor_sintoma in sintomas_dict.items():
            tipo_sintoma = self._determinar_tipo_sintoma(nombre_sintoma, valor_sintoma)
            
            self.cursor.execute("""
                INSERT INTO sintomas (diagnostico_id, nombre_sintoma, valor_sintoma, tipo_sintoma)
                VALUES (?, ?, ?, ?)
            """, (diagnostico_id, nombre_sintoma, str(valor_sintoma), tipo_sintoma))
        
        # Guardar recomendaciones
        recomendaciones = principal.get('recomendaciones', [])
        for idx, rec in enumerate(recomendaciones, 1):
            self.cursor.execute("""
                INSERT INTO recomendaciones (diagnostico_id, recomendacion, orden)
                VALUES (?, ?, ?)
            """, (diagnostico_id, rec, idx))
        
        self.connection.commit()
        self.disconnect()
        
        return diagnostico_id
    
    def _determinar_tipo_sintoma(self, nombre, valor):
        """Determina el tipo de síntoma basado en su nombre y valor"""
        if isinstance(valor, (int, float)):
            return 'numerico'
        elif nombre.endswith('_visible') or nombre.endswith('_cara'):
            return 'booleano'
        else:
            return 'categorico'
    
    def obtener_historial_paciente(self, paciente_nombre):
        """
        Obtiene el historial de diagnósticos de un paciente
        
        Args:
            paciente_nombre: Nombre del paciente
        
        Returns:
            Lista de diagnósticos del paciente
        """
        self.connect()
        
        self.cursor.execute("""
            SELECT 
                d.id,
                d.fecha_diagnostico,
                d.diagnostico_principal,
                d.confianza_principal,
                d.gravedad,
                d.urgencia,
                d.descripcion
            FROM diagnosticos d
            JOIN pacientes p ON d.paciente_id = p.id
            WHERE p.nombre = ?
            ORDER BY d.fecha_diagnostico DESC
        """, (paciente_nombre,))
        
        historial = []
        for row in self.cursor.fetchall():
            historial.append({
                'id': row['id'],
                'fecha': row['fecha_diagnostico'],
                'diagnostico': row['diagnostico_principal'],
                'confianza': row['confianza_principal'],
                'gravedad': row['gravedad'],
                'urgencia': row['urgencia'],
                'descripcion': row['descripcion']
            })
        
        self.disconnect()
        return historial
    
    def obtener_diagnostico_detallado(self, diagnostico_id):
        """
        Obtiene los detalles completos de un diagnóstico
        
        Args:
            diagnostico_id: ID del diagnóstico
        
        Returns:
            Diccionario con todos los detalles
        """
        self.connect()
        
        # Obtener diagnóstico
        self.cursor.execute("""
            SELECT d.*, p.nombre as paciente_nombre
            FROM diagnosticos d
            JOIN pacientes p ON d.paciente_id = p.id
            WHERE d.id = ?
        """, (diagnostico_id,))
        
        diag_row = self.cursor.fetchone()
        if not diag_row:
            self.disconnect()
            return None
        
        diagnostico = dict(diag_row)
        
        # Obtener síntomas
        self.cursor.execute("""
            SELECT nombre_sintoma, valor_sintoma, tipo_sintoma
            FROM sintomas
            WHERE diagnostico_id = ?
        """, (diagnostico_id,))
        
        diagnostico['sintomas'] = [dict(row) for row in self.cursor.fetchall()]
        
        # Obtener recomendaciones
        self.cursor.execute("""
            SELECT recomendacion
            FROM recomendaciones
            WHERE diagnostico_id = ?
            ORDER BY orden
        """, (diagnostico_id,))
        
        diagnostico['recomendaciones'] = [row['recomendacion'] for row in self.cursor.fetchall()]
        
        self.disconnect()
        return diagnostico
    
    def obtener_estadisticas(self):
        """
        Obtiene estadísticas generales del sistema
        
        Returns:
            Diccionario con estadísticas
        """
        self.connect()
        
        stats = {}
        
        # Total de pacientes
        self.cursor.execute("SELECT COUNT(*) as total FROM pacientes")
        stats['total_pacientes'] = self.cursor.fetchone()['total']
        
        # Total de diagnósticos
        self.cursor.execute("SELECT COUNT(*) as total FROM diagnosticos")
        stats['total_diagnosticos'] = self.cursor.fetchone()['total']
        
        # Diagnósticos más comunes
        self.cursor.execute("""
            SELECT diagnostico_principal, COUNT(*) as cantidad
            FROM diagnosticos
            GROUP BY diagnostico_principal
            ORDER BY cantidad DESC
            LIMIT 5
        """)
        stats['diagnosticos_comunes'] = [
            {'diagnostico': row['diagnostico_principal'], 'cantidad': row['cantidad']}
            for row in self.cursor.fetchall()
        ]
        
        # Urgencias más frecuentes
        self.cursor.execute("""
            SELECT urgencia, COUNT(*) as cantidad
            FROM diagnosticos
            GROUP BY urgencia
            ORDER BY cantidad DESC
        """)
        stats['urgencias'] = [
            {'urgencia': row['urgencia'], 'cantidad': row['cantidad']}
            for row in self.cursor.fetchall()
        ]
        
        self.disconnect()
        return stats
    
    def buscar_pacientes(self, termino_busqueda):
        """
        Busca pacientes por nombre
        
        Args:
            termino_busqueda: Término a buscar
        
        Returns:
            Lista de pacientes que coinciden
        """
        self.connect()
        
        self.cursor.execute("""
            SELECT id, nombre, edad, telefono, email, fecha_registro
            FROM pacientes
            WHERE nombre LIKE ?
            ORDER BY nombre
        """, (f'%{termino_busqueda}%',))
        
        pacientes = [dict(row) for row in self.cursor.fetchall()]
        
        self.disconnect()
        return pacientes
    
    def exportar_datos_csv(self, archivo_salida):
        """
        Exporta todos los diagnósticos a un archivo CSV
        
        Args:
            archivo_salida: Ruta del archivo CSV de salida
        """
        import csv
        
        self.connect()
        
        self.cursor.execute("""
            SELECT 
                p.nombre as paciente,
                d.fecha_diagnostico,
                d.diagnostico_principal,
                d.confianza_principal,
                d.gravedad,
                d.urgencia,
                d.num_sintomas_evaluados
            FROM diagnosticos d
            JOIN pacientes p ON d.paciente_id = p.id
            ORDER BY d.fecha_diagnostico DESC
        """)
        
        with open(archivo_salida, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Paciente', 'Fecha', 'Diagnóstico', 'Confianza %',
                'Gravedad', 'Urgencia', 'Síntomas Evaluados'
            ])
            
            for row in self.cursor.fetchall():
                writer.writerow([
                    row['paciente'],
                    row['fecha_diagnostico'],
                    row['diagnostico_principal'],
                    f"{row['confianza_principal']*100:.1f}",
                    row['gravedad'],
                    row['urgencia'],
                    row['num_sintomas_evaluados']
                ])
        
        self.disconnect()
        print(f"Datos exportados a: {archivo_salida}")
