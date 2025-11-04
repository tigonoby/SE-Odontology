# 🗄️ Base de Datos - Sistema Experto de Odontología

## Descripción General

El sistema utiliza **SQLite** como base de datos local. SQLite es perfecto para este proyecto porque:
- ✅ No requiere instalación de servidor
- ✅ Es portátil (un solo archivo .db)
- ✅ Fácil de usar y mantener
- ✅ Perfecto para aplicaciones de escritorio
- ✅ Puede migrar a MySQL fácilmente si se necesita

## Ubicación de la Base de Datos

```
Proyecto/
└── data/
    └── odontologia.db  ← Archivo de base de datos SQLite
```

## Estructura de la Base de Datos

### 📋 Tabla: `pacientes`

Almacena información de los pacientes.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | ID único del paciente |
| nombre | TEXT NOT NULL | Nombre completo del paciente |
| edad | INTEGER | Edad del paciente (opcional) |
| telefono | TEXT | Teléfono de contacto (opcional) |
| email | TEXT | Correo electrónico (opcional) |
| fecha_registro | TIMESTAMP | Fecha de primer registro |
| notas | TEXT | Notas adicionales (opcional) |

### 🩺 Tabla: `diagnosticos`

Almacena los diagnósticos realizados.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | ID único del diagnóstico |
| paciente_id | INTEGER NOT NULL | FK a pacientes |
| fecha_diagnostico | TIMESTAMP | Fecha/hora del diagnóstico |
| diagnostico_principal | TEXT NOT NULL | Nombre del diagnóstico |
| confianza_principal | REAL NOT NULL | Nivel de confianza (0.0 - 1.0) |
| gravedad | TEXT | Nivel de gravedad |
| urgencia | TEXT | Nivel de urgencia |
| descripcion | TEXT | Descripción del diagnóstico |
| diagnosticos_alternativos | TEXT | JSON con diagnósticos alternativos |
| num_sintomas_evaluados | INTEGER | Cantidad de síntomas evaluados |
| usa_logica_fuzzy | BOOLEAN | Si se usó lógica difusa |

### 🔬 Tabla: `sintomas`

Almacena los síntomas evaluados en cada diagnóstico.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | ID único del síntoma |
| diagnostico_id | INTEGER NOT NULL | FK a diagnosticos |
| nombre_sintoma | TEXT NOT NULL | Nombre del síntoma |
| valor_sintoma | TEXT NOT NULL | Valor del síntoma |
| tipo_sintoma | TEXT | Tipo: numerico, categorico, booleano |

### 💊 Tabla: `recomendaciones`

Almacena las recomendaciones asociadas a cada diagnóstico.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | ID único de la recomendación |
| diagnostico_id | INTEGER NOT NULL | FK a diagnosticos |
| recomendacion | TEXT NOT NULL | Texto de la recomendación |
| orden | INTEGER | Orden de prioridad |

## Diagrama de Relaciones

```
┌─────────────┐
│  pacientes  │
│─────────────│
│ id (PK)     │
│ nombre      │
│ edad        │
│ telefono    │
│ email       │
│ ...         │
└──────┬──────┘
       │
       │ 1:N
       │
┌──────▼──────────┐
│  diagnosticos   │
│─────────────────│
│ id (PK)         │
│ paciente_id(FK) │
│ fecha           │
│ diagnostico     │
│ confianza       │
│ gravedad        │
│ urgencia        │
│ ...             │
└──────┬──────────┘
       │
       ├─────────────────┐
       │ 1:N             │ 1:N
       │                 │
┌──────▼────────┐ ┌──────▼────────────┐
│   sintomas    │ │  recomendaciones  │
│───────────────│ │───────────────────│
│ id (PK)       │ │ id (PK)           │
│ diag_id (FK)  │ │ diag_id (FK)      │
│ nombre        │ │ recomendacion     │
│ valor         │ │ orden             │
│ tipo          │ │                   │
└───────────────┘ └───────────────────┘
```

## 🚀 Uso desde la Interfaz

### 1. Guardar Diagnóstico (Automático)

Cada vez que presionas el botón **"Diagnosticar"**, el sistema:
1. Realiza el diagnóstico
2. **Guarda automáticamente** en la base de datos
3. Muestra confirmación en la barra de estado
4. Retorna el ID del diagnóstico guardado

**Ejemplo de mensaje:**
```
✓ Diagnóstico completado y guardado (ID: 15)
```

### 2. Ver Historial del Paciente

**Menú → Base de Datos → Ver Historial del Paciente**

- Muestra todos los diagnósticos previos del paciente actual
- Tabla con: Fecha, Diagnóstico, Confianza, Urgencia
- Botón "Ver Detalles" para información completa

### 3. Buscar Pacientes

**Menú → Base de Datos → Buscar Pacientes**

- Busca pacientes por nombre
- Muestra lista de resultados
- Permite ver cuándo se registraron

### 4. Ver Estadísticas

**Menú → Base de Datos → Estadísticas**

Muestra:
- 📊 Total de pacientes registrados
- 📊 Total de diagnósticos realizados
- 📊 Diagnósticos más comunes (Top 5)
- 📊 Urgencias registradas

### 5. Exportar a CSV

**Menú → Base de Datos → Exportar Datos a CSV**

- Exporta toda la información a formato CSV
- Compatible con Excel
- Incluye: Paciente, Fecha, Diagnóstico, Confianza, Gravedad, Urgencia

## 💻 Uso Programático

### Ejemplo 1: Guardar un Diagnóstico

