# 🦷 Guía de Inicio Rápido

## ¡Bienvenido al Sistema Experto de Odontología!

Esta guía te ayudará a instalar y usar el sistema en menos de 5 minutos.

---

## 📋 Requisitos Previos

- ✅ Python 3.8 o superior instalado
- ✅ PowerShell o Terminal
- ✅ 100 MB de espacio libre

**¿No tienes Python?** Descárgalo de: https://www.python.org/downloads/

---

## 🚀 Instalación Rápida (3 pasos)

### Paso 1: Abrir PowerShell en el directorio del proyecto

```powershell
cd "C:\Proyecto Universidad\Odontologia-proyect"
```

### Paso 2: Instalar dependencias

```powershell
pip install -r requirements.txt
```

⏱️ Esto tomará 1-2 minutos.

### Paso 3: Ejecutar la aplicación

```powershell
python src/main.py
```

🎉 **¡Listo!** La aplicación debería abrirse.

---

## 📱 Primer Uso - Tutorial Rápido

### Pantalla Principal

```
┌─────────────────────────────────────────────────────────────────┐
│ 🦷 Sistema Experto de Odontología                               │
│                                    Nombre del Paciente: [____]  │
├─────────────────────────┬───────────────────────────────────────┤
│                         │                                       │
│  SÍNTOMAS               │        RESULTADOS                     │
│  (Panel Izquierdo)      │      (Panel Derecho)                 │
│                         │                                       │
│  • Tipo de Dolor        │   "Ingrese síntomas y presione      │
│  • Intensidad (0-10)    │    Diagnosticar..."                  │
│  • Sensibilidad         │                                       │
│  • Estado Encías        │                                       │
│  • Observaciones        │                                       │
│  • Signos Infección     │                                       │
│                         │                                       │
├─────────────────────────┴───────────────────────────────────────┤
│         [🔍 Diagnosticar]  [🗑️ Limpiar]  [📄 Guardar PDF]      │
└─────────────────────────────────────────────────────────────────┘
```

### Ejemplo Paso a Paso: Diagnóstico de Caries

#### 1️⃣ Ingresar Síntomas

En el panel izquierdo, configure:

```
📊 DOLOR
├─ Tipo de Dolor: Agudo
├─ Intensidad: [■■■■■□□□□□] 5/10
└─ Duración: 1-3 días

🌡️ SENSIBILIDAD
├─ Al Frío: [■■■■■■□□□□] 6/10
├─ Al Calor: [■■□□□□□□□□] 2/10
└─ Al Dulce: [■■■■■■■■□□] 8/10

🦷 OBSERVACIONES
├─ ¿Caries Visible?: ● Sí ○ No
└─ ¿Mancha Oscura?: ● Sí ○ No
```

#### 2️⃣ Hacer Clic en "Diagnosticar"

#### 3️⃣ Ver Resultados

El panel derecho mostrará:

```
┌─────────────────────────────────────────────┐
│ 📅 AGENDE UNA CITA ODONTOLÓGICA             │
└─────────────────────────────────────────────┘

DIAGNÓSTICO PRINCIPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🦷 Caries Dental

Confianza: 90%
[■■■■■■■■■□] 

Descripción: Deterioro del esmalte y dentina 
causado por ácidos bacterianos

Gravedad: MEDIA | Urgencia: MODERADA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMENDACIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Agende una cita con su odontólogo lo antes posible
2. Evite alimentos y bebidas azucaradas
3. Mantenga una higiene oral rigurosa
4. Use hilo dental diariamente
5. Enjuague con agua tibia con sal si hay molestias
```

#### 4️⃣ Guardar Reporte (Opcional)

Click en **"Guardar PDF"** para generar un reporte completo.

---

## 🎯 Casos de Ejemplo Rápidos

### Caso 1: Dolor Leve por Frío
```
Síntomas clave:
├─ Sensibilidad al frío: 7/10
├─ Intensidad dolor: 4/10
└─ Caries visible: No

Resultado: Sensibilidad Dental
```

### Caso 2: Dolor Severo Nocturno
```
Síntomas clave:
├─ Intensidad dolor: 9/10
├─ Dolor nocturno: 9/10
└─ Tipo: Pulsante

Resultado: Pulpitis (¡URGENTE!)
```

### Caso 3: Hinchazón y Fiebre
```
Síntomas clave:
├─ Hinchazón cara: Sí
├─ Pus visible: Sí
├─ Fiebre: Sí
└─ Intensidad dolor: 10/10

Resultado: Absceso (¡EMERGENCIA!)
```

