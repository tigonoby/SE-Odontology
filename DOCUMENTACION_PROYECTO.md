# 📚 Documentación del Sistema Experto de Odontología

## 🎯 Descripción General del Proyecto

**Sistema Experto de Odontología** es una aplicación inteligente de diagnóstico dental que utiliza **Inteligencia Artificial** basada en **sistemas expertos** para analizar síntomas bucales y proporcionar diagnósticos precisos con niveles de confianza específicos.

### Características Principales
- ✅ **53+ Reglas Expertas** organizadas en 9 categorías de diagnósticos dentales
- ✅ **30+ Diagnósticos Diferentes** cubriendo desde caries hasta emergencias médicas
- ✅ **Lógica Crisp y Difusa** para razonamiento preciso y manejo de incertidumbre
- ✅ **Interfaz Gráfica Intuitiva** desarrollada con Tkinter
- ✅ **Sistema de Confianza Variable** (25% - 98%) según severidad de síntomas
- ✅ **Generación de Reportes PDF** profesionales
- ✅ **Sistema de Logging** para trazabilidad de diagnósticos

---

## 🏗️ Arquitectura del Sistema

El sistema está organizado en **4 módulos principales**:

```
SE-Odontology/
│
├── src/
│   ├── base_conocimiento/      # Base de Conocimientos (Reglas + Hechos)
│   ├── motor_inferencia/        # Motor de Inferencia (Razonamiento)
│   ├── interfaz/                # Interfaz Gráfica (GUI)
│   └── utilidades/              # Utilidades (Logs, Reportes)
│
├── data/                        # Datos del sistema
├── logs/                        # Archivos de registro
├── requirements.txt             # Dependencias Python
└── run.py                       # Punto de entrada de la aplicación
```

---

## 📂 1. BASE DE CONOCIMIENTO (`src/base_conocimiento/`)

La **base de conocimiento** es el cerebro del sistema experto. Almacena todo el conocimiento del dominio odontológico en forma de **hechos**, **reglas crisp** y **reglas difusas**.

### 📄 `hechos.py` - Base de Conocimientos Factuales

**¿Qué hace?**
- Define **30+ diagnósticos** dentales con descripciones y niveles de urgencia
- Almacena **recomendaciones específicas** para cada diagnóstico (4-6 por condición)
- Establece **síntomas evaluables** (50+ parámetros diferentes)

**Componentes Principales:**

#### 1️⃣ **DIAGNOSTICOS Dictionary**
Contiene 30+ condiciones dentales organizadas por gravedad:

```python
DIAGNOSTICOS = {
    'celulitis_facial': {
        'nombre': 'Celulitis Facial',
        'descripcion': 'EMERGENCIA MÉDICA - Infección grave...',
        'urgencia': 'urgente'  # urgente, alta, moderada, baja
    },
    'pulpitis': {...},
    'caries_profunda': {...},
    # ... 27+ diagnósticos más
}
```

**Categorías de Diagnósticos:**
- **Emergencias**: celulitis_facial, absceso, necrosis_pulpar
- **Pulpa**: pulpitis (reversible/irreversible)
- **Caries**: caries_inicial, caries, caries_profunda, caries_radicular
- **Periodontales**: gingivitis, periodontitis, absceso_periodontal
- **Sensibilidad/Desgaste**: sensibilidad, erosion_dental, abrasion_dental
- **Trauma**: fractura_dental, fisura_dental
- **Funcionales**: bruxismo, atm_disfuncion
- **Post-tratamiento**: fracaso_endodoncia, dolor_post_obturacion
- **Otros**: ortodoncia, impactacion_alimentaria

#### 2️⃣ **RECOMENDACIONES Dictionary**
Proporciona 4-6 recomendaciones específicas por cada diagnóstico:

```python
RECOMENDACIONES = {
    'caries': [
        "Agende cita con dentista para evaluación urgente",
        "Evite alimentos y bebidas azucaradas",
        "Use hilo dental diariamente",
        # ... más recomendaciones
    ]
}
```

#### 3️⃣ **SINTOMAS Dictionary**
Define 50+ síntomas evaluables agrupados en:

- **Dolor**: tipo (agudo, pulsante, sordo), intensidad (0-10), duración
- **Sensibilidad**: frío, calor, dulce (escalas 0-10)
- **Encías**: inflamación, sangrado, color, retracción
- **Visual**: caries visible, manchas, fracturas, desgaste
- **Infección**: hinchazón facial, pus, fiebre, mal aliento
- **Movilidad/Funcional**: movilidad dental, problemas de mordida, rechinar dientes

**¿Por qué es importante?**
> Esta base de datos representa el **conocimiento experto** de un odontólogo. Es la diferencia entre un sistema genérico y un verdadero **experto digital**.

---

### 📄 `reglas_crisp.py` - Reglas Determinísticas (53 Reglas)

**¿Qué hace?**
- Implementa **53 reglas IF-THEN determinísticas** organizadas en 9 categorías
- Cada regla tiene condiciones específicas y niveles de confianza (70%-98%)
- Usa **lógica booleana** para diagnósticos precisos cuando los síntomas coinciden exactamente

