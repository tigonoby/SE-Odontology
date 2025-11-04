# Estructura del Proyecto - Sistema Experto de Odontología

```
Odontologia-proyect/
│
├── 📄 README.md                      # Documentación principal del proyecto
├── 📄 requirements.txt               # Dependencias de Python
├── 📄 .gitignore                     # Archivos ignorados por Git
│
├── 📁 src/                           # Código fuente principal
│   ├── 📄 __init__.py               # Módulo raíz
│   ├── 📄 main.py                   # Punto de entrada de la aplicación ⭐
│   │
│   ├── 📁 knowledge_base/            # Base de conocimientos
│   │   ├── 📄 __init__.py
│   │   ├── 📄 facts.py              # Hechos, síntomas y diagnósticos
│   │   ├── 📄 crisp_rules.py        # Reglas determinísticas (IF-THEN)
│   │   └── 📄 fuzzy_rules.py        # Reglas difusas con lógica fuzzy
│   │
│   ├── 📁 inference_engine/          # Motor de inferencia
│   │   ├── 📄 __init__.py
│   │   ├── 📄 forward_chaining.py   # Encadenamiento hacia adelante
│   │   ├── 📄 fuzzy_logic.py        # Sistema de lógica difusa
│   │   └── 📄 diagnosis.py          # Lógica de diagnóstico principal
│   │
│   ├── 📁 gui/                       # Interfaz gráfica de usuario
│   │   ├── 📄 __init__.py
│   │   ├── 📄 main_window.py        # Ventana principal de la aplicación
│   │   ├── 📄 symptoms_panel.py     # Panel de ingreso de síntomas
│   │   └── 📄 results_panel.py      # Panel de visualización de resultados
│   │
│   └── 📁 utils/                     # Utilidades del sistema
│       ├── 📄 __init__.py
│       ├── 📄 logger.py             # Sistema de registro de eventos (logs)
│       └── 📄 report_generator.py   # Generador de reportes PDF
│
├── 📁 tests/                         # Casos de prueba
│   ├── 📄 README.md                 # Documentación de pruebas
│   └── 📄 test_diagnosis.py         # Pruebas unitarias del sistema
│
├── 📁 data/                          # Datos y casos de ejemplo
│   └── 📄 casos_ejemplo.md          # Casos clínicos de ejemplo
│
├── 📁 docs/                          # Documentación del proyecto
│   ├── 📄 INSTALACION.md            # Guía de instalación y ejecución
│   └── 📄 documentacion_tecnica.md  # Documentación técnica completa
│
├── 📁 logs/                          # Archivos de registro (generados)
│   └── sistema_YYYYMMDD.log         # Logs diarios del sistema
│
└── 📁 reports/                       # Reportes PDF generados
    └── diagnostico_*.pdf             # Reportes de diagnóstico

```

## Descripción de Componentes

### 🎯 Archivos Principales

- **`src/main.py`**: Punto de entrada. Ejecute este archivo para iniciar la aplicación.
- **`requirements.txt`**: Lista todas las dependencias necesarias.
- **`README.md`**: Documentación general y guía de inicio rápido.

### 🧠 Base de Conocimientos (`src/knowledge_base/`)

Contiene todo el conocimiento experto del sistema:

- **`facts.py`**: Define síntomas, diagnósticos y recomendaciones
- **`crisp_rules.py`**: Reglas determinísticas (ej: SI caries_visible Y dolor_dulce ENTONCES caries)
- **`fuzzy_rules.py`**: Reglas difusas para casos ambiguos

### ⚙️ Motor de Inferencia (`src/inference_engine/`)

Procesa los síntomas y genera diagnósticos:

- **`forward_chaining.py`**: Implementa encadenamiento hacia adelante
- **`fuzzy_logic.py`**: Maneja lógica difusa para síntomas ambiguos
- **`diagnosis.py`**: Coordina el proceso de diagnóstico completo

### 🖥️ Interfaz Gráfica (`src/gui/`)

Interfaz visual con tkinter:

- **`main_window.py`**: Ventana principal con menús y controles
- **`symptoms_panel.py`**: Formulario para ingresar síntomas (escalas, combos, checkboxes)
- **`results_panel.py`**: Muestra diagnósticos, confianza y recomendaciones

### 🛠️ Utilidades (`src/utils/`)

Herramientas de soporte:

- **`logger.py`**: Registra eventos, errores y diagnósticos
- **`report_generator.py`**: Crea reportes PDF profesionales

### ✅ Pruebas (`tests/`)

Validación del sistema:

- **`test_diagnosis.py`**: 5 casos de prueba (caries, pulpitis, absceso, gingivitis, sensibilidad)

### 📚 Documentación (`docs/`)

Guías y manuales:

- **`INSTALACION.md`**: Guía paso a paso de instalación
- **`documentacion_tecnica.md`**: Arquitectura, reglas y funcionamiento

### 📊 Datos (`data/`)

- **`casos_ejemplo.md`**: 8 casos clínicos de ejemplo para probar

### 📝 Archivos Generados

- **`logs/`**: Logs automáticos del sistema
- **`reports/`**: PDFs generados con diagnósticos

## Flujo de Ejecución

```
1. Usuario ejecuta: python src/main.py
                          ↓
2. main.py → Carga MainWindow (GUI)
                          ↓
3. Usuario ingresa síntomas en symptoms_panel.py
                          ↓
4. Click en "Diagnosticar"
                          ↓
5. DiagnosisEngine procesa:
   a. Evalúa reglas crisp (crisp_rules.py)
   b. Evalúa reglas fuzzy (fuzzy_rules.py)
   c. Resuelve conflictos (forward_chaining.py)
                          ↓
6. Resultados mostrados en results_panel.py
                          ↓
7. Usuario puede:
   - Ver recomendaciones
   - Guardar PDF (report_generator.py)
   - Limpiar y repetir
```

## Dependencias Principales

```
tkinter        → Interfaz gráfica (incluido en Python)
scikit-fuzzy   → Lógica difusa
numpy          → Cálculos numéricos
reportlab      → Generación de PDF
matplotlib     → Gráficos (opcional)
pillow         → Manejo de imágenes
```

## Tamaño Aproximado

```
Código fuente:     ~3,500 líneas
Archivos Python:   15 archivos
Documentación:     ~2,000 líneas
Total proyecto:    ~10 MB (sin venv)
Con venv:          ~150 MB
```

## Convenciones de Código

- **PEP 8**: Estilo de código Python
- **Docstrings**: Documentación en cada función
- **Type hints**: Opcional, usado donde es útil
- **Comments**: En español para claridad educativa

## Ejecutar el Sistema

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python src/main.py

# Ejecutar pruebas
python tests/test_diagnosis.py
```

---

**🦷 Sistema Experto de Odontología v1.0**
*Proyecto Educativo - Universidad*