### Caso 4: Sangrado de Encías
```
Síntomas clave:
├─ Sangrado encías: Moderado
├─ Inflamación: 6/10
└─ Color encías: Rojo claro

Resultado: Gingivitis
```

---

## 🎨 Uso de Controles

### Escalas Deslizantes (0-10)
```
Intensidad: [━━━━━━━━━━━━━━━] 
             0     5      10
             │     │       │
           Ninguna Media  Máxima
```
Arrastre el control o haga clic en la posición deseada.

### Menús Desplegables
```
Tipo de Dolor: [Agudo      ▼]
                ├─ Agudo
                ├─ Punzante
                ├─ Constante
                ├─ Pulsante
                ├─ Sordo
                └─ Intermitente
```

### Botones de Radio
```
¿Caries Visible?
● Sí
○ No
○ No estoy seguro
```

---

## 📊 Interpretación de Resultados

### Niveles de Confianza

```
90-100% → ■■■■■■■■■■  Muy Alta Confianza
70-89%  → ■■■■■■■□□□  Alta Confianza
50-69%  → ■■■■■□□□□□  Confianza Media
30-49%  → ■■■□□□□□□□  Confianza Baja
```

### Niveles de Urgencia

```
🚨 URGENTE     → Busque atención INMEDIATA
⚠️ ALTA        → Consulte en 24-48 horas
📅 MODERADA    → Agende cita esta semana
ℹ️ BAJA        → Considere evaluación próximamente
```

---

## 💾 Generar Reporte PDF

1. Complete el diagnóstico
2. Click en **"Guardar PDF"**
3. Seleccione ubicación
4. El PDF incluye:
   - ✅ Diagnóstico completo
   - ✅ Todos los síntomas
   - ✅ Recomendaciones
   - ✅ Información técnica
   - ✅ Advertencias legales

---

## 🔄 Nuevo Diagnóstico

Para otro paciente:

1. Click en **"Limpiar"**
2. Cambie nombre del paciente
3. Ingrese nuevos síntomas
4. Repita el proceso

---

## ⚠️ Advertencias Importantes

```
┌─────────────────────────────────────────────────────┐
│  ⚠️  ESTE SISTEMA ES SOLO PARA ORIENTACIÓN         │
│                                                     │
│  ❌ NO reemplaza consulta médica profesional       │
│  ❌ NO use para autodiagnóstico definitivo         │
│  ✅ SIEMPRE consulte con un odontólogo certificado │
└─────────────────────────────────────────────────────┘
```

---

## 🆘 Solución Rápida de Problemas

### ❌ Error: "No module named 'tkinter'"
```powershell
# Windows: Reinstalar Python con tcl/tk
# Linux:
sudo apt-get install python3-tk
```

### ❌ Error: "No module named 'skfuzzy'"
```powershell
pip install scikit-fuzzy
```

### ❌ La ventana no abre
```powershell
# Verificar errores:
python src/main.py
# Leer mensajes en consola
```

### ❌ Error al guardar PDF
```powershell
pip install --upgrade reportlab
```

---

## 📚 Más Información

- **Manual completo**: `docs/INSTALACION.md`
- **Documentación técnica**: `docs/documentacion_tecnica.md`
- **Casos de ejemplo**: `data/casos_ejemplo.md`
- **Estructura del proyecto**: `ESTRUCTURA.md`

---

## 🎓 Para Evaluación Académica

### Demostrar Funcionamiento

1. **Caso Simple**: Caries con síntomas claros
2. **Caso Complejo**: Múltiples diagnósticos posibles
3. **Caso Urgente**: Absceso con necesidad de atención inmediata
4. **Generar PDF**: Mostrar reporte profesional
5. **Ver Logs**: Mostrar registro de actividad en `logs/`

### Aspectos Técnicos a Destacar

- ✅ Base de conocimientos con 14+ reglas crisp
- ✅ Lógica difusa para síntomas ambiguos
- ✅ Motor de inferencia con forward chaining
- ✅ Resolución de conflictos
- ✅ Interfaz gráfica intuitiva
- ✅ Generación de reportes PDF
- ✅ Sistema de logging
- ✅ Casos de prueba validados

---

## 📞 Soporte

¿Problemas o dudas?

1. Revisar `docs/INSTALACION.md`
2. Consultar logs en `logs/sistema_*.log`
3. Ejecutar pruebas: `python tests/test_diagnosis.py`
4. Contactar al desarrollador

---

## ✨ ¡Comienza Ahora!

```powershell
# Un solo comando para empezar:
cd "C:\Proyecto Universidad\Odontologia-proyect" ; python src/main.py
```

**¡Disfruta usando el Sistema Experto de Odontología!** 🦷

---

© 2025 - Proyecto Universidad - Sistemas Expertos