**Estructura de una Regla:**

```python
def rule_celulitis_facial(facts):
    """Celulitis facial - EMERGENCIA MÉDICA"""
    conditions = [
        lambda f: f.get('hinchazon_cara') == 'si',
        lambda f: f.get('fiebre') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 8,
        lambda f: f.get('mal_aliento') in ['moderado', 'severo']
    ]
    return Rule(
        name="Celulitis facial - EMERGENCIA",
        conditions=conditions,
        conclusion="celulitis_facial",
        confidence=0.98  # 98% de confianza
    )
```

**Categorías de las 53 Reglas:**

| Categoría | # Reglas | Ejemplos | Confianza |
|-----------|----------|----------|-----------|
| **EMERGENCIAS** | 6 | Celulitis, Abscesos agudos | 92-98% |
| **PULPA** | 7 | Necrosis, Pulpitis irreversible/reversible | 82-97% |
| **CARIES** | 10 | Caries profunda, moderada, inicial | 70-96% |
| **PERIODONTALES** | 9 | Periodontitis, Gingivitis | 75-94% |
| **SENSIBILIDAD/DESGASTE** | 6 | Erosión, Abrasión, Hipersensibilidad | 72-86% |
| **TRAUMA** | 3 | Fracturas, Fisuras | 78-96% |
| **FUNCIONALES** | 4 | Bruxismo, Disfunción ATM | 76-93% |
| **POST-TRATAMIENTO** | 3 | Fracaso endodoncia | 77-87% |
| **OTROS** | 2 | Ortodoncia, Impactación | 71-79% |

**Ejemplo de Evaluación:**

```python
# Si el paciente tiene:
facts = {
    'hinchazon_cara': 'si',
    'pus_visible': 'si',
    'intensidad_dolor': 8
}

# La regla rule_absceso_agudo_1 se activa
# Diagnóstico: "absceso" con confianza 98%
```

**¿Por qué 53 reglas?**
> Las reglas cubren **TODAS las combinaciones comunes** de síntomas que un odontólogo consideraría. Más reglas = **mayor cobertura diagnóstica** y menos diagnósticos genéricos.

---

### 📄 `reglas_difusas.py` - Reglas de Lógica Difusa

**¿Qué hace?**
- Maneja **incertidumbre y ambigüedad** en los síntomas
- Usa **conjuntos difusos** (bajo, moderado, severo) en lugar de valores exactos
- Complementa las reglas crisp cuando los síntomas no son claros

**Conceptos Clave:**

#### Conjuntos Difusos
En lugar de decir "dolor = 5", la lógica difusa dice:
- "dolor es 30% moderado Y 70% severo"

Esto permite razonar con **incertidumbre**, como lo hace un médico real.

**Ejemplo de Regla Difusa:**

```python
{
    'antecedentes': [
        ('dolor', 'severo'),       # Si dolor es SEVERO
        ('sensibilidad', 'alta'),  # Y sensibilidad es ALTA
        ('inflamacion', 'alta')    # Y inflamación es ALTA
    ],
    'consecuente': 'pulpitis',
    'confianza': 0.85
}
```

**¿Cuándo se usa?**
- Cuando los síntomas son **ambiguos o intermedios**
- Cuando ninguna regla crisp aplica exactamente
- Para **afinar diagnósticos** con múltiples síntomas graduales

---

## ⚙️ 2. MOTOR DE INFERENCIA (`src/motor_inferencia/`)

El **motor de inferencia** es el "cerebro pensante" que **aplica las reglas** a los síntomas del paciente para generar diagnósticos.

### 📄 `diagnostico.py` - Motor Principal de Diagnóstico

**¿Qué hace?**
- **Coordina** la evaluación de reglas crisp y difusas
- **Combina resultados** de múltiples reglas aplicadas
- Genera **diagnóstico de respaldo inteligente** si no se activa ninguna regla
- Calcula **niveles de confianza dinámicos** (25%-95%) según severidad

**Proceso de Diagnóstico:**

```
1. Recibe síntomas del paciente
   ↓
2. Evalúa 53 reglas crisp
   ↓
3. Evalúa reglas difusas (si están habilitadas)
   ↓
4. Combina todos los resultados
   ↓
5. Si NO hay resultados → Genera diagnóstico de respaldo
   ↓
6. Aplica resolución de conflictos
   ↓
7. Selecciona diagnóstico PRINCIPAL (mayor confianza)
   ↓
8. Retorna diagnósticos + recomendaciones + nivel urgencia
```

**Sistema de Respaldo Inteligente:**

Si ninguna regla se activa, el sistema NO retorna 50% genérico. En su lugar, **analiza por prioridad**:

