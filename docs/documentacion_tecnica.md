# Documentación del Sistema Experto de Odontología

## Índice
1. [Arquitectura del Sistema](#arquitectura)
2. [Base de Conocimientos](#base-de-conocimientos)
3. [Motor de Inferencia](#motor-de-inferencia)
4. [Lógica Difusa](#logica-difusa)
5. [Interfaz Gráfica](#interfaz-grafica)
6. [Guía de Usuario](#guia-de-usuario)

---

## Arquitectura

El sistema está organizado en módulos independientes:

```
src/
├── knowledge_base/      # Base de conocimientos
│   ├── facts.py        # Hechos y síntomas
│   ├── crisp_rules.py  # Reglas determinísticas
│   └── fuzzy_rules.py  # Reglas difusas
│
├── inference_engine/    # Motor de inferencia
│   ├── forward_chaining.py
│   ├── fuzzy_logic.py
│   └── diagnosis.py
│
├── gui/                 # Interfaz gráfica
│   ├── main_window.py
│   ├── symptoms_panel.py
│   └── results_panel.py
│
└── utils/              # Utilidades
    ├── logger.py
    └── report_generator.py
```

---

## Base de Conocimientos

### Síntomas Evaluados

El sistema evalúa los siguientes tipos de síntomas:

1. **Dolor**:
   - Tipo (agudo, punzante, constante, pulsante, sordo, intermitente)
   - Intensidad (0-10)
   - Duración (menos de 24h, 1-3 días, 3-7 días, más de 7 días)

2. **Sensibilidad**:
   - Al frío (0-10)
   - Al calor (0-10)
   - Al dulce (0-10)

3. **Dolor Específico**:
   - Al masticar (0-10)
   - A la presión (0-10)
   - Nocturno (0-10)
   - Mandibular (0-10)

4. **Encías**:
   - Inflamación (0-10)
   - Sangrado (no, leve, moderado, severo)
   - Color (normal, rojo claro, rojo intenso, púrpura)
   - Retraimiento (no, leve, moderado, severo)

5. **Observaciones Visuales**:
   - Caries visible
   - Manchas oscuras
   - Fracturas
   - Desgaste dental

6. **Signos de Infección**:
   - Hinchazón facial
   - Pus visible
   - Fiebre
   - Mal aliento

### Diagnósticos Soportados

1. **Caries Dental**: Deterioro del esmalte y dentina
2. **Pulpitis**: Inflamación de la pulpa dental
3. **Absceso Dental**: Infección con acumulación de pus
4. **Sensibilidad Dental**: Hipersensibilidad dentinaria
5. **Gingivitis**: Inflamación de las encías
6. **Periodontitis**: Enfermedad periodontal avanzada
7. **Bruxismo**: Rechinamiento de dientes
8. **Problema de Ortodoncia**: Maloclusión

---

## Motor de Inferencia

### Encadenamiento Hacia Adelante

El sistema utiliza forward chaining:
1. Se ingresan los síntomas (hechos iniciales)
2. Se evalúan todas las reglas
3. Se activan las reglas cuyas condiciones se cumplen
4. Se generan conclusiones (diagnósticos)

### Resolución de Conflictos

Cuando múltiples reglas se activan, el sistema usa:
- **Combinación de evidencia**: Agrupa diagnósticos iguales
- **Mayor confianza**: Prioriza reglas con alta confianza
- **Más específicas**: Favorece reglas con más condiciones

---

## Lógica Difusa

### Variables Difusas

1. **Intensidad del Dolor**:
   - Bajo: 0-4
   - Medio: 2-8
   - Alto: 6-10

2. **Sensibilidad**:
   - Baja: 0-4
   - Media: 2-8
   - Alta: 6-10

3. **Inflamación**:
   - Baja: 0-4
   - Media: 2-8
   - Alta: 6-10

### Funciones de Pertenencia

Se utilizan funciones triangulares y trapezoidales para modelar la ambigüedad en los síntomas.

### Reglas Difusas Ejemplo

```
SI intensidad_dolor es ALTA Y sensibilidad es ALTA 
ENTONCES probabilidad_pulpitis es ALTA

SI sensibilidad es ALTA Y intensidad_dolor es MEDIA 
ENTONCES probabilidad_caries es MEDIA
```

---

## Interfaz Gráfica

### Componentes Principales

1. **Panel de Síntomas** (Izquierda):
   - Escalas deslizantes para valores numéricos
   - Menús desplegables para opciones categóricas
   - Botones de radio para opciones binarias

2. **Panel de Resultados** (Derecha):
   - Diagnóstico principal con confianza
   - Nivel de urgencia
   - Recomendaciones
   - Diagnósticos alternativos

3. **Barra de Menú**:
   - Archivo: Nuevo, Guardar PDF, Salir
   - Edición: Limpiar formulario
   - Ayuda: Acerca de, Manual

---

## Guía de Usuario

### Paso 1: Ingresar Síntomas

1. Complete todos los campos relevantes en el panel izquierdo
2. Use las escalas para valores numéricos (0 = ninguno, 10 = máximo)
3. Seleccione opciones en los menús desplegables
4. Sea lo más preciso posible

### Paso 2: Realizar Diagnóstico

1. Haga clic en el botón "Diagnosticar"
2. El sistema procesará los síntomas
3. Los resultados aparecerán en el panel derecho

### Paso 3: Revisar Resultados

1. Lea el diagnóstico principal
2. Verifique el nivel de confianza
3. Preste atención al nivel de urgencia:
   - 🚨 URGENTE: Busque atención inmediata
   - ⚠️ ALTA: Consulte pronto
   - 📅 MODERADA: Agende cita
   - ℹ️ BAJA: Considere evaluación

4. Lea todas las recomendaciones

### Paso 4: Guardar Reporte

1. Haga clic en "Guardar PDF"
2. Seleccione ubicación de guardado
3. El reporte incluye:
   - Diagnóstico completo
   - Síntomas reportados
   - Recomendaciones
   - Información del sistema

### Paso 5: Nuevo Diagnóstico

1. Use "Limpiar" para resetear
2. Ingrese nuevo nombre de paciente si es necesario
3. Repita el proceso

---

## Advertencias Importantes

⚠️ **ESTE SISTEMA ES SOLO PARA ORIENTACIÓN PRELIMINAR**

- NO reemplaza consulta con odontólogo profesional
- NO use para autodiagnóstico definitivo
- SIEMPRE consulte con un profesional certificado
- Use solo como guía para priorizar atención

---

## Casos de Uso Típicos

### Caso 1: Dolor Agudo Reciente
**Síntomas**: Dolor agudo al tomar bebidas frías
**Proceso**: 
1. Intensidad dolor: 6
2. Sensibilidad frío: 8
3. Duración: menos 24h
**Resultado probable**: Sensibilidad dental o caries inicial

### Caso 2: Dolor Severo Prolongado
**Síntomas**: Dolor pulsante intenso, no duerme
**Proceso**:
1. Intensidad dolor: 9
2. Dolor nocturno: 9
3. Duración: más de 7 días
**Resultado probable**: Pulpitis o absceso

### Caso 3: Sangrado de Encías
**Síntomas**: Sangrado al cepillar, sin dolor fuerte
**Proceso**:
1. Sangrado: moderado
2. Inflamación encías: 6
3. Intensidad dolor: 3
**Resultado probable**: Gingivitis

---

## Mantenimiento y Actualización

### Agregar Nuevos Diagnósticos

1. Editar `src/knowledge_base/facts.py`:
   - Agregar diagnóstico a `DIAGNOSTICOS`
   - Agregar recomendaciones a `RECOMENDACIONES`

2. Crear reglas en `src/knowledge_base/crisp_rules.py`:
   ```python
   def rule_nuevo_diagnostico(facts):
       conditions = [...]
       return Rule(...)
   ```

3. Agregar reglas difusas si es necesario en `fuzzy_rules.py`

### Modificar Síntomas

1. Editar `SINTOMAS` en `facts.py`
2. Actualizar `symptoms_panel.py` para agregar widgets
3. Actualizar reglas que usen el nuevo síntoma

---

## Soporte Técnico

Para problemas o preguntas:
1. Revisar este documento
2. Consultar logs en `logs/`
3. Verificar casos de prueba en `tests/`
4. Contactar al desarrollador

---

© 2025 - Sistema Experto de Odontología - Proyecto Educativo