```python
from src.database.db_manager import DatabaseManager

# Inicializar
db = DatabaseManager()

# Guardar diagnóstico
diagnostico_id = db.guardar_diagnostico(
    paciente_nombre="Juan Pérez",
    resultado_diagnostico={
        'principal': {
            'nombre': 'Caries Dental',
            'confianza': 0.85,
            'gravedad': 'media',
            'urgencia': 'moderada',
            'descripcion': 'Deterioro del esmalte...',
            'recomendaciones': [
                'Agende cita con odontólogo',
                'Evite alimentos azucarados'
            ]
        },
        'diagnosticos': [...],
        'sintomas_evaluados': 15,
        'usa_logica_fuzzy': True
    },
    sintomas_dict={
        'intensidad_dolor': 7,
        'sensibilidad_frio': 8,
        'caries_visible': 'si'
    }
)

print(f"Diagnóstico guardado con ID: {diagnostico_id}")
```

### Ejemplo 2: Obtener Historial

```python
# Obtener historial de un paciente
historial = db.obtener_historial_paciente("Juan Pérez")

for diag in historial:
    print(f"{diag['fecha']}: {diag['diagnostico']} ({diag['confianza']*100}%)")
```

### Ejemplo 3: Obtener Estadísticas

```python
# Obtener estadísticas
stats = db.obtener_estadisticas()

print(f"Total pacientes: {stats['total_pacientes']}")
print(f"Total diagnósticos: {stats['total_diagnosticos']}")

print("\nDiagnósticos más comunes:")
for diag in stats['diagnosticos_comunes']:
    print(f"- {diag['diagnostico']}: {diag['cantidad']} casos")
```

### Ejemplo 4: Exportar a CSV

```python
# Exportar todos los datos
db.exportar_datos_csv("diagnosticos_2025.csv")
```

## 🔄 Migración a MySQL (Opcional)

Si en el futuro necesitas usar MySQL en lugar de SQLite:

### 1. Instalar conector MySQL

```bash
pip install mysql-connector-python
```

### 2. Modificar `db_manager.py`

Cambia la conexión en el método `connect()`:

```python
import mysql.connector

def connect(self):
    try:
        self.connection = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_password",
            database="odontologia_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)
        return True
    except Exception as e:
        print(f"Error conectando a MySQL: {e}")
        return False
```

### 3. Crear la base de datos en MySQL

```sql
CREATE DATABASE odontologia_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Las tablas se crearán automáticamente al ejecutar la aplicación.

## 📊 Consultas SQL Útiles

### Ver todos los pacientes

```sql
SELECT * FROM pacientes ORDER BY nombre;
```

### Ver diagnósticos recientes

```sql
SELECT 
    p.nombre,
    d.fecha_diagnostico,
    d.diagnostico_principal,
    d.confianza_principal
FROM diagnosticos d
JOIN pacientes p ON d.paciente_id = p.id
ORDER BY d.fecha_diagnostico DESC
LIMIT 10;
```

### Contar diagnósticos por urgencia

```sql
SELECT 
    urgencia,
    COUNT(*) as cantidad
FROM diagnosticos
GROUP BY urgencia
ORDER BY cantidad DESC;
```

### Buscar pacientes con diagnósticos urgentes

```sql
SELECT DISTINCT
    p.nombre,
    p.telefono,
    d.diagnostico_principal,
    d.fecha_diagnostico
FROM pacientes p
JOIN diagnosticos d ON p.id = d.paciente_id
WHERE d.urgencia = 'urgente'
ORDER BY d.fecha_diagnostico DESC;
```

### Síntomas más comunes

```sql
SELECT 
    nombre_sintoma,
    COUNT(*) as frecuencia,
    AVG(CAST(valor_sintoma AS REAL)) as valor_promedio
FROM sintomas
WHERE tipo_sintoma = 'numerico'
GROUP BY nombre_sintoma
ORDER BY frecuencia DESC
LIMIT 10;
```

## 🔐 Seguridad y Respaldo

### Respaldo de la Base de Datos

1. **Copia simple** (SQLite):
   ```bash
   copy "data\odontologia.db" "backups\odontologia_backup_20251104.db"
   ```

2. **Exportar a CSV** desde la aplicación:
   - Menú → Base de Datos → Exportar Datos a CSV

### Recomendaciones

- ✅ Realiza respaldos periódicos (semanal/mensual)
- ✅ Guarda los respaldos en ubicación segura
- ✅ Verifica la integridad de los respaldos
- ✅ No compartas la base de datos sin anonimizar

## 📝 Notas Técnicas

- **Motor de BD**: SQLite 3
- **Codificación**: UTF-8
- **Tamaño máximo**: Prácticamente ilimitado para este uso
- **Concurrencia**: Soporta múltiples lecturas, una escritura
- **Transacciones**: ACID compliant
- **Índices**: Automáticos en Primary Keys y Foreign Keys

## ✅ Ventajas del Sistema

1. **Sin configuración**: No requiere instalar servidor de BD
2. **Portátil**: Todo en un archivo .db
3. **Rápido**: Excelente rendimiento para este volumen de datos
4. **Confiable**: ACID compliant, no pierde datos
5. **Fácil respaldo**: Simplemente copia el archivo .db
6. **Escalable**: Puede migrar a MySQL si crece mucho

## 🎓 Para el Proyecto Universitario

Esta implementación demuestra:
- ✅ Persistencia de datos
- ✅ Modelado de base de datos relacional
- ✅ Normalización correcta (3FN)
- ✅ Relaciones 1:N apropiadas
- ✅ Integridad referencial con Foreign Keys
- ✅ Consultas y reportes
- ✅ Exportación de datos
- ✅ Interfaz gráfica integrada con BD

---

*Desarrollado para el Sistema Experto de Odontología*
*Noviembre 2025*
