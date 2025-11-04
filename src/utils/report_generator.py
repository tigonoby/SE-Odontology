"""
Generador de Reportes PDF
Crea reportes PDF con los resultados del diagnóstico
"""

import os
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.colors import HexColor


class ReportGenerator:
    """Generador de reportes PDF para diagnósticos"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
    
    def setup_custom_styles(self):
        """Configura estilos personalizados"""
        # Estilo para título principal
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=HexColor('#007bff'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Estilo para subtítulos
        self.styles.add(ParagraphStyle(
            name='CustomHeading',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=HexColor('#343a40'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Estilo para texto normal
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['Normal'],
            fontSize=11,
            alignment=TA_JUSTIFY,
            spaceAfter=10
        ))
        
        # Estilo para advertencias
        self.styles.add(ParagraphStyle(
            name='Warning',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=HexColor('#856404'),
            backColor=HexColor('#fff3cd'),
            borderColor=HexColor('#ffc107'),
            borderWidth=1,
            borderPadding=10,
            spaceAfter=10
        ))
    
    def generate_report(self, patient_name, symptoms, diagnosis, output_path, patient_info=None):
        """
        Genera un reporte PDF completo
        
        Args:
            patient_name: nombre del paciente
            symptoms: diccionario de síntomas
            diagnosis: resultado del diagnóstico
            output_path: ruta donde guardar el PDF
            patient_info: diccionario con edad, teléfono, email (opcional)
        """
        # Asegurar que el directorio existe
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        
        # Crear documento
        doc = SimpleDocTemplate(
            output_path,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Contenido del documento
        story = []
        
        # Encabezado
        story.extend(self._create_header(patient_name, patient_info))
        
        # Información del diagnóstico
        if diagnosis and diagnosis.get('num_diagnosticos', 0) > 0:
            story.extend(self._create_diagnosis_section(diagnosis))
            story.extend(self._create_recommendations_section(diagnosis))
            
            if diagnosis['num_diagnosticos'] > 1:
                story.extend(self._create_alternatives_section(diagnosis))
        else:
            story.append(Paragraph(
                "No se pudo determinar un diagnóstico con los síntomas proporcionados.",
                self.styles['CustomBody']
            ))
        
        # Síntomas reportados
        story.extend(self._create_symptoms_section(symptoms))
        
        # Información adicional
        story.extend(self._create_info_section(diagnosis))
        
        # Advertencia legal
        story.extend(self._create_warning_section())
        
        # Construir PDF
        doc.build(story)
    
    def _create_header(self, patient_name, patient_info=None):
        """Crea el encabezado del reporte"""
        elements = []
        
        # Título
        elements.append(Paragraph(
            "🦷 REPORTE DE DIAGNÓSTICO ODONTOLÓGICO",
            self.styles['CustomTitle']
        ))
        
        elements.append(Spacer(1, 0.2 * inch))
        
        # Información del paciente - usar Paragraph para formatear correctamente
        patient_data = [
            [Paragraph('<b>Paciente:</b>', self.styles['Normal']), Paragraph(patient_name, self.styles['Normal'])],
            [Paragraph('<b>Fecha:</b>', self.styles['Normal']), Paragraph(datetime.now().strftime('%d/%m/%Y %H:%M'), self.styles['Normal'])],
        ]
        
        # Agregar edad si está disponible
        if patient_info and patient_info.get('edad'):
            patient_data.append([
                Paragraph('<b>Edad:</b>', self.styles['Normal']), 
                Paragraph(f"{patient_info['edad']} años", self.styles['Normal'])
            ])
        
        # Agregar teléfono si está disponible
        if patient_info and patient_info.get('telefono'):
            patient_data.append([
                Paragraph('<b>Teléfono:</b>', self.styles['Normal']), 
                Paragraph(patient_info['telefono'], self.styles['Normal'])
            ])
        
        # Agregar email si está disponible
        if patient_info and patient_info.get('email'):
            patient_data.append([
                Paragraph('<b>Email:</b>', self.styles['Normal']), 
                Paragraph(patient_info['email'], self.styles['Normal'])
            ])
        
        patient_data.append([
            Paragraph('<b>Sistema:</b>', self.styles['Normal']), 
            Paragraph('Sistema Experto de Odontología v1.0', self.styles['Normal'])
        ])
        
        table = Table(patient_data, colWidths=[2*inch, 4*inch])
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 0.3 * inch))
        
        return elements
    
    def _create_diagnosis_section(self, diagnosis):
        """Crea la sección de diagnóstico principal"""
        elements = []
        
        principal = diagnosis['principal']
        
        # Título de sección
        elements.append(Paragraph(
            "DIAGNÓSTICO PRINCIPAL",
            self.styles['CustomHeading']
        ))
        
        # Información del diagnóstico - usar Paragraph para cada celda
        diag_data = [
            [Paragraph('<b>Diagnóstico:</b>', self.styles['Normal']), Paragraph(principal['nombre'], self.styles['Normal'])],
            [Paragraph('<b>Descripción:</b>', self.styles['Normal']), Paragraph(principal['descripcion'], self.styles['Normal'])],
            [Paragraph('<b>Confianza:</b>', self.styles['Normal']), Paragraph(f"{principal['confianza_porcentaje']}%", self.styles['Normal'])],
            [Paragraph('<b>Gravedad:</b>', self.styles['Normal']), Paragraph(principal['gravedad'].upper(), self.styles['Normal'])],
            [Paragraph('<b>Urgencia:</b>', self.styles['Normal']), Paragraph(principal['urgencia'].upper(), self.styles['Normal'])],
            [Paragraph('<b>Regla aplicada:</b>', self.styles['Normal']), Paragraph(principal['regla'], self.styles['Normal'])]
        ]
        
        table = Table(diag_data, colWidths=[2*inch, 4.5*inch])
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 0.2 * inch))
        
        return elements
    
    def _create_recommendations_section(self, diagnosis):
        """Crea la sección de recomendaciones"""
        elements = []
        
        principal = diagnosis['principal']
        
        if not principal.get('recomendaciones'):
            return elements
        
        # Título
        elements.append(Paragraph(
            "RECOMENDACIONES",
            self.styles['CustomHeading']
        ))
        
        # Lista de recomendaciones
        for i, rec in enumerate(principal['recomendaciones'], 1):
            elements.append(Paragraph(
                f"{i}. {rec}",
                self.styles['CustomBody']
            ))
        
        elements.append(Spacer(1, 0.2 * inch))
        
        return elements
    
    def _create_alternatives_section(self, diagnosis):
        """Crea la sección de diagnósticos alternativos"""
        elements = []
        
        diagnosticos = diagnosis['diagnosticos'][1:4]  # Hasta 3 alternativos
        
        if not diagnosticos:
            return elements
        
        # Título
        elements.append(Paragraph(
            "DIAGNÓSTICOS ALTERNATIVOS",
            self.styles['CustomHeading']
        ))
        
        # Tabla de alternativos
        data = [['Diagnóstico', 'Confianza', 'Descripción']]
        
        for diag in diagnosticos:
            data.append([
                diag['nombre'],
                f"{diag['confianza_porcentaje']}%",
                diag['descripcion'][:100] + '...' if len(diag['descripcion']) > 100 else diag['descripcion']
            ])
        
        table = Table(data, colWidths=[2*inch, 1*inch, 3.5*inch])
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 0.2 * inch))
        
        return elements
    
    def _create_symptoms_section(self, symptoms):
        """Crea la sección de síntomas reportados"""
        elements = []
        
        # Título
        elements.append(Paragraph(
            "SÍNTOMAS REPORTADOS",
            self.styles['CustomHeading']
        ))
        
        # Filtrar síntomas relevantes
        relevant_symptoms = []
        
        for key, value in symptoms.items():
            if isinstance(value, (int, float)) and value > 0:
                # Convertir nombre de variable a texto legible
                readable_name = key.replace('_', ' ').title()
                relevant_symptoms.append([readable_name, str(value)])
            elif isinstance(value, str) and value not in ['no', 'normal']:
                readable_name = key.replace('_', ' ').title()
                readable_value = value.replace('_', ' ').title()
                relevant_symptoms.append([readable_name, readable_value])
        
        if relevant_symptoms:
            # Dividir en dos columnas
            mid = len(relevant_symptoms) // 2 + len(relevant_symptoms) % 2
            col1 = relevant_symptoms[:mid]
            col2 = relevant_symptoms[mid:]
            
            # Igualar longitudes
            while len(col1) > len(col2):
                col2.append(['', ''])
            
            # Combinar columnas
            data = []
            for i in range(max(len(col1), len(col2))):
                row = []
                if i < len(col1):
                    row.extend(col1[i])
                else:
                    row.extend(['', ''])
                if i < len(col2):
                    row.extend(col2[i])
                else:
                    row.extend(['', ''])
                data.append(row)
            
            table = Table(data, colWidths=[2*inch, 1.2*inch, 2*inch, 1.2*inch])
            table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
            ]))
            
            elements.append(table)
        else:
            elements.append(Paragraph(
                "No se reportaron síntomas significativos.",
                self.styles['CustomBody']
            ))
        
        elements.append(Spacer(1, 0.2 * inch))
        
        return elements
    
    def _create_info_section(self, diagnosis):
        """Crea la sección de información adicional"""
        elements = []
        
        # Título
        elements.append(Paragraph(
            "INFORMACIÓN DEL DIAGNÓSTICO",
            self.styles['CustomHeading']
        ))
        
        info_text = f"""
        <b>Síntomas evaluados:</b> {diagnosis.get('sintomas_evaluados', 0)}<br/>
        <b>Diagnósticos encontrados:</b> {diagnosis.get('num_diagnosticos', 0)}<br/>
        <b>Lógica difusa utilizada:</b> {'Sí' if diagnosis.get('usa_logica_fuzzy') else 'No'}<br/>
        <b>Método de inferencia:</b> Encadenamiento hacia adelante (Forward Chaining)
        """
        
        elements.append(Paragraph(info_text, self.styles['CustomBody']))
        elements.append(Spacer(1, 0.2 * inch))
        
        return elements
    
    def _create_warning_section(self):
        """Crea la sección de advertencia legal"""
        elements = []
        
        warning_text = """
        <b>⚠️ ADVERTENCIA IMPORTANTE</b><br/><br/>
        Este sistema es únicamente una herramienta de orientación preliminar y 
        <b>NO reemplaza el diagnóstico de un profesional odontólogo</b>.<br/><br/>
        Siempre consulte con un dentista certificado para un diagnóstico definitivo 
        y tratamiento adecuado. Este reporte no debe ser utilizado como sustituto 
        de atención médica profesional.<br/><br/>
        El sistema experto proporciona sugerencias basadas en reglas y lógica difusa, 
        pero solo un profesional de la salud puede realizar un diagnóstico preciso 
        mediante examen clínico directo.
        """
        
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph(warning_text, self.styles['Warning']))
        
        # Pie de página
        footer_text = f"""
        <br/><br/>
        <i>Reporte generado por Sistema Experto de Odontología v1.0<br/>
        Proyecto Educativo - Universidad<br/>
        © {datetime.now().year}</i>
        """
        
        elements.append(Paragraph(footer_text, self.styles['Normal']))
        
        return elements