```python
# Análisis por GRAVEDAD (de mayor a menor)
1. ¿Hay absceso o infección? → 70-95% confianza
2. ¿Hay pulpitis? → 60-85% confianza
3. ¿Hay caries? → 60-88% confianza
4. ¿Hay periodontitis? → 65-82% confianza
5. ¿Hay gingivitis? → 55-80% confianza
6. ¿Hay sensibilidad? → 50-75% confianza
7. ¿Caries inicial? → 45-68% confianza
8. ¿NINGÚN síntoma? → 25-30% "evaluacion_general"
```

**¿Por qué es importante?**
> Este sistema garantiza que **SIEMPRE** se dé un diagnóstico útil basado en síntomas, incluso cuando los datos son incompletos.

---

### 📄 `encadenamiento_adelante.py` - Forward Chaining

**¿Qué hace?**
- Implementa **encadenamiento hacia adelante** (Forward Chaining)
- Parte de los **HECHOS** (síntomas) → Aplica **REGLAS** → Llega a **CONCLUSIONES**
- Maneja **resolución de conflictos** cuando múltiples reglas se activan

**Proceso Forward Chaining:**

```
HECHOS (Síntomas del Paciente)
   ↓
Evaluar TODAS las reglas
   ↓
Reglas que COINCIDEN se activan
   ↓
Múltiples conclusiones posibles
   ↓
RESOLUCIÓN DE CONFLICTOS:
   - Estrategia 1: Mayor especificidad
   - Estrategia 2: Mayor confianza
   - Estrategia 3: Combinar todos
   ↓
CONCLUSIÓN FINAL
```

**Estrategias de Resolución:**

1. **`highest_confidence`**: Selecciona solo el diagnóstico con mayor confianza
2. **`most_specific`**: Prioriza reglas con más condiciones (más específicas)
3. **`combine`**: Retorna TODOS los diagnósticos ordenados por confianza

**¿Por qué Forward Chaining?**
> Es ideal para diagnóstico médico: **partimos de síntomas observables** (hechos) y buscamos posibles enfermedades (conclusiones). Es como el razonamiento de un médico real.

---

### 📄 `logica_difusa.py` - Motor de Lógica Difusa

**¿Qué hace?**
- Implementa **conjuntos difusos** (FuzzySet)
- Define **funciones de pertenencia** (triangular, trapezoidal)
- Calcula **grados de pertenencia** (membership degrees)
- Realiza **inferencia difusa** con reglas difusas

**Funciones de Pertenencia:**

```
Intensidad del Dolor (0-10):

Bajo      Moderado    Severo
  ▲         ▲          ▲
 / \       /|\        /|
/   \     / | \      / |
────────────────────────
0   3   5   7   9   10

Ejemplo: Dolor = 6
- 40% pertenece a "moderado"
- 60% pertenece a "severo"
```

**Proceso de Inferencia Difusa:**

```
1. Fuzzificación: Convierte valores numéricos → Grados de pertenencia
   Ejemplo: dolor=7 → 0.6 "moderado" + 0.4 "severo"
   
2. Evaluación de Reglas: Aplica reglas difusas
   SI dolor es "severo" Y sensibilidad es "alta" → pulpitis
   
3. Agregación: Combina resultados de múltiples reglas
   
4. Defuzzificación: Convierte resultado difuso → Valor concreto
   Ejemplo: "pulpitis con confianza 0.85"
```

**¿Por qué Lógica Difusa?**
> Los síntomas médicos **NO son binarios**. Un dolor de "6/10" no es ni bajo ni alto: es algo intermedio. La lógica difusa modela esta **realidad gradual**.

---

## 🖥️ 3. INTERFAZ GRÁFICA (`src/interfaz/`)

La interfaz es la **capa de presentación** que permite al usuario interactuar con el sistema experto de forma visual e intuitiva.

### 📄 `ventana_principal.py` - Ventana Principal

**¿Qué hace?**
- **Coordina** todos los componentes de la aplicación
- Gestiona el **menú principal** (Archivo, Herramientas, Ayuda)
- Maneja **eventos de usuario** (clicks, inputs, diagnósticos)
- Integra **panel de síntomas** y **panel de resultados**
- Controla **generación de reportes PDF** y **exportación de datos**

**Componentes Principales:**

```python
class VentanaPrincipal:
    def __init__(self):
        # Inicializa motor de diagnóstico
        self.motor_diagnostico = MotorDiagnostico()
        
        # Sistemas auxiliares
        self.registro = Registro()  # Logging
        self.generador_reportes = GeneradorReportes()  # PDFs
        
        # Datos del paciente
        self.patient_name = "Paciente Anónimo"
        self.patient_age = "N/A"
```

**Flujo de Interacción:**

```
Usuario Ingresa Síntomas (PanelSintomas)
   ↓
Click en "Diagnosticar"
   ↓
VentanaPrincipal.realizar_diagnostico()
   ↓
MotorDiagnostico.diagnose(symptoms)
   ↓
Resultados → PanelResultados.display_results()
   ↓
Usuario ve diagnóstico + recomendaciones
   ↓
Opción: Generar PDF o Nueva Consulta
```

**Funcionalidades del Menú:**

