"""
Ventana Principal de la Aplicación
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import os
import sys

# Añadir el directorio padre al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.gui.symptoms_panel import SymptomsPanel
from src.gui.results_panel import ResultsPanel
from src.inference_engine import DiagnosisEngine
from src.utils.logger import Logger
from src.utils.report_generator import ReportGenerator
from src.database.db_manager import DatabaseManager


class MainWindow:
    """Ventana principal del sistema experto"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto de Odontología")
        self.root.geometry("1200x800")
        
        # Centrar ventana
        self.center_window()
        
        # Inicializar componentes
        self.diagnosis_engine = DiagnosisEngine()
        self.logger = Logger()
        self.report_generator = ReportGenerator()
        self.db_manager = DatabaseManager()  # Inicializar gestor de BD
        
        # Variables
        self.current_diagnosis = None
        self.current_symptoms = None
        self.patient_name = tk.StringVar(value="")
        self.patient_age = tk.StringVar(value="")
        self.patient_phone = tk.StringVar(value="")
        self.patient_email = tk.StringVar(value="")
        
        # Configurar estilo
        self.setup_style()
        
        # Crear widgets
        self.create_menu()
        self.create_widgets()
        
        # Log de inicio
        self.logger.log("Sistema iniciado")
        self.logger.log(f"Base de datos inicializada: {self.db_manager.db_path}")

    
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_style(self):
        """Configura el estilo de la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores del tema
        self.colors = {
            'primary': '#2E86AB',      # Azul profesional
            'secondary': '#A23B72',    # Morado/Rosa
            'success': '#06A77D',      # Verde
            'warning': '#F18F01',      # Naranja
            'danger': '#C73E1D',       # Rojo
            'light': '#F4F4F9',        # Gris claro
            'dark': '#2B2D42',         # Azul oscuro
            'white': '#FFFFFF',
            'border': '#DEE2E6'        # Gris para bordes
        }
        
        # Configurar colores
        style.configure('Title.TLabel', font=('Segoe UI', 16, 'bold'), 
                       foreground=self.colors['dark'])
        style.configure('Subtitle.TLabel', font=('Segoe UI', 11), 
                       foreground=self.colors['dark'])
        style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'),
                       foreground=self.colors['primary'])
        
        # Botones
        style.configure('Primary.TButton', font=('Segoe UI', 10, 'bold'),
                       background=self.colors['primary'], foreground='white')
        style.configure('Success.TButton', font=('Segoe UI', 10),
                       background=self.colors['success'])
        style.configure('Danger.TButton', font=('Segoe UI', 10),
                       background=self.colors['danger'])
        
        # Frames
        style.configure('Card.TFrame', background=self.colors['white'], 
                       relief='flat', borderwidth=1)
        style.configure('Header.TFrame', background=self.colors['primary'])
    
    def create_menu(self):
        """Crea la barra de menú"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Nuevo Diagnóstico", command=self.new_diagnosis)
        file_menu.add_command(label="Guardar Reporte PDF", command=self.save_pdf_report)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit_app)
        
        # Menú Edición
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edición", menu=edit_menu)
        edit_menu.add_command(label="Limpiar Formulario", command=self.clear_form)
        
        # Menú Base de Datos (NUEVO)
        db_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Base de Datos", menu=db_menu)
        db_menu.add_command(label="Ver Historial del Paciente", command=self.show_patient_history)
        db_menu.add_command(label="Buscar Pacientes", command=self.search_patients)
        db_menu.add_command(label="Estadísticas", command=self.show_statistics)
        db_menu.add_separator()
        db_menu.add_command(label="Exportar Datos a CSV", command=self.export_to_csv)
        
        # Menú Ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        help_menu.add_command(label="Manual de Usuario", command=self.show_manual)
    
    def create_widgets(self):
        """Crea los widgets principales"""
        
        # Configurar color de fondo
        self.root.configure(bg=self.colors['light'])
        
        # Frame superior (header) con estilo mejorado
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # Contenedor interno del header
        header_content = tk.Frame(header_frame, bg=self.colors['primary'])
        header_content.pack(expand=True, fill='both', padx=20)
        
        # Título con icono
        title = tk.Label(
            header_content,
            text="🦷 Sistema Experto de Odontología",
            font=('Segoe UI', 20, 'bold'),
            bg=self.colors['primary'],
            fg='white'
        )
        title.pack(side='left', pady=10)
        
        # Información del paciente con diseño mejorado
        patient_frame = tk.Frame(header_content, bg=self.colors['primary'])
        patient_frame.pack(side='right', pady=10)
        
        # Fila 1: Nombre y Edad
        row1 = tk.Frame(patient_frame, bg=self.colors['primary'])
        row1.pack(fill='x', pady=2)
        
        tk.Label(
            row1,
            text="👤 Nombre:",
            font=('Segoe UI', 9),
            bg=self.colors['primary'],
            fg='white'
        ).pack(side='left', padx=5)
        
        patient_entry = tk.Entry(
            row1,
            textvariable=self.patient_name,
            width=20,
            font=('Segoe UI', 9),
            relief='flat',
            bd=2
        )
        patient_entry.pack(side='left', ipady=3)
        
        tk.Label(
            row1,
            text="📅 Edad:",
            font=('Segoe UI', 9),
            bg=self.colors['primary'],
            fg='white'
        ).pack(side='left', padx=(10, 5))
        
        self.patient_age = tk.StringVar()
        age_entry = tk.Entry(
            row1,
            textvariable=self.patient_age,
            width=5,
            font=('Segoe UI', 9),
            relief='flat',
            bd=2
        )
        age_entry.pack(side='left', ipady=3)
        
        # Fila 2: Teléfono y Email
        row2 = tk.Frame(patient_frame, bg=self.colors['primary'])
        row2.pack(fill='x', pady=2)
        
        tk.Label(
            row2,
            text="📞 Tel:",
            font=('Segoe UI', 9),
            bg=self.colors['primary'],
            fg='white'
        ).pack(side='left', padx=5)
        
        self.patient_phone = tk.StringVar()
        phone_entry = tk.Entry(
            row2,
            textvariable=self.patient_phone,
            width=12,
            font=('Segoe UI', 9),
            relief='flat',
            bd=2
        )
        phone_entry.pack(side='left', ipady=3)
        
        tk.Label(
            row2,
            text="📧 Email:",
            font=('Segoe UI', 9),
            bg=self.colors['primary'],
            fg='white'
        ).pack(side='left', padx=(10, 5))
        
        self.patient_email = tk.StringVar()
        email_entry = tk.Entry(
            row2,
            textvariable=self.patient_email,
            width=20,
            font=('Segoe UI', 9),
            relief='flat',
            bd=2
        )
        email_entry.pack(side='left', ipady=3)
        
        # Frame principal con PanedWindow
        main_container = tk.Frame(self.root, bg=self.colors['light'])
        main_container.pack(fill='both', expand=True, padx=15, pady=15)
        
        paned_window = ttk.PanedWindow(main_container, orient='horizontal')
        paned_window.pack(fill='both', expand=True)
        
        # Panel izquierdo: Síntomas (con scroll y card)
        left_card = tk.Frame(paned_window, bg='white', relief='solid', bd=1)
        paned_window.add(left_card, weight=1)
        
        # Canvas para scroll
        canvas = tk.Canvas(left_card, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(left_card, orient='vertical', command=canvas.yview)
        
        self.symptoms_panel = SymptomsPanel(canvas)
        
        canvas.create_window((0, 0), window=self.symptoms_panel, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        self.symptoms_panel.bind("<Configure>", on_frame_configure)
        
        # Hacer scroll con la rueda del mouse
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", on_mousewheel)
        
        canvas.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y', pady=5)
        
        # Panel derecho: Resultados (con card)
        right_card = tk.Frame(paned_window, bg='white', relief='solid', bd=1)
        paned_window.add(right_card, weight=1)
        
        self.results_panel = ResultsPanel(right_card)
        self.results_panel.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Frame inferior (botones de acción) con diseño mejorado
        bottom_frame = tk.Frame(self.root, bg=self.colors['light'], height=80)
        bottom_frame.pack(fill='x', side='bottom')
        bottom_frame.pack_propagate(False)
        
        # Botones con estilos mejorados
        btn_frame = tk.Frame(bottom_frame, bg=self.colors['light'])
        btn_frame.pack(pady=15)
        
        # Botón Diagnosticar (principal)
        self.diagnose_btn = tk.Button(
            btn_frame,
            text="🔍 Diagnosticar",
            command=self.perform_diagnosis,
            font=('Segoe UI', 11, 'bold'),
            bg=self.colors['primary'],
            fg='white',
            activebackground=self.colors['secondary'],
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            bd=0,
            padx=30,
            pady=12
        )
        self.diagnose_btn.pack(side='left', padx=5)
        
        # Botón Limpiar
        clear_btn = tk.Button(
            btn_frame,
            text="🗑️ Limpiar",
            command=self.clear_form,
            font=('Segoe UI', 10),
            bg='white',
            fg=self.colors['dark'],
            activebackground=self.colors['light'],
            cursor='hand2',
            relief='solid',
            bd=1,
            padx=20,
            pady=10
        )
        clear_btn.pack(side='left', padx=5)
        
        # Botón Guardar PDF
        save_btn = tk.Button(
            btn_frame,
            text="📄 Guardar PDF",
            command=self.save_pdf_report,
            font=('Segoe UI', 10),
            bg=self.colors['success'],
            fg='white',
            activebackground='#058a68',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            bd=0,
            padx=20,
            pady=10
        )
        save_btn.pack(side='left', padx=5)
        
        # Botón Historial Clínico (NUEVO)
        history_btn = tk.Button(
            btn_frame,
            text="📋 Historial Clínico",
            command=self.show_clinical_history,
            font=('Segoe UI', 10),
            bg=self.colors['primary'],
            fg='white',
            activebackground=self.colors['secondary'],
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            bd=0,
            padx=20,
            pady=10
        )
        history_btn.pack(side='left', padx=5)
        
        # Variable para barra de estado
        self.status_var = tk.StringVar(value="� Ingrese los síntomas del paciente y presione Diagnosticar")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            bg=self.colors['dark'],
            fg='white',
            font=('Segoe UI', 9),
            anchor='w',
            padx=10,
            pady=5
        )
        status_bar.pack(fill='x', side='bottom')
    
    def perform_diagnosis(self):
        """Realiza el diagnóstico basado en los síntomas"""
        try:
            self.status_var.set("Procesando diagnóstico...")
            self.root.update()
            
            # Obtener síntomas
            symptoms = self.symptoms_panel.get_symptoms()
            
            # Validar síntomas
            validation = self.diagnosis_engine.validate_symptoms(symptoms)
            if not validation['valido']:
                warnings_msg = "\n".join(validation['advertencias'])
                messagebox.showwarning(
                    "Advertencias de Validación",
                    f"Se encontraron las siguientes advertencias:\n\n{warnings_msg}\n\n¿Desea continuar?"
                )
            
            # Realizar diagnóstico
            self.current_diagnosis = self.diagnosis_engine.diagnose(
                symptoms,
                use_fuzzy=True,
                strategy='combine'
            )
            
            # Guardar síntomas para la BD
            self.current_symptoms = symptoms
            
            # Log del diagnóstico
            patient = self.patient_name.get()
            if self.current_diagnosis['num_diagnosticos'] > 0:
                principal = self.current_diagnosis['principal']
                self.logger.log(
                    f"Diagnóstico realizado para {patient}: {principal['nombre']} "
                    f"(Confianza: {principal['confianza_porcentaje']}%)"
                )
                
                # Guardar en base de datos
                try:
                    # Obtener información del paciente
                    patient = self.patient_name.get()
                    edad = self.patient_age.get()
                    telefono = self.patient_phone.get()
                    email = self.patient_email.get()
                    
                    # Convertir edad a entero si está presente
                    edad_int = None
                    if edad and edad.strip().isdigit():
                        edad_int = int(edad)
                    
                    # Guardar paciente con toda la información
                    paciente_id = self.db_manager.guardar_paciente(
                        nombre=patient,
                        edad=edad_int,
                        telefono=telefono if telefono else None,
                        email=email if email else None,
                        notas=None
                    )
                    
                    # Guardar diagnóstico
                    diagnostico_id = self.db_manager.guardar_diagnostico(
                        patient,
                        self.current_diagnosis,
                        symptoms
                    )
                    self.logger.log(f"Diagnóstico guardado en BD con ID: {diagnostico_id}")
                    self.status_var.set(f"✓ Diagnóstico completado y guardado (ID: {diagnostico_id})")
                except Exception as db_error:
                    self.logger.log(f"Error guardando en BD: {str(db_error)}", level='ERROR')
                    self.status_var.set("⚠ Diagnóstico completado (error al guardar en BD)")
            else:
                self.logger.log(f"No se encontró diagnóstico para {patient}")
                self.status_var.set("Diagnóstico completado")
            
            # Mostrar resultados
            self.results_panel.display_results(self.current_diagnosis)
            
            
        except Exception as e:
            self.logger.log(f"Error en diagnóstico: {str(e)}", level='ERROR')
            messagebox.showerror(
                "Error",
                f"Ocurrió un error al realizar el diagnóstico:\n{str(e)}"
            )
            self.status_var.set("Error en el diagnóstico")
    
    def clear_form(self):
        """Limpia el formulario de síntomas y resultados"""
        response = messagebox.askyesno(
            "Confirmar",
            "¿Está seguro de que desea limpiar el formulario?"
        )
        if response:
            self.symptoms_panel.reset()
            self.results_panel.clear()
            self.current_diagnosis = None
            # Limpiar campos del paciente
            self.patient_name.set("")
            self.patient_age.set("")
            self.patient_phone.set("")
            self.patient_email.set("")
            self.status_var.set("Formulario limpiado")
            self.logger.log("Formulario limpiado")
    
    def new_diagnosis(self):
        """Inicia un nuevo diagnóstico"""
        self.clear_form()
        self.patient_name.set("Paciente")
    
    def save_pdf_report(self):
        """Guarda un reporte PDF del diagnóstico"""
        if not self.current_diagnosis or self.current_diagnosis['num_diagnosticos'] == 0:
            messagebox.showwarning(
                "Sin Diagnóstico",
                "No hay un diagnóstico para exportar a PDF."
            )
            return
        
        try:
            # Solicitar ubicación de guardado
            filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
                initialfile=f"diagnostico_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            )
            
            if filename:
                self.status_var.set("Generando reporte PDF...")
                self.root.update()
                
                # Obtener síntomas
                symptoms = self.symptoms_panel.get_symptoms()
                
                # Recopilar información del paciente
                patient_info = {
                    'edad': self.patient_age.get() if self.patient_age.get() else None,
                    'telefono': self.patient_phone.get() if self.patient_phone.get() else None,
                    'email': self.patient_email.get() if self.patient_email.get() else None
                }
                
                # Generar reporte
                self.report_generator.generate_report(
                    patient_name=self.patient_name.get(),
                    symptoms=symptoms,
                    diagnosis=self.current_diagnosis,
                    output_path=filename,
                    patient_info=patient_info
                )
                
                self.status_var.set(f"Reporte guardado: {os.path.basename(filename)}")
                self.logger.log(f"Reporte PDF generado: {filename}")
                
                messagebox.showinfo(
                    "Éxito",
                    f"Reporte guardado exitosamente en:\n{filename}"
                )
        
        except Exception as e:
            self.logger.log(f"Error al generar PDF: {str(e)}", level='ERROR')
            messagebox.showerror(
                "Error",
                f"Error al generar el reporte PDF:\n{str(e)}"
            )
            self.status_var.set("Error al generar PDF")
    
    def show_about(self):
        """Muestra información sobre la aplicación"""
        about_text = """
        Sistema Experto de Odontología
        Versión 1.0
        
        Desarrollado para la Universidad
        Curso de Sistemas Expertos
        
        Este sistema utiliza reglas crisp y lógica difusa
        para identificar posibles causas de dolor dental.
        
        ⚠️ IMPORTANTE:
        Este sistema es solo para orientación preliminar.
        NO reemplaza la consulta con un odontólogo profesional.
        
        © 2025 - Proyecto Educativo
        """
        
        messagebox.showinfo("Acerca de", about_text)
    
    def show_manual(self):
        """Muestra el manual de usuario"""
        manual_text = """
        MANUAL DE USUARIO
        
        1. INGRESO DE SÍNTOMAS:
           - Complete los campos en el panel izquierdo
           - Use las escalas para intensidad (0-10)
           - Seleccione opciones en los menús desplegables
        
        2. DIAGNÓSTICO:
           - Presione el botón "Diagnosticar"
           - Revise los resultados en el panel derecho
           - El sistema muestra el diagnóstico principal y alternativas
        
        3. RECOMENDACIONES:
           - Lea cuidadosamente las recomendaciones
           - Preste atención al nivel de urgencia
           - Siga las indicaciones para atención profesional
        
        4. GENERAR REPORTE:
           - Use el botón "Guardar PDF" para exportar
           - El reporte incluye todos los detalles del diagnóstico
        
        5. NUEVO DIAGNÓSTICO:
           - Use "Limpiar" para resetear el formulario
           - Ingrese un nuevo nombre de paciente si es necesario
        
        Para más información, contacte al desarrollador.
        """
        
        # Crear ventana de diálogo personalizada
        manual_window = tk.Toplevel(self.root)
        manual_window.title("Manual de Usuario")
        manual_window.geometry("600x500")
        
        text_widget = tk.Text(manual_window, wrap='word', padx=20, pady=20)
        text_widget.pack(fill='both', expand=True)
        text_widget.insert('1.0', manual_text)
        text_widget.config(state='disabled')
        
        close_btn = ttk.Button(
            manual_window,
            text="Cerrar",
            command=manual_window.destroy
        )
        close_btn.pack(pady=10)
    
    def quit_app(self):
        """Cierra la aplicación"""
        response = messagebox.askyesno(
            "Salir",
            "¿Está seguro de que desea salir?"
        )
        if response:
            self.logger.log("Sistema cerrado")
            self.root.quit()
    
    # ==================== HISTORIAL CLÍNICO ====================
    
    def show_clinical_history(self):
        """Muestra ventana completa de Historial Clínico"""
        # Crear ventana principal
        history_window = tk.Toplevel(self.root)
        history_window.title("📋 Historial Clínico Completo")
        history_window.geometry("1000x700")
        history_window.configure(bg=self.colors['light'])
        
        # Frame principal
        main_container = tk.Frame(history_window, bg=self.colors['light'])
        main_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === HEADER ===
        header = tk.Frame(main_container, bg=self.colors['primary'], height=60)
        header.pack(fill='x', pady=(0, 10))
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="📋 HISTORIAL CLÍNICO COMPLETO",
            font=('Segoe UI', 16, 'bold'),
            bg=self.colors['primary'],
            fg='white'
        ).pack(pady=15)
        
        # === PANEL DE BÚSQUEDA ===
        search_frame = tk.Frame(main_container, bg='white', relief='solid', bd=1)
        search_frame.pack(fill='x', pady=(0, 10), padx=5)
        
        search_content = tk.Frame(search_frame, bg='white')
        search_content.pack(fill='x', padx=15, pady=10)
        
        tk.Label(
            search_content,
            text="🔍 Buscar Paciente:",
            font=('Segoe UI', 10, 'bold'),
            bg='white'
        ).pack(side='left', padx=(0, 10))
        
        search_var = tk.StringVar()
        search_entry = tk.Entry(
            search_content,
            textvariable=search_var,
            font=('Segoe UI', 10),
            width=30,
            relief='solid',
            bd=1
        )
        search_entry.pack(side='left', padx=5, ipady=5)
        
        # === CONTENEDOR CON PESTAÑAS ===
        notebook = ttk.Notebook(main_container)
        notebook.pack(fill='both', expand=True, pady=(0, 10))
        
        # Pestaña 1: Todos los Pacientes
        all_patients_frame = tk.Frame(notebook, bg='white')
        notebook.add(all_patients_frame, text='👥 Todos los Pacientes')
        
        # Pestaña 2: Diagnósticos Recientes
        recent_diag_frame = tk.Frame(notebook, bg='white')
        notebook.add(recent_diag_frame, text='🕒 Diagnósticos Recientes')
        
        # Pestaña 3: Estadísticas
        stats_frame = tk.Frame(notebook, bg='white')
        notebook.add(stats_frame, text='📊 Estadísticas')
        
        # === PESTAÑA 1: TODOS LOS PACIENTES ===
        self._create_all_patients_tab(all_patients_frame, search_var, search_entry)
        
        # === PESTAÑA 2: DIAGNÓSTICOS RECIENTES ===
        self._create_recent_diagnostics_tab(recent_diag_frame)
        
        # === PESTAÑA 3: ESTADÍSTICAS ===
        self._create_statistics_tab(stats_frame)
        
        # === BOTONES INFERIORES ===
        bottom_frame = tk.Frame(main_container, bg=self.colors['light'])
        bottom_frame.pack(fill='x', pady=(10, 0))
        
        tk.Button(
            bottom_frame,
            text="🔄 Actualizar",
            command=lambda: self._refresh_history(all_patients_frame, recent_diag_frame, stats_frame, search_var, search_entry),
            font=('Segoe UI', 10),
            bg=self.colors['primary'],
            fg='white',
            cursor='hand2',
            relief='flat',
            padx=20,
            pady=8
        ).pack(side='left', padx=5)
        
        tk.Button(
            bottom_frame,
            text="📥 Exportar Todo a CSV",
            command=self.export_to_csv,
            font=('Segoe UI', 10),
            bg=self.colors['success'],
            fg='white',
            cursor='hand2',
            relief='flat',
            padx=20,
            pady=8
        ).pack(side='left', padx=5)
        
        tk.Button(
            bottom_frame,
            text="❌ Cerrar",
            command=history_window.destroy,
            font=('Segoe UI', 10),
            bg='#6c757d',
            fg='white',
            cursor='hand2',
            relief='flat',
            padx=20,
            pady=8
        ).pack(side='right', padx=5)
    
    def _create_all_patients_tab(self, parent, search_var, search_entry):
        """Crea la pestaña de todos los pacientes"""
        # Frame con scroll
        canvas = tk.Canvas(parent, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        scrollbar.pack(side='right', fill='y')
        
        # Función de búsqueda
        def do_search():
            termino = search_var.get()
            # Limpiar frame
            for widget in scrollable_frame.winfo_children():
                widget.destroy()
            
            if termino:
                pacientes = self.db_manager.buscar_pacientes(termino)
            else:
                # Obtener todos los pacientes
                self.db_manager.connect()
                self.db_manager.cursor.execute("""
                    SELECT p.*, COUNT(d.id) as num_diagnosticos
                    FROM pacientes p
                    LEFT JOIN diagnosticos d ON p.id = d.paciente_id
                    GROUP BY p.id
                    ORDER BY p.fecha_registro DESC
                """)
                pacientes = [dict(row) for row in self.db_manager.cursor.fetchall()]
                self.db_manager.disconnect()
            
            if not pacientes:
                tk.Label(
                    scrollable_frame,
                    text="No se encontraron pacientes",
                    font=('Segoe UI', 12),
                    bg='white',
                    fg='gray'
                ).pack(pady=50)
                return
            
            # Mostrar pacientes
            for pac in pacientes:
                self._create_patient_card(scrollable_frame, pac)
        
        # Bind búsqueda
        search_entry.bind('<Return>', lambda e: do_search())
        
        # Cargar todos inicialmente
        do_search()
    
    def _create_patient_card(self, parent, paciente):
        """Crea una tarjeta visual para un paciente"""
        card = tk.Frame(parent, bg='white', relief='solid', bd=1, highlightbackground=self.colors['border'])
        card.pack(fill='x', padx=10, pady=5)
        
        content = tk.Frame(card, bg='white')
        content.pack(fill='both', expand=True, padx=15, pady=12)
        
        # Fila superior: Nombre y botones
        top_row = tk.Frame(content, bg='white')
        top_row.pack(fill='x')
        
        # Nombre
        tk.Label(
            top_row,
            text=f"👤 {paciente['nombre']}",
            font=('Segoe UI', 12, 'bold'),
            bg='white',
            fg=self.colors['dark']
        ).pack(side='left')
        
        # Badge de diagnósticos
        num_diag = paciente.get('num_diagnosticos', 0)
        badge_color = self.colors['primary'] if num_diag > 0 else '#6c757d'
        tk.Label(
            top_row,
            text=f"{num_diag} diagnóstico{'s' if num_diag != 1 else ''}",
            font=('Segoe UI', 9, 'bold'),
            bg=badge_color,
            fg='white',
            padx=8,
            pady=3
        ).pack(side='left', padx=10)
        
        # Botones
        btn_frame = tk.Frame(top_row, bg='white')
        btn_frame.pack(side='right')
        
        tk.Button(
            btn_frame,
            text="📋 Ver Historial",
            command=lambda: self._show_patient_full_history(paciente['nombre']),
            font=('Segoe UI', 9),
            bg=self.colors['primary'],
            fg='white',
            cursor='hand2',
            relief='flat',
            padx=10,
            pady=5
        ).pack(side='left', padx=3)
        
        # Fila inferior: Detalles
        details = tk.Frame(content, bg='white')
        details.pack(fill='x', pady=(8, 0))
        
        # Edad
        if paciente.get('edad'):
            tk.Label(
                details,
                text=f"📅 {paciente['edad']} años",
                font=('Segoe UI', 9),
                bg='white',
                fg='#666'
            ).pack(side='left', padx=(0, 15))
        
        # Teléfono
        if paciente.get('telefono'):
            tk.Label(
                details,
                text=f"📞 {paciente['telefono']}",
                font=('Segoe UI', 9),
                bg='white',
                fg='#666'
            ).pack(side='left', padx=(0, 15))
        
        # Email
        if paciente.get('email'):
            tk.Label(
                details,
                text=f"📧 {paciente['email']}",
                font=('Segoe UI', 9),
                bg='white',
                fg='#666'
            ).pack(side='left', padx=(0, 15))
        
        # Fecha de registro
        tk.Label(
            details,
            text=f"🕒 Registro: {paciente['fecha_registro']}",
            font=('Segoe UI', 9),
            bg='white',
            fg='#999'
        ).pack(side='right')
    
    def _show_patient_full_history(self, patient_name):
        """Muestra el historial completo de un paciente en ventana dedicada"""
        # Obtener historial
        historial = self.db_manager.obtener_historial_paciente(patient_name)
        
        if not historial:
            messagebox.showinfo(
                "Historial",
                f"No se encontraron diagnósticos para {patient_name}"
            )
            return
        
        # Crear ventana
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"Historial de {patient_name}")
        detail_window.geometry("900x650")
        detail_window.configure(bg='white')
        
        # Header
        header = tk.Frame(detail_window, bg=self.colors['primary'], height=60)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text=f"📋 Historial Clínico de {patient_name}",
            font=('Segoe UI', 14, 'bold'),
            bg=self.colors['primary'],
            fg='white'
        ).pack(pady=15)
        
        # Contenido con scroll
        canvas = tk.Canvas(detail_window, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(detail_window, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        scrollbar.pack(side='right', fill='y')
        
        # Mostrar cada diagnóstico
        for idx, diag in enumerate(historial, 1):
            self._create_diagnosis_card(scrollable_frame, diag, idx)
        
        # Botón cerrar
        tk.Button(
            detail_window,
            text="Cerrar",
            command=detail_window.destroy,
            font=('Segoe UI', 10),
            bg=self.colors['primary'],
            fg='white',
            cursor='hand2',
            relief='flat',
            padx=30,
            pady=10
        ).pack(pady=10)
    
    def _create_diagnosis_card(self, parent, diag, number):
        """Crea tarjeta para mostrar un diagnóstico"""
        card = tk.Frame(parent, bg='white', relief='solid', bd=2, highlightbackground=self.colors['border'])
        card.pack(fill='x', padx=15, pady=10)
        
        content = tk.Frame(card, bg='white')
        content.pack(fill='both', expand=True, padx=15, pady=12)
        
        # Número y fecha
        top = tk.Frame(content, bg='white')
        top.pack(fill='x', pady=(0, 10))
        
        tk.Label(
            top,
            text=f"#{number}",
            font=('Segoe UI', 14, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(side='left')
        
        tk.Label(
            top,
            text=diag['fecha'],
            font=('Segoe UI', 10),
            bg='white',
            fg='#666'
        ).pack(side='right')
        
        # Diagnóstico
        tk.Label(
            content,
            text=diag['diagnostico'],
            font=('Segoe UI', 12, 'bold'),
            bg='white',
            fg=self.colors['dark']
        ).pack(anchor='w', pady=(0, 5))
        
        # Descripción
        tk.Label(
            content,
            text=diag['descripcion'],
            font=('Segoe UI', 10),
            bg='white',
            fg='#666',
            wraplength=800,
            justify='left'
        ).pack(anchor='w', pady=(0, 10))
        
        # Info badges
        badges = tk.Frame(content, bg='white')
        badges.pack(fill='x')
        
        # Confianza
        conf_color = self.colors['success'] if diag['confianza'] >= 0.7 else self.colors['warning']
        tk.Label(
            badges,
            text=f"📊 Confianza: {diag['confianza']*100:.1f}%",
            font=('Segoe UI', 9),
            bg=conf_color,
            fg='white',
            padx=8,
            pady=4
        ).pack(side='left', padx=(0, 5))
        
        # Urgencia
        urgencia_colors = {
            'urgente': self.colors['danger'],
            'alta': self.colors['warning'],
            'moderada': self.colors['primary'],
            'baja': self.colors['success']
        }
        tk.Label(
            badges,
            text=f"⏰ {diag['urgencia'].upper()}",
            font=('Segoe UI', 9),
            bg=urgencia_colors.get(diag['urgencia'], '#6c757d'),
            fg='white',
            padx=8,
            pady=4
        ).pack(side='left', padx=(0, 5))
        
        # Gravedad
        tk.Label(
            badges,
            text=f"⚖️ {diag['gravedad'].upper()}",
            font=('Segoe UI', 9),
            bg='#6c757d',
            fg='white',
            padx=8,
            pady=4
        ).pack(side='left')
        
        # Botón ver detalles
        tk.Button(
            badges,
            text="Ver Detalles Completos",
            command=lambda: self._show_full_diagnosis_details(diag['id']),
            font=('Segoe UI', 9),
            bg=self.colors['light'],
            fg=self.colors['dark'],
            cursor='hand2',
            relief='flat',
            padx=10,
            pady=4
        ).pack(side='right')
    
    def _show_full_diagnosis_details(self, diag_id):
        """Muestra todos los detalles de un diagnóstico incluyendo síntomas"""
        detalles = self.db_manager.obtener_diagnostico_detallado(diag_id)
        
        if not detalles:
            messagebox.showerror("Error", "No se pudieron cargar los detalles")
            return
        
        # Crear ventana
        detail_win = tk.Toplevel(self.root)
        detail_win.title(f"Detalles Diagnóstico #{diag_id}")
        detail_win.geometry("800x700")
        detail_win.configure(bg='white')
        
        # Canvas con scroll
        canvas = tk.Canvas(detail_win, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(detail_win, orient='vertical', command=canvas.yview)
        scrollable = tk.Frame(canvas, bg='white')
        
        scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side='left', fill='both', expand=True, padx=15, pady=15)
        scrollbar.pack(side='right', fill='y')
        
        # Contenido
        tk.Label(
            scrollable,
            text=f"Diagnóstico #{diag_id}",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(anchor='w', pady=(0, 5))
        
        tk.Label(
            scrollable,
            text=f"Paciente: {detalles['paciente_nombre']}",
            font=('Segoe UI', 12),
            bg='white'
        ).pack(anchor='w')
        
        tk.Label(
            scrollable,
            text=f"Fecha: {detalles['fecha_diagnostico']}",
            font=('Segoe UI', 10),
            bg='white',
            fg='#666'
        ).pack(anchor='w', pady=(0, 15))
        
        ttk.Separator(scrollable, orient='horizontal').pack(fill='x', pady=10)
        
        # Diagnóstico
        tk.Label(
            scrollable,
            text="🎯 Diagnóstico Principal",
            font=('Segoe UI', 12, 'bold'),
            bg='white'
        ).pack(anchor='w', pady=(0, 5))
        
        tk.Label(
            scrollable,
            text=detalles['diagnostico_principal'],
            font=('Segoe UI', 11),
            bg='white',
            fg=self.colors['dark']
        ).pack(anchor='w')
        
        tk.Label(
            scrollable,
            text=f"Confianza: {detalles['confianza_principal']*100:.1f}% | Gravedad: {detalles['gravedad']} | Urgencia: {detalles['urgencia']}",
            font=('Segoe UI', 10),
            bg='white',
            fg='#666'
        ).pack(anchor='w', pady=(5, 15))
        
        ttk.Separator(scrollable, orient='horizontal').pack(fill='x', pady=10)
        
        # Síntomas
        tk.Label(
            scrollable,
            text="🔬 Síntomas Evaluados",
            font=('Segoe UI', 12, 'bold'),
            bg='white'
        ).pack(anchor='w', pady=(0, 10))
        
        symptoms_frame = tk.Frame(scrollable, bg=self.colors['light'], relief='solid', bd=1)
        symptoms_frame.pack(fill='x', pady=(0, 15))
        
        symptoms_content = tk.Frame(symptoms_frame, bg=self.colors['light'])
        symptoms_content.pack(fill='both', padx=15, pady=10)
        
        for sintoma in detalles['sintomas']:
            s_row = tk.Frame(symptoms_content, bg=self.colors['light'])
            s_row.pack(fill='x', pady=2)
            
            tk.Label(
                s_row,
                text=f"• {sintoma['nombre_sintoma']}:",
                font=('Segoe UI', 9),
                bg=self.colors['light'],
                width=25,
                anchor='w'
            ).pack(side='left')
            
            tk.Label(
                s_row,
                text=sintoma['valor_sintoma'],
                font=('Segoe UI', 9, 'bold'),
                bg=self.colors['light'],
                fg=self.colors['primary']
            ).pack(side='left')
        
        ttk.Separator(scrollable, orient='horizontal').pack(fill='x', pady=10)
        
        # Recomendaciones
        tk.Label(
            scrollable,
            text="💊 Recomendaciones",
            font=('Segoe UI', 12, 'bold'),
            bg='white'
        ).pack(anchor='w', pady=(0, 10))
        
        for rec in detalles['recomendaciones']:
            rec_frame = tk.Frame(scrollable, bg='white')
            rec_frame.pack(fill='x', pady=3)
            
            tk.Label(
                rec_frame,
                text="✓",
                font=('Segoe UI', 11, 'bold'),
                bg='white',
                fg=self.colors['success']
            ).pack(side='left', padx=(0, 8))
            
            tk.Label(
                rec_frame,
                text=rec,
                font=('Segoe UI', 10),
                bg='white',
                wraplength=700,
                justify='left'
            ).pack(side='left', fill='x', expand=True)
        
        # Botón cerrar
        tk.Button(
            detail_win,
            text="Cerrar",
            command=detail_win.destroy,
            font=('Segoe UI', 10),
            bg=self.colors['primary'],
            fg='white',
            cursor='hand2',
            relief='flat',
            padx=30,
            pady=10
        ).pack(pady=15)
    
    def _create_recent_diagnostics_tab(self, parent):
        """Crea la pestaña de diagnósticos recientes"""
        # Canvas con scroll
        canvas = tk.Canvas(parent, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        scrollbar.pack(side='right', fill='y')
        
        # Obtener diagnósticos recientes
        self.db_manager.connect()
        self.db_manager.cursor.execute("""
            SELECT 
                d.id,
                p.nombre as paciente,
                d.fecha_diagnostico,
                d.diagnostico_principal,
                d.confianza_principal,
                d.urgencia,
                d.gravedad
            FROM diagnosticos d
            JOIN pacientes p ON d.paciente_id = p.id
            ORDER BY d.fecha_diagnostico DESC
            LIMIT 50
        """)
        diagnosticos = [dict(row) for row in self.db_manager.cursor.fetchall()]
        self.db_manager.disconnect()
        
        if not diagnosticos:
            tk.Label(
                scrollable_frame,
                text="No hay diagnósticos registrados",
                font=('Segoe UI', 12),
                bg='white',
                fg='gray'
            ).pack(pady=50)
            return
        
        # Mostrar diagnósticos
        for idx, diag in enumerate(diagnosticos, 1):
            diag_copy = {
                'id': diag['id'],
                'fecha': diag['fecha_diagnostico'],
                'diagnostico': diag['diagnostico_principal'],
                'descripcion': '',
                'confianza': diag['confianza_principal'],
                'urgencia': diag['urgencia'],
                'gravedad': diag['gravedad']
            }
            self._create_diagnosis_card(scrollable_frame, diag_copy, idx)
    
    def _create_statistics_tab(self, parent):
        """Crea la pestaña de estadísticas"""
        stats = self.db_manager.obtener_estadisticas()
        
        # Contenedor principal
        container = tk.Frame(parent, bg='white')
        container.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Título
        tk.Label(
            container,
            text="📊 Estadísticas del Sistema",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['dark']
        ).pack(anchor='w', pady=(0, 20))
        
        # Cards de resumen
        summary_frame = tk.Frame(container, bg='white')
        summary_frame.pack(fill='x', pady=(0, 30))
        
        # Total Pacientes
        self._create_stat_card(
            summary_frame,
            "👥",
            stats['total_pacientes'],
            "Pacientes Registrados",
            self.colors['primary']
        ).pack(side='left', padx=5, fill='x', expand=True)
        
        # Total Diagnósticos
        self._create_stat_card(
            summary_frame,
            "🩺",
            stats['total_diagnosticos'],
            "Diagnósticos Realizados",
            self.colors['success']
        ).pack(side='left', padx=5, fill='x', expand=True)
        
        # Diagnósticos más comunes
        tk.Label(
            container,
            text="🔝 Diagnósticos Más Comunes",
            font=('Segoe UI', 13, 'bold'),
            bg='white',
            fg=self.colors['dark']
        ).pack(anchor='w', pady=(0, 10))
        
        for idx, diag in enumerate(stats['diagnosticos_comunes'], 1):
            diag_row = tk.Frame(container, bg=self.colors['light'], relief='solid', bd=1)
            diag_row.pack(fill='x', pady=3)
            
            content = tk.Frame(diag_row, bg=self.colors['light'])
            content.pack(fill='x', padx=15, pady=10)
            
            tk.Label(
                content,
                text=f"{idx}.",
                font=('Segoe UI', 11, 'bold'),
                bg=self.colors['light'],
                width=3
            ).pack(side='left')
            
            tk.Label(
                content,
                text=diag['diagnostico'],
                font=('Segoe UI', 11),
                bg=self.colors['light'],
                anchor='w'
            ).pack(side='left', fill='x', expand=True)
            
            tk.Label(
                content,
                text=f"{diag['cantidad']} casos",
                font=('Segoe UI', 11, 'bold'),
                bg=self.colors['primary'],
                fg='white',
                padx=15,
                pady=3
            ).pack(side='right')
        
        # Urgencias
        tk.Label(
            container,
            text="⏰ Distribución de Urgencias",
            font=('Segoe UI', 13, 'bold'),
            bg='white',
            fg=self.colors['dark']
        ).pack(anchor='w', pady=(20, 10))
        
        urgencia_colors = {
            'urgente': self.colors['danger'],
            'alta': self.colors['warning'],
            'moderada': self.colors['primary'],
            'baja': self.colors['success']
        }
        
        for urg in stats['urgencias']:
            urg_row = tk.Frame(container, bg='white')
            urg_row.pack(fill='x', pady=3)
            
            tk.Label(
                urg_row,
                text=urg['urgencia'].upper(),
                font=('Segoe UI', 10),
                bg='white',
                width=15,
                anchor='w'
            ).pack(side='left')
            
            tk.Label(
                urg_row,
                text=f"{urg['cantidad']} casos",
                font=('Segoe UI', 10, 'bold'),
                bg=urgencia_colors.get(urg['urgencia'], '#6c757d'),
                fg='white',
                padx=12,
                pady=5
            ).pack(side='left')
    
    def _create_stat_card(self, parent, icon, value, label, color):
        """Crea una tarjeta de estadística"""
        card = tk.Frame(parent, bg=color, relief='solid', bd=0)
        
        content = tk.Frame(card, bg=color)
        content.pack(padx=20, pady=20)
        
        tk.Label(
            content,
            text=icon,
            font=('Segoe UI', 32),
            bg=color,
            fg='white'
        ).pack()
        
        tk.Label(
            content,
            text=str(value),
            font=('Segoe UI', 24, 'bold'),
            bg=color,
            fg='white'
        ).pack()
        
        tk.Label(
            content,
            text=label,
            font=('Segoe UI', 10),
            bg=color,
            fg='white'
        ).pack()
        
        return card
    
    def _refresh_history(self, all_tab, recent_tab, stats_tab, search_var, search_entry):
        """Refresca todas las pestañas del historial"""
        # Limpiar y recrear cada pestaña
        for widget in all_tab.winfo_children():
            widget.destroy()
        for widget in recent_tab.winfo_children():
            widget.destroy()
        for widget in stats_tab.winfo_children():
            widget.destroy()
        
        self._create_all_patients_tab(all_tab, search_var, search_entry)
        self._create_recent_diagnostics_tab(recent_tab)
        self._create_statistics_tab(stats_tab)
        
        messagebox.showinfo("Éxito", "Historial actualizado")
    
    # ==================== MÉTODOS DE BASE DE DATOS ====================
    
    def show_patient_history(self):
        """Muestra el historial de diagnósticos del paciente actual"""
        patient_name = self.patient_name.get()
        
        if not patient_name or patient_name == "Paciente":
            messagebox.showwarning(
                "Advertencia",
                "Por favor ingrese un nombre de paciente válido"
            )
            return
        
        # Obtener historial
        historial = self.db_manager.obtener_historial_paciente(patient_name)
        
        if not historial:
            messagebox.showinfo(
                "Historial",
                f"No se encontraron diagnósticos previos para {patient_name}"
            )
            return
        
        # Crear ventana de historial
        history_window = tk.Toplevel(self.root)
        history_window.title(f"Historial de {patient_name}")
        history_window.geometry("800x600")
        
        # Frame principal
        main_frame = ttk.Frame(history_window, padding=20)
        main_frame.pack(fill='both', expand=True)
        
        # Título
        title = ttk.Label(
            main_frame,
            text=f"📋 Historial Médico de {patient_name}",
            font=('Segoe UI', 14, 'bold')
        )
        title.pack(pady=10)
        
        # Treeview para mostrar historial
        columns = ('Fecha', 'Diagnóstico', 'Confianza', 'Urgencia')
        tree = ttk.Treeview(main_frame, columns=columns, show='tree headings', height=15)
        
        tree.heading('#0', text='ID')
        tree.heading('Fecha', text='Fecha')
        tree.heading('Diagnóstico', text='Diagnóstico')
        tree.heading('Confianza', text='Confianza %')
        tree.heading('Urgencia', text='Urgencia')
        
        tree.column('#0', width=50)
        tree.column('Fecha', width=150)
        tree.column('Diagnóstico', width=300)
        tree.column('Confianza', width=100)
        tree.column('Urgencia', width=100)
        
        # Agregar datos
        for diag in historial:
            tree.insert('', 'end', 
                       text=str(diag['id']),
                       values=(
                           diag['fecha'],
                           diag['diagnostico'],
                           f"{diag['confianza']*100:.1f}%",
                           diag['urgencia']
                       ))
        
        tree.pack(fill='both', expand=True, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(
            btn_frame,
            text="Ver Detalles",
            command=lambda: self.show_diagnosis_details(tree)
        ).pack(side='left', padx=5)
        
        ttk.Button(
            btn_frame,
            text="Cerrar",
            command=history_window.destroy
        ).pack(side='left', padx=5)
    
    def show_diagnosis_details(self, tree):
        """Muestra los detalles de un diagnóstico seleccionado"""
        selection = tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Seleccione un diagnóstico")
            return
        
        # Obtener ID del diagnóstico
        item = tree.item(selection[0])
        diag_id = int(item['text'])
        
        # Obtener detalles
        detalles = self.db_manager.obtener_diagnostico_detallado(diag_id)
        
        if not detalles:
            messagebox.showerror("Error", "No se pudieron cargar los detalles")
            return
        
        # Crear ventana de detalles
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Detalles del Diagnóstico #{diag_id}")
        details_window.geometry("700x600")
        
        # Frame con scroll
        canvas = tk.Canvas(details_window)
        scrollbar = ttk.Scrollbar(details_window, orient='vertical', command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Contenido
        content = ttk.Frame(scrollable_frame, padding=20)
        content.pack(fill='both', expand=True)
        
        # Información general
        ttk.Label(
            content,
            text=f"Paciente: {detalles['paciente_nombre']}",
            font=('Segoe UI', 12, 'bold')
        ).pack(anchor='w', pady=5)
        
        ttk.Label(
            content,
            text=f"Fecha: {detalles['fecha_diagnostico']}",
            font=('Segoe UI', 10)
        ).pack(anchor='w')
        
        ttk.Separator(content, orient='horizontal').pack(fill='x', pady=10)
        
        # Diagnóstico
        ttk.Label(
            content,
            text="Diagnóstico Principal:",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor='w', pady=5)
        
        ttk.Label(
            content,
            text=detalles['diagnostico_principal'],
            font=('Segoe UI', 10)
        ).pack(anchor='w')
        
        ttk.Label(
            content,
            text=f"Confianza: {detalles['confianza_principal']*100:.1f}%",
            font=('Segoe UI', 10)
        ).pack(anchor='w')
        
        ttk.Label(
            content,
            text=f"Gravedad: {detalles['gravedad']} | Urgencia: {detalles['urgencia']}",
            font=('Segoe UI', 10)
        ).pack(anchor='w')
        
        ttk.Separator(content, orient='horizontal').pack(fill='x', pady=10)
        
        # Síntomas
        ttk.Label(
            content,
            text="Síntomas Evaluados:",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor='w', pady=5)
        
        symptoms_frame = ttk.Frame(content)
        symptoms_frame.pack(fill='x', pady=5)
        
        for sintoma in detalles['sintomas'][:10]:  # Mostrar primeros 10
            ttk.Label(
                symptoms_frame,
                text=f"• {sintoma['nombre_sintoma']}: {sintoma['valor_sintoma']}",
                font=('Segoe UI', 9)
            ).pack(anchor='w', padx=20)
        
        ttk.Separator(content, orient='horizontal').pack(fill='x', pady=10)
        
        # Recomendaciones
        ttk.Label(
            content,
            text="Recomendaciones:",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor='w', pady=5)
        
        for rec in detalles['recomendaciones']:
            ttk.Label(
                content,
                text=f"✓ {rec}",
                font=('Segoe UI', 9),
                wraplength=600
            ).pack(anchor='w', padx=20, pady=2)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        ttk.Button(
            details_window,
            text="Cerrar",
            command=details_window.destroy
        ).pack(pady=10)
    
    def search_patients(self):
        """Busca pacientes en la base de datos"""
        # Ventana de búsqueda
        search_window = tk.Toplevel(self.root)
        search_window.title("Buscar Pacientes")
        search_window.geometry("600x500")
        
        main_frame = ttk.Frame(search_window, padding=20)
        main_frame.pack(fill='both', expand=True)
        
        # Campo de búsqueda
        search_frame = ttk.Frame(main_frame)
        search_frame.pack(fill='x', pady=10)
        
        ttk.Label(search_frame, text="Buscar:").pack(side='left', padx=5)
        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=search_var, width=30)
        search_entry.pack(side='left', padx=5)
        
        # Listbox para resultados
        results_frame = ttk.Frame(main_frame)
        results_frame.pack(fill='both', expand=True, pady=10)
        
        listbox = tk.Listbox(results_frame, height=15)
        listbox.pack(side='left', fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=listbox.yview)
        scrollbar.pack(side='right', fill='y')
        listbox.configure(yscrollcommand=scrollbar.set)
        
        def do_search():
            listbox.delete(0, tk.END)
            termino = search_var.get()
            if termino:
                resultados = self.db_manager.buscar_pacientes(termino)
                for pac in resultados:
                    listbox.insert(tk.END, f"{pac['nombre']} - {pac['fecha_registro']}")
        
        ttk.Button(
            search_frame,
            text="Buscar",
            command=do_search
        ).pack(side='left', padx=5)
        
        ttk.Button(
            main_frame,
            text="Cerrar",
            command=search_window.destroy
        ).pack(pady=10)
    
    def show_statistics(self):
        """Muestra estadísticas de la base de datos"""
        stats = self.db_manager.obtener_estadisticas()
        
        # Ventana de estadísticas
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Estadísticas del Sistema")
        stats_window.geometry("600x500")
        
        main_frame = ttk.Frame(stats_window, padding=20)
        main_frame.pack(fill='both', expand=True)
        
        # Título
        ttk.Label(
            main_frame,
            text="📊 Estadísticas del Sistema",
            font=('Segoe UI', 14, 'bold')
        ).pack(pady=10)
        
        # Estadísticas generales
        stats_text = f"""
        Total de Pacientes Registrados: {stats['total_pacientes']}
        Total de Diagnósticos Realizados: {stats['total_diagnosticos']}
        
        DIAGNÓSTICOS MÁS COMUNES:
        """
        
        for i, diag in enumerate(stats['diagnosticos_comunes'], 1):
            stats_text += f"\n{i}. {diag['diagnostico']} - {diag['cantidad']} casos"
        
        stats_text += "\n\nURGENCIAS REGISTRADAS:"
        for urg in stats['urgencias']:
            stats_text += f"\n• {urg['urgencia']}: {urg['cantidad']} casos"
        
        text_widget = tk.Text(main_frame, wrap='word', height=20)
        text_widget.pack(fill='both', expand=True, pady=10)
        text_widget.insert('1.0', stats_text)
        text_widget.config(state='disabled')
        
        ttk.Button(
            main_frame,
            text="Cerrar",
            command=stats_window.destroy
        ).pack(pady=10)
    
    def export_to_csv(self):
        """Exporta todos los datos a CSV"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile=f"diagnosticos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
        
        if filename:
            try:
                self.db_manager.exportar_datos_csv(filename)
                messagebox.showinfo(
                    "Éxito",
                    f"Datos exportados exitosamente a:\n{filename}"
                )
            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Error al exportar datos:\n{str(e)}"
                )



def main():
    """Función principal"""
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
