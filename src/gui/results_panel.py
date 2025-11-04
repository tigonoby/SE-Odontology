"""
Panel de Resultados - Muestra el diagnóstico y recomendaciones
CON DISEÑO MEJORADO Y AMIGABLE
"""

import tkinter as tk
from tkinter import ttk, scrolledtext


class ResultsPanel(tk.Frame):
    """Panel para mostrar los resultados del diagnóstico con diseño mejorado"""
    
    def __init__(self, parent):
        super().__init__(parent, bg='white')
        self.results = None
        self.colors = {
            'primary': '#2E86AB',
            'success': '#06A77D',
            'warning': '#F18F01',
            'danger': '#C73E1D',
            'light': '#F4F4F9',
            'dark': '#2B2D42',
            'white': '#FFFFFF',
            'border': '#E0E0E0'
        }
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets del panel de resultados"""
        
        # Título con estilo
        title_frame = tk.Frame(self, bg=self.colors['light'], height=50)
        title_frame.pack(fill='x', pady=(0, 10))
        title_frame.pack_propagate(False)
        
        title = tk.Label(
            title_frame,
            text="📊 Resultados del Diagnóstico",
            font=('Segoe UI', 14, 'bold'),
            bg=self.colors['light'],
            fg=self.colors['dark']
        )
        title.pack(pady=10, padx=15, anchor='w')
        
        # Frame principal con scroll
        main_frame = tk.Frame(self, bg='white')
        main_frame.pack(fill='both', expand=True)
        
        # Canvas y scrollbar
        canvas = tk.Canvas(main_frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg='white')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Scroll con mouse wheel
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", on_mousewheel)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Mensaje inicial elegante
        self.initial_container = tk.Frame(self.scrollable_frame, bg='white')
        self.initial_container.pack(fill='both', expand=True, pady=50)
        
        icon_label = tk.Label(
            self.initial_container,
            text="ℹ️",
            font=('Segoe UI', 48),
            bg='white',
            fg=self.colors['primary']
        )
        icon_label.pack(pady=(20, 10))
        
        self.initial_message = tk.Label(
            self.initial_container,
            text="No se pudo determinar un diagnóstico con los síntomas\nproporcionados.",
            font=('Segoe UI', 11),
            bg='white',
            fg='gray',
            justify='center'
        )
        self.initial_message.pack(pady=10)
        
        advice = tk.Label(
            self.initial_container,
            text="Por favor, verifique los síntomas ingresados o consulte a un odontólogo.",
            font=('Segoe UI', 9, 'italic'),
            bg='white',
            fg='gray',
            justify='center'
        )
        advice.pack(pady=5)
    
    def display_results(self, diagnosis_result):
        """
        Muestra los resultados del diagnóstico con diseño mejorado
        diagnosis_result: diccionario con el resultado del diagnóstico
        """
        self.results = diagnosis_result
        
        # Limpiar contenido previo
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        if not diagnosis_result or diagnosis_result.get('num_diagnosticos', 0) == 0:
            self.display_no_diagnosis()
            return
        
        # Container principal
        container = tk.Frame(self.scrollable_frame, bg='white')
        container.pack(fill='both', expand=True, padx=15, pady=10)
        
        # Obtener diagnóstico principal
        principal = diagnosis_result.get('principal')
        if not principal:
            self.display_no_diagnosis()
            return
        
        # === TARJETA DE URGENCIA ===
        urgencia_colors = {
            'urgente': ('#C73E1D', '🚨 ATENCIÓN URGENTE REQUERIDA'),
            'alta': ('#F18F01', '⚠️ Consulte a un odontólogo pronto'),
            'moderada': ('#F9C80E', '📅 Agende una cita odontológica'),
            'baja': ('#06A77D', 'ℹ️ Consulta preventiva recomendada')
        }
        
        urgencia = principal.get('urgencia', 'baja')
        color, mensaje = urgencia_colors.get(urgencia, ('#06A77D', 'ℹ️ Consulta recomendada'))
        
        urgencia_card = tk.Frame(container, bg=color, relief='flat')
        urgencia_card.pack(fill='x', pady=(0, 15))
        
        urgencia_label = tk.Label(
            urgencia_card,
            text=mensaje,
            font=('Segoe UI', 13, 'bold'),
            bg=color,
            fg='white',
            pady=15
        )
        urgencia_label.pack()
        
        # === TARJETA DE DIAGNÓSTICO PRINCIPAL ===
        diag_card = tk.Frame(container, bg='white', relief='solid', bd=1, highlightbackground=self.colors['border'])
        diag_card.pack(fill='x', pady=(0, 15))
        
        # Header del diagnóstico
        diag_header = tk.Frame(diag_card, bg=self.colors['primary'], height=40)
        diag_header.pack(fill='x')
        diag_header.pack_propagate(False)
        
        tk.Label(
            diag_header,
            text="🎯 Diagnóstico Principal",
            font=('Segoe UI', 12, 'bold'),
            bg=self.colors['primary'],
            fg='white'
        ).pack(side='left', padx=15, pady=8)
        
        # Contenido del diagnóstico
        diag_content = tk.Frame(diag_card, bg='white')
        diag_content.pack(fill='both', expand=True, padx=20, pady=15)
        
        # Nombre del diagnóstico
        tk.Label(
            diag_content,
            text=principal['nombre'],
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['dark']
        ).pack(anchor='w', pady=(0, 10))
        
        # Descripción
        tk.Label(
            diag_content,
            text=principal['descripcion'],
            font=('Segoe UI', 10),
            bg='white',
            fg='#666',
            wraplength=500,
            justify='left'
        ).pack(anchor='w', pady=(0, 15))
        
        # Confianza con barra visual
        conf_frame = tk.Frame(diag_content, bg='white')
        conf_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(
            conf_frame,
            text=f"📊 Nivel de Confianza: {principal['confianza_porcentaje']}%",
            font=('Segoe UI', 10, 'bold'),
            bg='white',
            fg=self.colors['dark']
        ).pack(anchor='w')
        
        # Barra de confianza personalizada
        bar_bg = tk.Frame(conf_frame, bg='#E0E0E0', height=25)
        bar_bg.pack(fill='x', pady=5)
        
        bar_width = int(500 * (principal['confianza_porcentaje'] / 100))
        bar_color = self.colors['success'] if principal['confianza_porcentaje'] >= 70 else \
                    self.colors['warning'] if principal['confianza_porcentaje'] >= 40 else \
                    self.colors['danger']
        
        bar_fg = tk.Frame(bar_bg, bg=bar_color, height=25, width=bar_width)
        bar_fg.pack(side='left', fill='y')
        
        tk.Label(
            bar_fg,
            text=f"{principal['confianza_porcentaje']}%",
            font=('Segoe UI', 9, 'bold'),
            bg=bar_color,
            fg='white'
        ).pack(side='right', padx=10) if bar_width > 50 else None
        
        # Info de gravedad y urgencia
        info_frame = tk.Frame(diag_content, bg='white')
        info_frame.pack(fill='x', pady=(10, 0))
        
        # Gravedad
        grav_frame = tk.Frame(info_frame, bg=self.colors['light'], relief='flat')
        grav_frame.pack(side='left', padx=(0, 10), pady=5)
        
        tk.Label(
            grav_frame,
            text=f"⚖️ Gravedad: {principal['gravedad'].upper()}",
            font=('Segoe UI', 9, 'bold'),
            bg=self.colors['light'],
            fg=self.colors['dark'],
            padx=10,
            pady=5
        ).pack()
        
        # Urgencia
        urg_frame = tk.Frame(info_frame, bg=self.colors['light'], relief='flat')
        urg_frame.pack(side='left', pady=5)
        
        tk.Label(
            urg_frame,
            text=f"⏰ Urgencia: {principal['urgencia'].upper()}",
            font=('Segoe UI', 9, 'bold'),
            bg=self.colors['light'],
            fg=self.colors['dark'],
            padx=10,
            pady=5
        ).pack()
        
        # Regla que se activó
        tk.Label(
            diag_content,
            text=f"💡 Regla aplicada: {principal['regla']}",
            font=('Segoe UI', 8, 'italic'),
            bg='white',
            fg='#999'
        ).pack(anchor='w', pady=(10, 0))
        
        # === TARJETA DE RECOMENDACIONES ===
        if principal and principal.get('recomendaciones'):
            rec_card = tk.Frame(container, bg='white', relief='solid', bd=1, highlightbackground=self.colors['border'])
            rec_card.pack(fill='x', pady=(0, 15))
            
            # Header de recomendaciones
            rec_header = tk.Frame(rec_card, bg=self.colors['success'], height=40)
            rec_header.pack(fill='x')
            rec_header.pack_propagate(False)
            
            tk.Label(
                rec_header,
                text="💊 Recomendaciones",
                font=('Segoe UI', 12, 'bold'),
                bg=self.colors['success'],
                fg='white'
            ).pack(side='left', padx=15, pady=8)
            
            # Contenido de recomendaciones
            rec_content = tk.Frame(rec_card, bg='white')
            rec_content.pack(fill='both', expand=True, padx=20, pady=15)
            
            for i, rec in enumerate(principal['recomendaciones'], 1):
                rec_frame = tk.Frame(rec_content, bg='white')
                rec_frame.pack(fill='x', pady=5)
                
                # Bullet point
                tk.Label(
                    rec_frame,
                    text=f"✓",
                    font=('Segoe UI', 12, 'bold'),
                    bg='white',
                    fg=self.colors['success']
                ).pack(side='left', padx=(0, 10))
                
                # Texto de recomendación
                rec_text = f"{rec}"
                tk.Label(
                    rec_frame,
                    text=rec_text,
                    font=('Segoe UI', 10),
                    bg='white',
                    fg=self.colors['dark'],
                    wraplength=480,
                    justify='left'
                ).pack(side='left', fill='x', expand=True)
        
        # === DIAGNÓSTICOS ALTERNATIVOS ===
        diagnosticos = diagnosis_result.get('diagnosticos', [])
        if len(diagnosticos) > 1:
            alt_card = tk.Frame(container, bg='white', relief='solid', bd=1, highlightbackground=self.colors['border'])
            alt_card.pack(fill='x', pady=(0, 15))
            
            # Header
            alt_header = tk.Frame(alt_card, bg=self.colors['warning'], height=40)
            alt_header.pack(fill='x')
            alt_header.pack_propagate(False)
            
            tk.Label(
                alt_header,
                text="🔍 Diagnósticos Alternativos",
                font=('Segoe UI', 11, 'bold'),
                bg=self.colors['warning'],
                fg='white'
            ).pack(side='left', padx=15, pady=8)
            
            # Contenido
            alt_content = tk.Frame(alt_card, bg='white')
            alt_content.pack(fill='both', expand=True, padx=20, pady=15)
            
            for idx, diag in enumerate(diagnosticos[1:4], 1):  # Mostrar hasta 3 alternativos
                diag_item = tk.Frame(alt_content, bg=self.colors['light'], relief='flat')
                diag_item.pack(fill='x', pady=5, padx=5)
                
                item_content = tk.Frame(diag_item, bg=self.colors['light'])
                item_content.pack(fill='x', padx=10, pady=10)
                
                # Nombre
                tk.Label(
                    item_content,
                    text=f"{idx}. {diag['nombre']}",
                    font=('Segoe UI', 10, 'bold'),
                    bg=self.colors['light'],
                    fg=self.colors['dark']
                ).pack(anchor='w')
                
                # Confianza
                tk.Label(
                    item_content,
                    text=f"📊 Confianza: {diag['confianza_porcentaje']}%",
                    font=('Segoe UI', 9),
                    bg=self.colors['light'],
                    fg='#666'
                ).pack(anchor='w', pady=(3, 0))
        
        # === ADVERTENCIA MÉDICA ===
        warning_card = tk.Frame(container, bg='#FFF3CD', relief='solid', bd=1, highlightbackground='#FFC107')
        warning_card.pack(fill='x', pady=(10, 0))
        
        warning_content = tk.Frame(warning_card, bg='#FFF3CD')
        warning_content.pack(fill='both', padx=15, pady=12)
        
        tk.Label(
            warning_content,
            text="⚠️ ADVERTENCIA IMPORTANTE",
            font=('Segoe UI', 10, 'bold'),
            bg='#FFF3CD',
            fg='#856404'
        ).pack(anchor='w', pady=(0, 5))
        
        warning_text = ("Este sistema es únicamente una herramienta de orientación preliminar "
                       "y NO reemplaza el diagnóstico profesional.\n\n"
                       "Siempre consulte con un odontólogo certificado para un diagnóstico "
                       "definitivo y tratamiento adecuado.")
        
        tk.Label(
            warning_content,
            text=warning_text,
            font=('Segoe UI', 9),
            bg='#FFF3CD',
            fg='#856404',
            justify='left',
            wraplength=500
        ).pack(anchor='w')
    
    def display_no_diagnosis(self):
        """Muestra mensaje cuando no se encontró diagnóstico - MEJORADO"""
        # Ya no debería llamarse porque siempre generamos un diagnóstico
        # Pero lo dejamos por compatibilidad
        
        container = tk.Frame(self.scrollable_frame, bg='white')
        container.pack(fill='both', expand=True, pady=50)
        
        icon_label = tk.Label(
            container,
            text="🔍",
            font=('Segoe UI', 56),
            bg='white',
            fg=self.colors['primary']
        )
        icon_label.pack(pady=(20, 10))
        
        text_label = tk.Label(
            container,
            text="No se encontraron coincidencias específicas",
            font=('Segoe UI', 14, 'bold'),
            bg='white',
            fg=self.colors['dark']
        )
        text_label.pack(pady=10)
        
        suggestion_label = tk.Label(
            container,
            text="Se recomienda una evaluación profesional preventiva.\nConsulte a un odontólogo para mayor seguridad.",
            font=('Segoe UI', 10),
            bg='white',
            fg='gray',
            wraplength=500,
            justify='center'
        )
        suggestion_label.pack()
    
    def get_summary(self, diagnosis_result):
        """Genera un resumen del diagnóstico"""
        principal = diagnosis_result.get('principal')
        if not principal:
            return {}
        
        # Determinar urgencia
        urgencia = principal.get('urgencia', 'baja')
        
        urgencia_msg = {
            'urgente': '🚨 ATENCIÓN URGENTE REQUERIDA',
            'alta': '⚠️ Consulte a un odontólogo pronto',
            'moderada': '📅 Agende una cita odontológica',
            'baja': 'ℹ️ Considere una evaluación odontológica'
        }
        
        return {
            'diagnostico_principal': principal['nombre'],
            'confianza': principal['confianza_porcentaje'],
            'urgencia': urgencia,
            'mensaje_urgencia': urgencia_msg.get(urgencia, ''),
            'num_alternativos': diagnosis_result.get('num_diagnosticos', 1) - 1
        }
    
    def clear(self):
        """Limpia el panel de resultados"""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        self.initial_message = ttk.Label(
            self.scrollable_frame,
            text="Ingrese los síntomas y presione 'Diagnosticar' para obtener resultados.",
            font=('Arial', 11),
            foreground='gray'
        )
        self.initial_message.pack(pady=50)
        
        self.results = None