| Menú | Opciones | Función |
|------|----------|---------|
| **Archivo** | Nueva Consulta | Reinicia formulario de síntomas |
| | Generar Reporte PDF | Crea PDF del diagnóstico actual |
| | Salir | Cierra la aplicación |
| **Herramientas** | Ver Logs | Muestra registros del sistema |
| | Limpiar Logs | Elimina archivos de log |
| **Ayuda** | Acerca de | Información del sistema |
| | Manual de Usuario | Guía de uso |

---

### 📄 `panel_sintomas.py` - Panel de Entrada de Síntomas

**¿Qué hace?**
- Presenta **formulario interactivo** con 50+ síntomas
- Organiza síntomas en **categorías** (Dolor, Sensibilidad, Encías, Visual, Infección)
- Valida **entradas del usuario** antes de diagnosticar
- Usa **sliders**, **dropdowns** y **radio buttons** para entrada de datos

**Organización del Panel:**

```
┌─────────────────────────────────────┐
│  🔍 INFORMACIÓN DEL PACIENTE        │
│  - Nombre                           │
│  - Edad                             │
├─────────────────────────────────────┤
│  😖 DOLOR Y MOLESTIAS              │
│  - Tipo de dolor (dropdown)         │
│  - Intensidad (slider 0-10)         │
│  - Duración (radio buttons)         │
├─────────────────────────────────────┤
│  🧊 SENSIBILIDAD                    │
│  - Al frío (slider 0-10)            │
│  - Al calor (slider 0-10)           │
│  - A lo dulce (slider 0-10)         │
├─────────────────────────────────────┤
│  🦷 ENCÍAS                          │
│  - Inflamación (slider 0-10)        │
│  - Sangrado (dropdown)              │
│  - Color (dropdown)                 │
├─────────────────────────────────────┤
│  👁️ EXAMEN VISUAL                  │
│  - Caries visible (si/no)           │
│  - Fracturas (si/no)                │
│  - Desgaste dental (dropdown)       │
├─────────────────────────────────────┤
│  🦠 SIGNOS DE INFECCIÓN            │
│  - Hinchazón facial (si/no)         │
│  - Pus visible (si/no)              │
│  - Fiebre (si/no)                   │
└─────────────────────────────────────┘
```

**Validación de Datos:**

```python
def get_symptoms(self):
    """Recolecta y valida síntomas"""
    symptoms = {}
    
    # Validar intensidad de dolor (0-10)
    if not 0 <= intensidad_dolor <= 10:
        raise ValueError("Intensidad inválida")
    
    # Validar datos obligatorios
    if tipo_dolor == "" and intensidad_dolor > 0:
        raise ValueError("Debe seleccionar tipo de dolor")
    
    return symptoms
```

---

### 📄 `panel_resultados.py` - Panel de Resultados

**¿Qué hace?**
- Muestra **diagnóstico principal** con nivel de confianza
- Presenta **diagnósticos alternativos** (si existen)
- Visualiza **nivel de urgencia** con códigos de color
- Lista **recomendaciones específicas** por diagnóstico
- Incluye **guía de interpretación** de niveles de confianza

**Diseño Visual:**

```
┌───────────────────────────────────────────┐
│  🚨 ATENCIÓN URGENTE REQUERIDA            │ ← Banner de urgencia
│     (rojo si urgente, naranja si alta)    │
├───────────────────────────────────────────┤
│  📖 Guía de Niveles de Confianza          │
│  • 90-100% → Sistema CASI SEGURO          │
│  • 70-89%  → Sistema BASTANTE SEGURO      │
│  • 50-69%  → Sistema SOSPECHA esto        │
│  • 30-49%  → Sistema tiene DUDAS          │
│  • <30%    → Sistema NO ESTÁ SEGURO       │
├───────────────────────────────────────────┤
│  🎯 DIAGNÓSTICO PRINCIPAL                 │
│                                           │
│  Pulpitis Irreversible                    │
│  "Inflamación severa e irreversible..."   │
│                                           │
│  📊 Nivel de Confianza: 95%               │
│  ████████████████████░ (95%)              │ ← Barra visual
│                                           │
│  ⚠️ Urgencia: ALTA                        │
├───────────────────────────────────────────┤
│  📋 RECOMENDACIONES                       │
│  1. Acuda a dentista URGENTEMENTE         │
│  2. Evite alimentos calientes             │
│  3. Tome analgésicos según prescripción   │
│  4. No demore la consulta                 │
├───────────────────────────────────────────┤
│  🔍 Diagnósticos Alternativos (2)         │
│  • Caries Profunda (88%)                  │
│  • Absceso Dental (82%)                   │
└───────────────────────────────────────────┘
```

**Código de Colores de Urgencia:**

| Urgencia | Color | Mensaje | Cuándo |
|----------|-------|---------|--------|
| **Urgente** | 🔴 Rojo | "ATENCIÓN URGENTE REQUERIDA" | Celulitis, abscesos severos |
| **Alta** | 🟠 Naranja | "Consulte a un odontólogo pronto" | Pulpitis, caries profunda |
| **Moderada** | 🟡 Amarillo | "Agende una cita odontológica" | Caries, gingivitis |
| **Baja** | 🟢 Verde | "Consulta preventiva recomendada" | Sensibilidad leve, evaluación |

