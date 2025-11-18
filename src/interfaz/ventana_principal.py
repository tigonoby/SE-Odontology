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

from src.interfaz.panel_sintomas import PanelSintomas
from src.interfaz.panel_resultados import PanelResultados
from src.motor_inferencia import MotorDiagnostico
from src.utilidades.registro import Registro
from src.utilidades.generador_reportes import GeneradorReportes


class VentanaPrincipal:
    """Ventana principal del sistema experto"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto de Odontología")
        self.root.geometry("1200x800")
        
        # Centrar ventana
        self.center_window()
        
        # Inicializar componentes
        self.motor_diagnostico = MotorDiagnostico()
        self.registro = Registro()
        self.generador_reportes = GeneradorReportes()
        
        # Variables
        self.current_diagnosis = None
        self.current_symptoms = None
        self.patient_name = tk.StringVar(value="")
        self.patient_age = tk.StringVar(value="")
        
        # Configurar estilo
        self.setup_style()
        
        # Crear widgets
        self.create_menu()
        self.create_widgets()
        
        # Log de inicio
        self.registro.log("Sistema iniciado")

    
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
        
        tk.Label(
            patient_frame,
            text="👤 Nombre:",
            font=('Segoe UI', 10),
            bg=self.colors['primary'],
            fg='white'
        ).pack(side='left', padx=5)
        
        patient_entry = tk.Entry(
            patient_frame,
            textvariable=self.patient_name,
            width=25,
            font=('Segoe UI', 10),
            relief='flat',
            bd=2
        )
        patient_entry.pack(side='left', ipady=3)
        
        tk.Label(
            patient_frame,
            text="📅 Edad:",
            font=('Segoe UI', 10),
            bg=self.colors['primary'],
            fg='white'
        ).pack(side='left', padx=(15, 5))
        
        age_entry = tk.Entry(
            patient_frame,
            textvariable=self.patient_age,
            width=5,
            font=('Segoe UI', 10),
            relief='flat',
            bd=2
        )
        age_entry.pack(side='left', ipady=3)
        
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
        
        self.symptoms_panel = PanelSintomas(canvas)
        
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
        
        self.results_panel = PanelResultados(right_card)
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
        
        # Variable para barra de estado
        self.status_var = tk.StringVar(value="✨ Ingrese los síntomas del paciente y presione Diagnosticar")
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
            validation = self.motor_diagnostico.validate_symptoms(symptoms)
            if not validation['valido']:
                warnings_msg = "\n".join(validation['advertencias'])
                messagebox.showwarning(
                    "Advertencias de Validación",
                    f"Se encontraron las siguientes advertencias:\n\n{warnings_msg}\n\n¿Desea continuar?"
                )
            
            # Realizar diagnóstico
            self.current_diagnosis = self.motor_diagnostico.diagnose(
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
                self.registro.log(
                    f"Diagnóstico realizado para {patient}: {principal['nombre']} "
                    f"(Confianza: {principal['confianza_porcentaje']}%)"
                )
                self.status_var.set(f"✓ Diagnóstico completado")
            else:
                self.registro.log(f"No se encontró diagnóstico para {patient}")
                self.status_var.set("Diagnóstico completado")
            
            # Mostrar resultados
            self.results_panel.display_results(self.current_diagnosis)
            
            
        except Exception as e:
            self.registro.log(f"Error en diagnóstico: {str(e)}", level='ERROR')
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
            self.status_var.set("Formulario limpiado")
            self.registro.log("Formulario limpiado")
    
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
                    'edad': self.patient_age.get() if self.patient_age.get() else None
                }
                
                # Generar reporte
                self.generador_reportes.generate_report(
                    patient_name=self.patient_name.get(),
                    symptoms=symptoms,
                    diagnosis=self.current_diagnosis,
                    output_path=filename,
                    patient_info=patient_info
                )
                
                self.status_var.set(f"Reporte guardado: {os.path.basename(filename)}")
                self.registro.log(f"Reporte PDF generado: {filename}")
                
                messagebox.showinfo(
                    "Éxito",
                    f"Reporte guardado exitosamente en:\n{filename}"
                )
        
        except Exception as e:
            self.registro.log(f"Error al generar PDF: {str(e)}", level='ERROR')
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
            self.registro.log("Sistema cerrado")
            self.root.quit()


def main():
    """Función principal"""
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()

