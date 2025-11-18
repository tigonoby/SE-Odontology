"""
Sistema de Logging
Registra eventos y errores del sistema
"""

import logging
import os
from datetime import datetime


class Registro:
    """Clase para manejar el logging del sistema"""
    
    def __init__(self, log_dir='logs'):
        """
        Inicializa el logger
        log_dir: directorio donde se guardarán los logs
        """
        self.log_dir = log_dir
        self.ensure_log_directory()
        self.setup_logger()
    
    def ensure_log_directory(self):
        """Asegura que el directorio de logs existe"""
        # Obtener la ruta del proyecto
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        self.log_dir_path = os.path.join(project_root, self.log_dir)
        
        if not os.path.exists(self.log_dir_path):
            os.makedirs(self.log_dir_path)
    
    def setup_logger(self):
        """Configura el logger"""
        # Nombre del archivo de log con fecha
        log_filename = datetime.now().strftime('sistema_%Y%m%d.log')
        log_path = os.path.join(self.log_dir_path, log_filename)
        
        # Configurar formato
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        date_format = '%Y-%m-%d %H:%M:%S'
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            datefmt=date_format,
            handlers=[
                logging.FileHandler(log_path, encoding='utf-8'),
                logging.StreamHandler()  # También imprimir en consola
            ]
        )
        
        self.logger = logging.getLogger('SistemaExperto')
    
    def log(self, message, level='INFO'):
        """
        Registra un mensaje
        
        Args:
            message: mensaje a registrar
            level: nivel de logging (INFO, WARNING, ERROR, DEBUG)
        """
        level = level.upper()
        
        if level == 'DEBUG':
            self.logger.debug(message)
        elif level == 'INFO':
            self.logger.info(message)
        elif level == 'WARNING':
            self.logger.warning(message)
        elif level == 'ERROR':
            self.logger.error(message)
        elif level == 'CRITICAL':
            self.logger.critical(message)
        else:
            self.logger.info(message)
    
    def debug(self, message):
        """Registra un mensaje de debug"""
        self.log(message, 'DEBUG')
    
    def info(self, message):
        """Registra un mensaje informativo"""
        self.log(message, 'INFO')
    
    def warning(self, message):
        """Registra una advertencia"""
        self.log(message, 'WARNING')
    
    def error(self, message):
        """Registra un error"""
        self.log(message, 'ERROR')
    
    def critical(self, message):
        """Registra un error crítico"""
        self.log(message, 'CRITICAL')
    
    def log_diagnosis(self, patient_name, symptoms, diagnosis):
        """
        Registra un diagnóstico completo
        
        Args:
            patient_name: nombre del paciente
            symptoms: diccionario de síntomas
            diagnosis: resultado del diagnóstico
        """
        self.logger.info(f"=== DIAGNÓSTICO PARA: {patient_name} ===")
        
        # Síntomas relevantes (con valores > 0 o diferentes de "no")
        relevant_symptoms = []
        for key, value in symptoms.items():
            if isinstance(value, (int, float)) and value > 0:
                relevant_symptoms.append(f"{key}: {value}")
            elif isinstance(value, str) and value != 'no':
                relevant_symptoms.append(f"{key}: {value}")
        
        if relevant_symptoms:
            self.logger.info("Síntomas reportados:")
            for symptom in relevant_symptoms:
                self.logger.info(f"  - {symptom}")
        
        # Diagnóstico
        if diagnosis and diagnosis.get('num_diagnosticos', 0) > 0:
            principal = diagnosis['principal']
            self.logger.info(f"Diagnóstico principal: {principal['nombre']}")
            self.logger.info(f"Confianza: {principal['confianza_porcentaje']}%")
            self.logger.info(f"Urgencia: {principal['urgencia']}")
            
            if diagnosis['num_diagnosticos'] > 1:
                self.logger.info("Diagnósticos alternativos:")
                for diag in diagnosis['diagnosticos'][1:]:
                    self.logger.info(f"  - {diag['nombre']} ({diag['confianza_porcentaje']}%)")
        else:
            self.logger.info("No se pudo determinar un diagnóstico")
        
        self.logger.info("=" * 50)
    
    def log_error_with_traceback(self, error, context=""):
        """
        Registra un error con su traceback
        
        Args:
            error: excepción capturada
            context: contexto adicional del error
        """
        import traceback
        
        self.logger.error(f"ERROR: {context}")
        self.logger.error(f"Tipo: {type(error).__name__}")
        self.logger.error(f"Mensaje: {str(error)}")
        self.logger.error("Traceback:")
        self.logger.error(traceback.format_exc())
    
    def get_log_path(self):
        """Retorna la ruta del archivo de log actual"""
        log_filename = datetime.now().strftime('sistema_%Y%m%d.log')
        return os.path.join(self.log_dir_path, log_filename)