---

## 🛠️ 4. UTILIDADES (`src/utilidades/`)

Módulo de **servicios auxiliares** que complementan la funcionalidad principal del sistema.

### 📄 `registro.py` - Sistema de Logging

**¿Qué hace?**
- Registra **todos los eventos** del sistema en archivos de log
- Almacena **diagnósticos realizados** con timestamp
- Guarda **errores y excepciones** para debugging
- Organiza logs por **fecha** (un archivo por día)

**Formato de Logs:**

```
2025-11-18 14:32:10 - Sistema iniciado
2025-11-18 14:32:45 - Diagnóstico realizado: pulpitis (95%)
2025-11-18 14:33:12 - Reporte PDF generado: reporte_20251118_143312.pdf
2025-11-18 14:35:22 - Error en evaluación fuzzy: ValueError
2025-11-18 14:40:05 - Sistema cerrado
```

**Niveles de Log:**

- **INFO**: Eventos normales (inicio, diagnósticos, reportes)
- **WARNING**: Situaciones inesperadas pero no críticas
- **ERROR**: Errores que afectan funcionalidad
- **DEBUG**: Información detallada para desarrollo

**¿Por qué es importante?**
> Los logs permiten **auditoría**, **debugging** y **análisis de uso** del sistema. Esencial para sistemas médicos donde se necesita trazabilidad.

---

### 📄 `generador_reportes.py` - Generador de PDFs

**¿Qué hace?**
- Genera **reportes profesionales en PDF** de los diagnósticos
- Incluye **datos del paciente**, síntomas, diagnósticos y recomendaciones
- Formato **profesional** con logo, colores corporativos y estructura clara
- Guarda reportes con **timestamp único** para evitar sobrescritura

**Contenido del Reporte PDF:**

```
┌────────────────────────────────────────┐
│  🏥 SISTEMA EXPERTO DE ODONTOLOGÍA     │
│  Reporte de Diagnóstico                │
│                                        │
│  Fecha: 18 de Noviembre, 2025          │
│  Hora: 14:32:45                        │
├────────────────────────────────────────┤
│  INFORMACIÓN DEL PACIENTE              │
│  Nombre: Juan Pérez                    │
│  Edad: 35 años                         │
├────────────────────────────────────────┤
│  SÍNTOMAS REPORTADOS                   │
│  • Dolor intenso: 9/10                 │
│  • Tipo: Pulsante                      │
│  • Sensibilidad al calor: 8/10         │
│  • Hinchazón facial: Sí                │
│  • Duración: Más de 7 días             │
├────────────────────────────────────────┤
│  DIAGNÓSTICO PRINCIPAL                 │
│  Pulpitis Irreversible                 │
│  Confianza: 95%                        │
│  Urgencia: ALTA                        │
│                                        │
│  Descripción:                          │
│  "Inflamación severa e irreversible    │
│   de la pulpa dental que requiere      │
│   tratamiento de conducto urgente..."  │
├────────────────────────────────────────┤
│  RECOMENDACIONES                       │
│  1. Acuda a dentista URGENTEMENTE      │
│  2. Evite alimentos calientes/fríos    │
│  3. Tome analgésicos prescritos        │
│  4. No demore la consulta              │
├────────────────────────────────────────┤
│  DIAGNÓSTICOS ALTERNATIVOS             │
│  • Caries Profunda (88%)               │
│  • Necrosis Pulpar (82%)               │
├────────────────────────────────────────┤
│  DISCLAIMER                            │
│  "Este reporte es generado por un      │
│   sistema experto y NO reemplaza       │
│   la evaluación de un profesional."    │
└────────────────────────────────────────┘
```

**Formato Técnico:**
- **Tamaño**: Carta (8.5" x 11")
- **Biblioteca**: ReportLab
- **Estilos**: Colores corporativos, fuentes Helvetica
- **Nombre archivo**: `reporte_YYYYMMDD_HHMMSS.pdf`

---

## 🧠 Cómo Funciona el Sistema (Flujo Completo)

### Proceso Completo de Diagnóstico:

