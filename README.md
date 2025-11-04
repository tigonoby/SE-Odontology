# Sistema Experto de Odontología 🦷

## Descripción
Sistema experto en odontología que utiliza reglas crisp (determinísticas) y lógica difusa (fuzzy) para identificar de manera preliminar la causa probable del dolor dental a partir de los síntomas reportados por el paciente.

## Objetivos del Proyecto

### Objetivo General
Diseñar e implementar un sistema experto en odontología que, a partir de los síntomas reportados por el paciente, identifique de manera preliminar la causa probable del dolor dental y oriente sobre la necesidad de atención profesional.

### Objetivos Específicos
1. Analizar los síntomas comunes del dolor dental (caries, pulpitis, infecciones, sensibilidad, enfermedades de encías)
2. Definir reglas crisp que relacionen síntomas con posibles causas
3. Implementar módulo de lógica difusa para casos con síntomas ambiguos
4. Desarrollar prototipo en Python con interfaz gráfica
5. Evaluar el funcionamiento mediante pruebas con casos reales

## Arquitectura del Sistema

### Componentes Principales
- **Base de Conocimientos**: Contiene hechos y reglas odontológicas
- **Motor de Inferencia**: Procesa síntomas y aplica reglas (encadenamiento hacia adelante)
- **Interfaz de Usuario**: GUI intuitiva para ingreso de síntomas y visualización de resultados
- **Sistema de Reportes**: Genera reportes PDF con diagnósticos y recomendaciones

## Estructura del Proyecto

```
Odontologia-proyect/
│
├── src/
│   ├── knowledge_base/
│   │   ├── __init__.py
│   │   ├── facts.py              # Hechos y síntomas
│   │   ├── crisp_rules.py        # Reglas determinísticas
│   │   └── fuzzy_rules.py        # Reglas difusas
│   │
│   ├── inference_engine/
│   │   ├── __init__.py
│   │   ├── forward_chaining.py   # Encadenamiento hacia adelante
│   │   ├── fuzzy_logic.py        # Motor de lógica difusa
│   │   └── diagnosis.py          # Lógica de diagnóstico
│   │
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py        # Ventana principal
│   │   ├── symptoms_panel.py     # Panel de síntomas
│   │   └── results_panel.py      # Panel de resultados
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py             # Sistema de logs
│   │   └── report_generator.py  # Generador de reportes PDF
│   │
│   └── main.py                   # Punto de entrada de la aplicación
│
├── tests/                        # Casos de prueba
├── data/                         # Datos de casos clínicos
├── docs/                         # Documentación
├── reports/                      # Reportes generados
├── logs/                         # Archivos de log
├── requirements.txt              # Dependencias
└── README.md                     # Este archivo
```

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. Clonar o descargar el proyecto

2. Navegar al directorio del proyecto:
```bash
cd "Odontologia-proyect"
```

3. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
```

4. Activar el entorno virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

5. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar la Aplicación
```bash
python src/main.py
```

### Flujo de Uso
1. La aplicación abrirá una interfaz gráfica
2. Ingrese los síntomas del paciente mediante los controles proporcionados
3. Haga clic en "Diagnosticar"
4. Revise el diagnóstico preliminar y las recomendaciones
5. Opcionalmente, genere un reporte PDF

## Diagnósticos Soportados

El sistema puede identificar las siguientes condiciones:

- **Caries Dental**: Deterioro del esmalte y dentina
- **Pulpitis**: Inflamación de la pulpa dental
- **Absceso Dental**: Infección con acumulación de pus
- **Sensibilidad Dental**: Hipersensibilidad a estímulos
- **Gingivitis**: Inflamación de las encías
- **Periodontitis**: Enfermedad periodontal avanzada
- **Bruxismo**: Rechinamiento de dientes
- **Problema de Ortodoncia**: Maloclusión o desalineación

## Síntomas Evaluados

- Tipo de dolor (agudo, punzante, constante, pulsante)
- Intensidad del dolor (escala 0-10)
- Duración del dolor
- Sensibilidad a temperatura (frío/calor)
- Dolor al masticar
- Inflamación de encías
- Sangrado de encías
- Presencia de caries visible
- Mal aliento
- Movilidad dental
- Y más...

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal
- **Tkinter**: Framework de interfaz gráfica
- **scikit-fuzzy**: Implementación de lógica difusa
- **NumPy**: Operaciones numéricas
- **ReportLab**: Generación de reportes PDF
- **Matplotlib**: Visualización de datos

## Pruebas

Ejecutar las pruebas:
```bash
pytest tests/
```

Con cobertura:
```bash
pytest --cov=src tests/
```

## Advertencia Importante ⚠️

**Este sistema es únicamente una herramienta de orientación preliminar y NO reemplaza el diagnóstico de un profesional odontólogo.**

Siempre consulte con un dentista certificado para un diagnóstico definitivo y tratamiento adecuado.

## Autor

Proyecto desarrollado para la Universidad - Curso de Sistemas Expertos

## Licencia

Proyecto educativo - Universidad

---

**Nota**: Este sistema experto está diseñado con fines educativos y de orientación inicial. No debe utilizarse como sustituto de atención médica profesional.
# SE-Odontology
