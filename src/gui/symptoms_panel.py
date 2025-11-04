"""
Panel de Síntomas - Interfaz para ingreso de síntomas del paciente
CON DISEÑO MEJORADO Y AMIGABLE
"""

import tkinter as tk
from tkinter import ttk, messagebox


class SymptomsPanel(ttk.Frame):
    """Panel para capturar los síntomas del paciente con diseño mejorado"""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.symptoms = {}
        self.widgets = {}
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets del panel de síntomas"""
        
        # Título con estilo mejorado
        title = ttk.Label(
            self,
            text="📝 Ingrese los Síntomas del Paciente",
            font=('Segoe UI', 14, 'bold')
        )
        title.grid(row=0, column=0, columnspan=3, pady=10, sticky='w', padx=10)
        
        row = 1
        
        # === SECCIÓN: DOLOR ===
        section = ttk.LabelFrame(
            self,
            text="  💢 Características del Dolor  ",
            padding=10
        )
        section.grid(row=row, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        
        # Tipo de dolor
        ttk.Label(section, text="Tipo de Dolor:").grid(row=0, column=0, sticky='w', pady=3)
        self.widgets['tipo_dolor'] = ttk.Combobox(section, width=20, state='readonly')
        self.widgets['tipo_dolor']['values'] = ['agudo', 'punzante', 'constante', 
                                                  'pulsante', 'sordo', 'intermitente']
        self.widgets['tipo_dolor'].grid(row=0, column=1, padx=5, pady=3, sticky='w')
        self.widgets['tipo_dolor'].current(0)
        
        # Intensidad del dolor
        ttk.Label(section, text="Intensidad del Dolor (0-10):").grid(row=1, column=0, sticky='w', pady=3)
        self.widgets['intensidad_dolor'] = ttk.Scale(section, from_=0, to=10, orient='horizontal', length=200)
        self.widgets['intensidad_dolor'].grid(row=1, column=1, padx=5, pady=3, sticky='w')
        self.widgets['intensidad_dolor_label'] = ttk.Label(section, text="0")
        self.widgets['intensidad_dolor_label'].grid(row=1, column=2, padx=5)
        self.widgets['intensidad_dolor'].configure(
            command=lambda v: self.widgets['intensidad_dolor_label'].config(text=f"{int(float(v))}")
        )
        
        # Duración del dolor
        ttk.Label(section, text="Duración del Dolor:").grid(row=2, column=0, sticky='w', pady=3)
        self.widgets['duracion_dolor'] = ttk.Combobox(section, width=20, state='readonly')
        self.widgets['duracion_dolor']['values'] = ['menos_24h', '1_3_dias', '3_7_dias', 'mas_7_dias']
        self.widgets['duracion_dolor'].grid(row=2, column=1, padx=5, pady=3, sticky='w')
        self.widgets['duracion_dolor'].current(0)
        
        row += 1
        
        # === SECCIÓN: SENSIBILIDAD ===
        section = ttk.LabelFrame(self, text="Sensibilidad", padding=10)
        section.grid(row=row, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        
        # Sensibilidad al frío
        ttk.Label(section, text="Sensibilidad al Frío (0-10):").grid(row=0, column=0, sticky='w', pady=3)
        self.widgets['sensibilidad_frio'] = ttk.Scale(section, from_=0, to=10, orient='horizontal', length=200)
        self.widgets['sensibilidad_frio'].grid(row=0, column=1, padx=5, pady=3, sticky='w')
        self.widgets['sensibilidad_frio_label'] = ttk.Label(section, text="0")
        self.widgets['sensibilidad_frio_label'].grid(row=0, column=2, padx=5)
        self.widgets['sensibilidad_frio'].configure(
            command=lambda v: self.widgets['sensibilidad_frio_label'].config(text=f"{int(float(v))}")
        )
        
        # Sensibilidad al calor
        ttk.Label(section, text="Sensibilidad al Calor (0-10):").grid(row=1, column=0, sticky='w', pady=3)
        self.widgets['sensibilidad_calor'] = ttk.Scale(section, from_=0, to=10, orient='horizontal', length=200)
        self.widgets['sensibilidad_calor'].grid(row=1, column=1, padx=5, pady=3, sticky='w')
        self.widgets['sensibilidad_calor_label'] = ttk.Label(section, text="0")
        self.widgets['sensibilidad_calor_label'].grid(row=1, column=2, padx=5)
        self.widgets['sensibilidad_calor'].configure(
            command=lambda v: self.widgets['sensibilidad_calor_label'].config(text=f"{int(float(v))}")
        )
        
        # Sensibilidad al dulce
        ttk.Label(section, text="Sensibilidad al Dulce (0-10):").grid(row=2, column=0, sticky='w', pady=3)
        self.widgets['sensibilidad_dulce'] = ttk.Scale(section, from_=0, to=10, orient='horizontal', length=200)
        self.widgets['sensibilidad_dulce'].grid(row=2, column=1, padx=5, pady=3, sticky='w')
        self.widgets['sensibilidad_dulce_label'] = ttk.Label(section, text="0")
        self.widgets['sensibilidad_dulce_label'].grid(row=2, column=2, padx=5)
        self.widgets['sensibilidad_dulce'].configure(
            command=lambda v: self.widgets['sensibilidad_dulce_label'].config(text=f"{int(float(v))}")
        )
        
        row += 1
        
        # === SECCIÓN: DOLOR ESPECÍFICO ===
        section = ttk.LabelFrame(self, text="Dolor Específico", padding=10)
        section.grid(row=row, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        
        # Dolor al masticar
        ttk.Label(section, text="Dolor al Masticar (0-10):").grid(row=0, column=0, sticky='w', pady=3)
        self.widgets['dolor_masticar'] = ttk.Scale(section, from_=0, to=10, orient='horizontal', length=200)
        self.widgets['dolor_masticar'].grid(row=0, column=1, padx=5, pady=3, sticky='w')
        self.widgets['dolor_masticar_label'] = ttk.Label(section, text="0")
        self.widgets['dolor_masticar_label'].grid(row=0, column=2, padx=5)
        self.widgets['dolor_masticar'].configure(
            command=lambda v: self.widgets['dolor_masticar_label'].config(text=f"{int(float(v))}")
        )
        
        # Dolor a la presión
        ttk.Label(section, text="Dolor a la Presión (0-10):").grid(row=1, column=0, sticky='w', pady=3)
        self.widgets['dolor_presion'] = ttk.Scale(section, from_=0, to=10, orient='horizontal', length=200)
        self.widgets['dolor_presion'].grid(row=1, column=1, padx=5, pady=3, sticky='w')
        self.widgets['dolor_presion_label'] = ttk.Label(section, text="0")
        self.widgets['dolor_presion_label'].grid(row=1, column=2, padx=5)
        self.widgets['dolor_presion'].configure(
            command=lambda v: self.widgets['dolor_presion_label'].config(text=f"{int(float(v))}")
        )
        
        # Dolor nocturno
        ttk.Label(section, text="Dolor Nocturno (0-10):").grid(row=2, column=0, sticky='w', pady=3)
        self.widgets['dolor_nocturno'] = ttk.Scale(section, from_=0, to=10, orient='horizontal', length=200)
        self.widgets['dolor_nocturno'].grid(row=2, column=1, padx=5, pady=3, sticky='w')
        self.widgets['dolor_nocturno_label'] = ttk.Label(section, text="0")
        self.widgets['dolor_nocturno_label'].grid(row=2, column=2, padx=5)
        self.widgets['dolor_nocturno'].configure(
            command=lambda v: self.widgets['dolor_nocturno_label'].config(text=f"{int(float(v))}")
        )
        
        # Dolor de mandíbula
        ttk.Label(section, text="Dolor de Mandíbula (0-10):").grid(row=3, column=0, sticky='w', pady=3)
        self.widgets['dolor_mandibula'] = ttk.Scale(section, from_=0, to=10, orient='horizontal', length=200)
        self.widgets['dolor_mandibula'].grid(row=3, column=1, padx=5, pady=3, sticky='w')
        self.widgets['dolor_mandibula_label'] = ttk.Label(section, text="0")
        self.widgets['dolor_mandibula_label'].grid(row=3, column=2, padx=5)
        self.widgets['dolor_mandibula'].configure(
            command=lambda v: self.widgets['dolor_mandibula_label'].config(text=f"{int(float(v))}")
        )
        
        row += 1
        
        # === SECCIÓN: ENCÍAS ===
        section = ttk.LabelFrame(self, text="Estado de las Encías", padding=10)
        section.grid(row=row, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        
        # Inflamación de encías
        ttk.Label(section, text="Inflamación de Encías (0-10):").grid(row=0, column=0, sticky='w', pady=3)
        self.widgets['inflamacion_encias'] = ttk.Scale(section, from_=0, to=10, orient='horizontal', length=200)
        self.widgets['inflamacion_encias'].grid(row=0, column=1, padx=5, pady=3, sticky='w')
        self.widgets['inflamacion_encias_label'] = ttk.Label(section, text="0")
        self.widgets['inflamacion_encias_label'].grid(row=0, column=2, padx=5)
        self.widgets['inflamacion_encias'].configure(
            command=lambda v: self.widgets['inflamacion_encias_label'].config(text=f"{int(float(v))}")
        )
        
        # Sangrado de encías
        ttk.Label(section, text="Sangrado de Encías:").grid(row=1, column=0, sticky='w', pady=3)
        self.widgets['sangrado_encias'] = ttk.Combobox(section, width=20, state='readonly')
        self.widgets['sangrado_encias']['values'] = ['no', 'leve', 'moderado', 'severo']
        self.widgets['sangrado_encias'].grid(row=1, column=1, padx=5, pady=3, sticky='w')
        self.widgets['sangrado_encias'].current(0)
        
        # Color de encías
        ttk.Label(section, text="Color de Encías:").grid(row=2, column=0, sticky='w', pady=3)
        self.widgets['color_encias'] = ttk.Combobox(section, width=20, state='readonly')
        self.widgets['color_encias']['values'] = ['normal', 'rojo_claro', 'rojo_intenso', 'purpura']
        self.widgets['color_encias'].grid(row=2, column=1, padx=5, pady=3, sticky='w')
        self.widgets['color_encias'].current(0)
        
        # Retraimiento de encías
        ttk.Label(section, text="Retraimiento de Encías:").grid(row=3, column=0, sticky='w', pady=3)
        self.widgets['retraimiento_encias'] = ttk.Combobox(section, width=20, state='readonly')
        self.widgets['retraimiento_encias']['values'] = ['no', 'leve', 'moderado', 'severo']
        self.widgets['retraimiento_encias'].grid(row=3, column=1, padx=5, pady=3, sticky='w')
        self.widgets['retraimiento_encias'].current(0)
        
        row += 1
        
        # === SECCIÓN: OBSERVACIONES VISUALES ===
        section = ttk.LabelFrame(self, text="Observaciones Visuales", padding=10)
        section.grid(row=row, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        
        col_frame = ttk.Frame(section)
        col_frame.grid(row=0, column=0, columnspan=3, sticky='ew')
        
        # Columna 1
        col1 = ttk.Frame(col_frame)
        col1.pack(side='left', padx=10)
        
        self.widgets['caries_visible'] = tk.StringVar(value='no')
        ttk.Label(col1, text="¿Caries Visible?").pack(anchor='w')
        ttk.Radiobutton(col1, text="Sí", variable=self.widgets['caries_visible'], value='si').pack(anchor='w')
        ttk.Radiobutton(col1, text="No", variable=self.widgets['caries_visible'], value='no').pack(anchor='w')
        ttk.Radiobutton(col1, text="No estoy seguro", variable=self.widgets['caries_visible'], value='no_seguro').pack(anchor='w')
        
        # Columna 2
        col2 = ttk.Frame(col_frame)
        col2.pack(side='left', padx=10)
        
        self.widgets['mancha_oscura'] = tk.StringVar(value='no')
        ttk.Label(col2, text="¿Mancha Oscura?").pack(anchor='w')
        ttk.Radiobutton(col2, text="Sí", variable=self.widgets['mancha_oscura'], value='si').pack(anchor='w')
        ttk.Radiobutton(col2, text="No", variable=self.widgets['mancha_oscura'], value='no').pack(anchor='w')
        
        # Columna 3
        col3 = ttk.Frame(col_frame)
        col3.pack(side='left', padx=10)
        
        self.widgets['fractura_diente'] = tk.StringVar(value='no')
        ttk.Label(col3, text="¿Fractura de Diente?").pack(anchor='w')
        ttk.Radiobutton(col3, text="Sí", variable=self.widgets['fractura_diente'], value='si').pack(anchor='w')
        ttk.Radiobutton(col3, text="No", variable=self.widgets['fractura_diente'], value='no').pack(anchor='w')
        
        # Desgaste dental
        ttk.Label(section, text="Desgaste Dental:").grid(row=1, column=0, sticky='w', pady=3, padx=10)
        self.widgets['desgaste_dental'] = ttk.Combobox(section, width=20, state='readonly')
        self.widgets['desgaste_dental']['values'] = ['no', 'leve', 'moderado', 'severo']
        self.widgets['desgaste_dental'].grid(row=1, column=1, padx=5, pady=3, sticky='w')
        self.widgets['desgaste_dental'].current(0)
        
        row += 1
        
        # === SECCIÓN: SIGNOS DE INFECCIÓN ===
        section = ttk.LabelFrame(self, text="Signos de Infección", padding=10)
        section.grid(row=row, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        
        col_frame = ttk.Frame(section)
        col_frame.grid(row=0, column=0, columnspan=3, sticky='ew')
        
        # Columna 1
        col1 = ttk.Frame(col_frame)
        col1.pack(side='left', padx=10)
        
        self.widgets['hinchazon_cara'] = tk.StringVar(value='no')
        ttk.Label(col1, text="¿Hinchazón en la Cara?").pack(anchor='w')
        ttk.Radiobutton(col1, text="Sí", variable=self.widgets['hinchazon_cara'], value='si').pack(anchor='w')
        ttk.Radiobutton(col1, text="No", variable=self.widgets['hinchazon_cara'], value='no').pack(anchor='w')
        
        # Columna 2
        col2 = ttk.Frame(col_frame)
        col2.pack(side='left', padx=10)
        
        self.widgets['pus_visible'] = tk.StringVar(value='no')
        ttk.Label(col2, text="¿Pus Visible?").pack(anchor='w')
        ttk.Radiobutton(col2, text="Sí", variable=self.widgets['pus_visible'], value='si').pack(anchor='w')
        ttk.Radiobutton(col2, text="No", variable=self.widgets['pus_visible'], value='no').pack(anchor='w')
        
        # Columna 3
        col3 = ttk.Frame(col_frame)
        col3.pack(side='left', padx=10)
        
        self.widgets['fiebre'] = tk.StringVar(value='no')
        ttk.Label(col3, text="¿Fiebre?").pack(anchor='w')
        ttk.Radiobutton(col3, text="Sí", variable=self.widgets['fiebre'], value='si').pack(anchor='w')
        ttk.Radiobutton(col3, text="No", variable=self.widgets['fiebre'], value='no').pack(anchor='w')
        
        # Mal aliento
        ttk.Label(section, text="Mal Aliento:").grid(row=1, column=0, sticky='w', pady=3, padx=10)
        self.widgets['mal_aliento'] = ttk.Combobox(section, width=20, state='readonly')
        self.widgets['mal_aliento']['values'] = ['no', 'leve', 'moderado', 'severo']
        self.widgets['mal_aliento'].grid(row=1, column=1, padx=5, pady=3, sticky='w')
        self.widgets['mal_aliento'].current(0)
        
        row += 1
        
        # === SECCIÓN: OTROS SÍNTOMAS ===
        section = ttk.LabelFrame(self, text="Otros Síntomas", padding=10)
        section.grid(row=row, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        
        # Movilidad dental
        ttk.Label(section, text="Movilidad Dental:").grid(row=0, column=0, sticky='w', pady=3)
        self.widgets['movilidad_dental'] = ttk.Combobox(section, width=20, state='readonly')
        self.widgets['movilidad_dental']['values'] = ['no', 'leve', 'moderado', 'severo']
        self.widgets['movilidad_dental'].grid(row=0, column=1, padx=5, pady=3, sticky='w')
        self.widgets['movilidad_dental'].current(0)
        
        col_frame = ttk.Frame(section)
        col_frame.grid(row=1, column=0, columnspan=3, sticky='ew', pady=5)
        
        # Rechinar dientes
        col1 = ttk.Frame(col_frame)
        col1.pack(side='left', padx=10)
        
        self.widgets['rechinar_dientes'] = tk.StringVar(value='no')
        ttk.Label(col1, text="¿Rechina los Dientes?").pack(anchor='w')
        ttk.Radiobutton(col1, text="Sí", variable=self.widgets['rechinar_dientes'], value='si').pack(anchor='w')
        ttk.Radiobutton(col1, text="No", variable=self.widgets['rechinar_dientes'], value='no').pack(anchor='w')
        ttk.Radiobutton(col1, text="No estoy seguro", variable=self.widgets['rechinar_dientes'], value='no_seguro').pack(anchor='w')
        
        # Problemas de mordida
        col2 = ttk.Frame(col_frame)
        col2.pack(side='left', padx=10)
        
        self.widgets['problemas_mordida'] = tk.StringVar(value='no')
        ttk.Label(col2, text="¿Problemas de Mordida?").pack(anchor='w')
        ttk.Radiobutton(col2, text="Sí", variable=self.widgets['problemas_mordida'], value='si').pack(anchor='w')
        ttk.Radiobutton(col2, text="No", variable=self.widgets['problemas_mordida'], value='no').pack(anchor='w')
        
        row += 1
        
        # === SECCIÓN: ANTECEDENTES ===
        section = ttk.LabelFrame(self, text="Antecedentes Recientes", padding=10)
        section.grid(row=row, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        
        col_frame = ttk.Frame(section)
        col_frame.grid(row=0, column=0, columnspan=3, sticky='ew')
        
        # Tratamiento reciente
        col1 = ttk.Frame(col_frame)
        col1.pack(side='left', padx=10)
        
        self.widgets['tratamiento_reciente'] = tk.StringVar(value='no')
        ttk.Label(col1, text="¿Tratamiento Dental Reciente?").pack(anchor='w')
        ttk.Radiobutton(col1, text="Sí", variable=self.widgets['tratamiento_reciente'], value='si').pack(anchor='w')
        ttk.Radiobutton(col1, text="No", variable=self.widgets['tratamiento_reciente'], value='no').pack(anchor='w')
        
        # Trauma reciente
        col2 = ttk.Frame(col_frame)
        col2.pack(side='left', padx=10)
        
        self.widgets['trauma_reciente'] = tk.StringVar(value='no')
        ttk.Label(col2, text="¿Trauma Reciente?").pack(anchor='w')
        ttk.Radiobutton(col2, text="Sí", variable=self.widgets['trauma_reciente'], value='si').pack(anchor='w')
        ttk.Radiobutton(col2, text="No", variable=self.widgets['trauma_reciente'], value='no').pack(anchor='w')
        
        # Configurar el grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
    
    def get_symptoms(self):
        """Obtiene todos los síntomas ingresados"""
        symptoms = {}
        
        # Valores de escala (0-10)
        scale_widgets = [
            'intensidad_dolor', 'sensibilidad_frio', 'sensibilidad_calor',
            'sensibilidad_dulce', 'dolor_masticar', 'dolor_presion',
            'dolor_nocturno', 'inflamacion_encias', 'dolor_mandibula'
        ]
        
        for widget_name in scale_widgets:
            symptoms[widget_name] = int(self.widgets[widget_name].get())
        
        # Valores de combobox
        combo_widgets = [
            'tipo_dolor', 'duracion_dolor', 'sangrado_encias', 'color_encias',
            'retraimiento_encias', 'desgaste_dental', 'mal_aliento', 'movilidad_dental'
        ]
        
        for widget_name in combo_widgets:
            symptoms[widget_name] = self.widgets[widget_name].get()
        
        # Valores de radiobutton (StringVar)
        radio_widgets = [
            'caries_visible', 'mancha_oscura', 'fractura_diente', 'hinchazon_cara',
            'pus_visible', 'fiebre', 'rechinar_dientes', 'problemas_mordida',
            'tratamiento_reciente', 'trauma_reciente'
        ]
        
        for widget_name in radio_widgets:
            symptoms[widget_name] = self.widgets[widget_name].get()
        
        return symptoms
    
    def reset(self):
        """Resetea todos los campos a sus valores por defecto"""
        # Resetear escalas
        scale_widgets = [
            'intensidad_dolor', 'sensibilidad_frio', 'sensibilidad_calor',
            'sensibilidad_dulce', 'dolor_masticar', 'dolor_presion',
            'dolor_nocturno', 'inflamacion_encias', 'dolor_mandibula'
        ]
        
        for widget_name in scale_widgets:
            self.widgets[widget_name].set(0)
        
        # Resetear combobox
        combo_widgets = [
            'tipo_dolor', 'duracion_dolor', 'sangrado_encias', 'color_encias',
            'retraimiento_encias', 'desgaste_dental', 'mal_aliento', 'movilidad_dental'
        ]
        
        for widget_name in combo_widgets:
            self.widgets[widget_name].current(0)
        
        # Resetear radiobuttons
        radio_widgets = [
            'caries_visible', 'mancha_oscura', 'fractura_diente', 'hinchazon_cara',
            'pus_visible', 'fiebre', 'rechinar_dientes', 'problemas_mordida',
            'tratamiento_reciente', 'trauma_reciente'
        ]
        
        for widget_name in radio_widgets:
            self.widgets[widget_name].set('no')