```
┌─────────────────────────────────────────────┐
│  1️⃣ ENTRADA DE DATOS                       │
│  Usuario ingresa síntomas en PanelSintomas  │
│  - Dolor: 8/10, pulsante                    │
│  - Sensibilidad calor: 9/10                 │
│  - Hinchazón facial: Sí                     │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│  2️⃣ VALIDACIÓN                             │
│  PanelSintomas.get_symptoms()               │
│  - Valida rangos (0-10)                     │
│  - Verifica datos requeridos                │
│  - Convierte a formato del motor            │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│  3️⃣ MOTOR DE DIAGNÓSTICO                   │
│  MotorDiagnostico.diagnose(symptoms)        │
│                                             │
│  A) Evaluar Reglas Crisp (53 reglas)       │
│     → rule_pulpitis_irreversible_1 ACTIVA   │
│        Confianza: 97%                       │
│     → rule_absceso_agudo_2 ACTIVA           │
│        Confianza: 96%                       │
│                                             │
│  B) Evaluar Reglas Difusas                  │
│     → fuzzy_rule_dolor_severo ACTIVA        │
│        Confianza: 85%                       │
│                                             │
│  C) Combinar Resultados                     │
│     [pulpitis: 97%, absceso: 96%,...]       │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│  4️⃣ RESOLUCIÓN DE CONFLICTOS               │
│  apply_conflict_resolution()                │
│  - Ordenar por confianza                    │
│  - Seleccionar diagnóstico principal        │
│  - Mantener alternativos                    │
│                                             │
│  Resultado:                                 │
│  Principal: Pulpitis Irreversible (97%)     │
│  Alternativos: Absceso (96%), Caries (85%)  │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│  5️⃣ ENRIQUECIMIENTO DE DATOS               │
│  get_diagnostico_info() + get_recomendaciones()│
│  - Agrega descripción del diagnóstico       │
│  - Carga recomendaciones específicas        │
│  - Determina nivel de urgencia              │
│  - Calcula prioridad de atención            │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│  6️⃣ PRESENTACIÓN DE RESULTADOS             │
│  PanelResultados.display_results()          │
│  - Muestra banner de urgencia               │
│  - Presenta diagnóstico principal           │
│  - Lista recomendaciones (4-6 items)        │
│  - Muestra diagnósticos alternativos        │
│  - Incluye guía de confianza                │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│  7️⃣ ACCIONES ADICIONALES (Opcional)        │
│  - Generar PDF → GeneradorReportes          │
│  - Guardar log → Registro.log()             │
│  - Nueva consulta → Limpiar formulario      │
└─────────────────────────────────────────────┘
```

---

## 📊 Sistema de Niveles de Confianza

### ¿Qué significa cada nivel?

| Rango | Interpretación | Acción Recomendada | Color |
|-------|----------------|-------------------|-------|
| **90-100%** | Sistema **CASI SEGURO** | ⚠️ **Vaya al dentista YA** | 🔴 Rojo |
| **70-89%** | Sistema **BASTANTE SEGURO** | 📅 **Consulte pronto** | 🟠 Naranja |
| **50-69%** | Sistema **SOSPECHA esto** | 🔍 **Haga un chequeo** | 🟡 Amarillo |
| **30-49%** | Sistema **tiene DUDAS** | ℹ️ **Posible problema inicial** | 🔵 Azul |
| **<30%** | Sistema **NO ESTÁ SEGURO** | ✅ **Todo parece normal** | 🟢 Verde |

### ¿Cómo se calcula?

1. **Reglas Crisp**: Cada regla tiene confianza fija (ej: 97% para pulpitis severa)
2. **Reglas Difusas**: Confianza calculada por grados de pertenencia
3. **Sistema de Respaldo**: Confianza dinámica según intensidad de síntomas

**Ejemplo de Cálculo de Respaldo:**

```python
# Si detecta absceso pero no hay regla exacta:
if pus_visible or hinchazon_cara:
    base_conf = 0.70
    
    # Ajustar por intensidad de dolor
    if intensidad_dolor >= 8:
        base_conf += 0.25  # → 95%
    elif intensidad_dolor >= 6:
        base_conf += 0.15  # → 85%
    
    # Ajustar por fiebre
    if fiebre == 'si':
        base_conf += 0.10  # +10%
```

---

## 🎓 Conceptos Técnicos para Defender el Proyecto

### 1. ¿Por qué es un Sistema Experto?

✅ **Características de un Sistema Experto Genuino:**

| Criterio | Cumplimiento | Evidencia |
|----------|--------------|-----------|
| **Base de Conocimientos** | ✅ SÍ | 53 reglas + 30 diagnósticos + recomendaciones |
| **Motor de Inferencia** | ✅ SÍ | Forward Chaining + Lógica Difusa |
| **Explicabilidad** | ✅ SÍ | Muestra qué reglas se activaron y por qué |
| **Separación Conocimiento-Control** | ✅ SÍ | Reglas en archivos separados del motor |
| **Razonamiento Simbólico** | ✅ SÍ | Usa IF-THEN, no solo ML estadístico |
| **Manejo de Incertidumbre** | ✅ SÍ | Lógica difusa + niveles de confianza |

**NO es simplemente:**
- ❌ Un árbol de decisión simple
- ❌ Un chatbot con respuestas predefinidas
- ❌ Machine Learning puro (sin explicabilidad)

**Es un verdadero sistema experto porque:**
> Emula el **razonamiento de un experto odontólogo** usando **reglas explícitas**, **maneja incertidumbre** con lógica difusa, y **explica sus conclusiones** mostrando niveles de confianza y reglas aplicadas.

---

### 2. Forward Chaining vs. Backward Chaining

**¿Por qué usamos Forward Chaining?**

```
FORWARD CHAINING (usado aquí):
Datos (síntomas) → Reglas → Conclusión (diagnóstico)
"Tengo estos síntomas, ¿qué enfermedad podría ser?"

BACKWARD CHAINING (no usado):
Hipótesis (diagnóstico) → Reglas → Validar (síntomas)
"¿Será pulpitis? Veamos si los síntomas coinciden"
```

**Forward Chaining es IDEAL para:**
- ✅ Diagnóstico médico (partimos de síntomas observables)
- ✅ Sistemas exploratorios (no sabemos la conclusión)
- ✅ Múltiples conclusiones posibles

---

### 3. Lógica Crisp vs. Lógica Difusa

| Aspecto | Lógica Crisp | Lógica Difusa |
|---------|--------------|---------------|
| **Valores** | Binarios (0 o 1) | Graduales (0.0 a 1.0) |
| **Ejemplo** | "Dolor SÍ o NO" | "Dolor 70% severo" |
| **Uso** | Síntomas claros | Síntomas ambiguos |
| **Ventaja** | Precisa cuando aplica | Maneja incertidumbre |
| **Reglas** | 53 reglas específicas | Complementarias |

**Ejemplo Comparativo:**

```python
# CRISP (Determinística):
IF dolor >= 8 AND sensibilidad >= 7 AND nocturno >= 7:
    ENTONCES pulpitis con 97% confianza

# DIFUSA (Gradual):
IF dolor es "muy_alto" (grado 0.8) 
   Y sensibilidad es "alta" (grado 0.7):
    ENTONCES pulpitis con 85% confianza
```

**¿Por qué usar ambas?**
> La lógica **crisp** es precisa para casos claros. La lógica **difusa** complementa cuando los síntomas son graduales o ambiguos. Juntas cubren **TODOS los escenarios**.

---

### 4. Resolución de Conflictos

**¿Qué pasa si 5 reglas se activan al mismo tiempo?**

Usamos **3 estrategias**:

1. **highest_confidence**: "Quédate con la regla de mayor confianza"
   - Ventaja: Diagnóstico más seguro
   - Desventaja: Ignora alternativas

2. **most_specific**: "Prefiere la regla con MÁS condiciones"
   - Ventaja: Más precisa (más síntomas considerados)
   - Desventaja: Puede ignorar reglas generales válidas

3. **combine**: "Retorna TODAS, ordenadas por confianza"
   - Ventaja: Diagnóstico principal + alternativos
   - Desventaja: Puede confundir con demasiadas opciones

**Sistema usa `combine` porque:**
> Permite mostrar diagnóstico principal + alternativos, dando **transparencia** al usuario sobre múltiples posibilidades.

---

## 🚀 Ventajas Competitivas del Sistema

### Comparado con sistemas básicos:

| Característica | Sistema Básico | Este Sistema |
|----------------|----------------|--------------|
| **Reglas** | 5-10 reglas genéricas | 53+ reglas específicas |
| **Diagnósticos** | 3-5 condiciones | 30+ condiciones |
| **Confianza** | Fija (siempre 50%) | Dinámica (25%-98%) |
| **Lógica** | Solo crisp | Crisp + Difusa |
| **Respaldo** | "No sé" si no hay regla | Diagnóstico inteligente siempre |
| **Explicabilidad** | Solo muestra resultado | Muestra confianza, urgencia, alternativos |
| **Interfaz** | Formulario simple | GUI profesional con guías |
| **Reportes** | No tiene | PDF profesional |
| **Logging** | No tiene | Logs completos por día |

---

## 📦 Dependencias del Proyecto

```bash
# Instalar con: pip install -r requirements.txt

scikit-fuzzy==0.4.2    # Lógica difusa
numpy==1.24.3          # Cálculos numéricos
reportlab==4.0.7       # Generación PDFs
Pillow==10.1.0         # Procesamiento imágenes
matplotlib==3.8.2      # Gráficos (opcional)
python-dateutil==2.8.2 # Manejo fechas

# tkinter viene con Python, no requiere instalación
```

---

## 🎯 Casos de Uso Reales

### Caso 1: Emergencia Médica

**Entrada:**
- Hinchazón facial: Sí
- Fiebre: Sí
- Dolor: 9/10
- Mal aliento: Severo

**Proceso:**
1. Regla `rule_celulitis_facial` se activa → 98% confianza
2. Sistema de urgencia → "URGENTE"
3. Banner rojo: "🚨 ATENCIÓN URGENTE REQUERIDA"

**Salida:**
- Diagnóstico: **Celulitis Facial**
- Confianza: **98%**
- Urgencia: **URGENTE**
- Acción: **IR A EMERGENCIAS INMEDIATAMENTE**

---

### Caso 2: Caries Inicial

**Entrada:**
- Mancha oscura: Sí
- Sensibilidad al frío: 4/10
- Dolor: 3/10
- Sensibilidad dulce: 5/10

**Proceso:**
1. Regla `rule_caries_inicial_1` se activa → 75% confianza
2. Sistema de urgencia → "moderada"
3. Banner amarillo: "📅 Agende una cita odontológica"

**Salida:**
- Diagnóstico: **Caries Inicial**
- Confianza: **75%**
- Urgencia: **Moderada**
- Acción: **Agende cita con dentista**

---

### Caso 3: Sin Síntomas Claros

**Entrada:**
- Sensibilidad leve al frío: 3/10
- Dolor: 2/10
- Todo lo demás: No/Normal

**Proceso:**
1. Ninguna regla crisp se activa
2. Sistema de respaldo analiza síntomas
3. Detecta síntomas mínimos → Evaluación general
4. Confianza baja: 28%

**Salida:**
- Diagnóstico: **Evaluación General Recomendada**
- Confianza: **28%**
- Urgencia: **Baja**
- Acción: **Consulta preventiva (no urgente)**

---

## 🛡️ Limitaciones y Disclaimer

### Limitaciones Técnicas:

1. **NO reemplaza a un odontólogo profesional**
   - Es una herramienta de **apoyo diagnóstico**
   - Diagnóstico final debe ser por profesional

2. **Basado en síntomas autoreportados**
   - Depende de la **precisión del usuario**
   - No incluye exámenes radiológicos

3. **Conocimiento limitado a reglas predefinidas**
   - No "aprende" de casos nuevos (no es ML adaptativo)
   - Requiere actualización manual de reglas

### Fortalezas:

1. ✅ **Alta cobertura** (53 reglas, 30 diagnósticos)
2. ✅ **Explicable** (muestra por qué llegó a una conclusión)
3. ✅ **Consistente** (mismo síntoma = mismo diagnóstico)
4. ✅ **Transparente** (niveles de confianza claros)

---

## 📝 Conclusión

Este **Sistema Experto de Odontología** es una aplicación completa que:

✅ Implementa **verdadera inteligencia artificial simbólica** (no solo estadística)  
✅ Usa **53+ reglas expertas** en 9 categorías de diagnósticos  
✅ Maneja **incertidumbre** con lógica crisp y difusa  
✅ Proporciona **diagnósticos explicables** con niveles de confianza  
✅ Ofrece **interfaz profesional** intuitiva y accesible  
✅ Genera **reportes PDF** para documentación  
✅ Mantiene **logs auditables** de todas las operaciones  

**Es un ejemplo perfecto de:**
- 🧠 Sistema Experto basado en reglas
- ⚙️ Forward Chaining para diagnóstico
- 🌫️ Lógica Difusa para incertidumbre
- 🖥️ Interfaz gráfica profesional
- 📊 Razonamiento con confianza variable

---

## 🎤 Puntos Clave para la Exposición

### 1. Introducción (2 min)
> "Desarrollé un Sistema Experto de Odontología que emula el razonamiento de un odontólogo profesional usando 53 reglas específicas para diagnosticar 30 condiciones dentales diferentes."

### 2. Arquitectura (3 min)
> "El sistema tiene 4 módulos principales:
> - **Base de Conocimientos**: 53 reglas + 30 diagnósticos + recomendaciones
> - **Motor de Inferencia**: Forward Chaining + Lógica Difusa
> - **Interfaz Gráfica**: Tkinter con formularios interactivos
> - **Utilidades**: Reportes PDF + Sistema de Logging"

### 3. Innovación Técnica (3 min)
> "A diferencia de sistemas básicos que siempre retornan 50% de confianza, este sistema:
> - Calcula confianza **dinámica** entre 25% y 98%
> - Combina **lógica crisp** (precisa) con **lógica difusa** (ambigua)
> - Genera **diagnóstico inteligente** incluso sin reglas exactas
> - Muestra **diagnósticos alternativos** para transparencia"

### 4. Demostración (5 min)
> [Mostrar interfaz]
> - Ingresar síntomas de pulpitis severa
> - Ver diagnóstico con 97% confianza
> - Mostrar guía de niveles de confianza
> - Generar PDF del reporte

### 5. Validación (2 min)
> "El sistema fue probado con múltiples casos:
> - Emergencias (celulitis) → 98% confianza, urgencia máxima
> - Caries profunda → 92% confianza, urgencia alta
> - Sensibilidad leve → 72% confianza, urgencia baja
> - Sin síntomas → 25% confianza, evaluación general"

### 6. Conclusión (1 min)
> "Este es un verdadero sistema experto porque:
> - Separa **conocimiento** (reglas) de **control** (motor)
> - Usa **razonamiento simbólico** explícito
> - Maneja **incertidumbre** con lógica difusa
> - Es **explicable** (muestra por qué diagnostica)
> - No solo predice, **RAZONA** como un experto."

---

**Fecha de Documentación**: 18 de Noviembre, 2025  
**Versión del Sistema**: 1.0  
**Autor**: Sistema Experto de Odontología  
**Tecnología**: Python 3.14 + Tkinter + scikit-fuzzy + ReportLab
