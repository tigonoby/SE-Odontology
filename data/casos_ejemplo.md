# Casos de Ejemplo - Sistema Experto de Odontología

Este archivo contiene casos de ejemplo para probar el sistema.

## Caso 1: Caries Dental Temprana

**Paciente**: María González, 28 años

**Síntomas Reportados**:
- Dolor agudo al consumir alimentos dulces
- Sensibilidad al frío moderada
- Mancha oscura visible en molar
- Dolor leve al masticar (3/10)
- Duración: 2 días

**Valores en el Sistema**:
```
tipo_dolor: agudo
intensidad_dolor: 5
duracion_dolor: 1_3_dias
sensibilidad_frio: 6
sensibilidad_calor: 2
sensibilidad_dulce: 8
dolor_masticar: 3
caries_visible: si
mancha_oscura: si
```

**Diagnóstico Esperado**: Caries Dental
**Recomendación**: Agendar cita con odontólogo pronto

---

## Caso 2: Pulpitis Aguda

**Paciente**: Carlos Ramírez, 35 años

**Síntomas Reportados**:
- Dolor pulsante severo que no cede
- Dolor intenso por las noches (no puede dormir)
- Sensibilidad extrema al calor
- El dolor aparece espontáneamente
- Duración: 5 días

**Valores en el Sistema**:
```
tipo_dolor: pulsante
intensidad_dolor: 9
duracion_dolor: 3_7_dias
sensibilidad_frio: 6
sensibilidad_calor: 9
dolor_nocturno: 9
dolor_presion: 7
```

**Diagnóstico Esperado**: Pulpitis
**Recomendación**: URGENTE - Consultar odontólogo inmediatamente

---

## Caso 3: Absceso Dental

**Paciente**: Ana Torres, 42 años

**Síntomas Reportados**:
- Dolor severo constante
- Hinchazón visible en mejilla
- Pus drenando de la encía
- Fiebre de 38.5°C
- Mal aliento intenso
- No puede masticar del lado afectado
- Duración: 10 días

**Valores en el Sistema**:
```
tipo_dolor: pulsante
intensidad_dolor: 10
duracion_dolor: mas_7_dias
dolor_presion: 10
dolor_masticar: 9
inflamacion_encias: 8
hinchazon_cara: si
pus_visible: si
fiebre: si
mal_aliento: severo
sangrado_encias: moderado
```

**Diagnóstico Esperado**: Absceso Dental
**Recomendación**: ¡EMERGENCIA! Buscar atención odontológica de emergencia

---

## Caso 4: Gingivitis

**Paciente**: Luis Mendoza, 30 años

**Síntomas Reportados**:
- Sangrado de encías al cepillar
- Encías rojas e inflamadas
- Mal aliento leve
- Dolor leve o molestia
- No hay movilidad dental
- Duración: 2 semanas

**Valores en el Sistema**:
```
tipo_dolor: sordo
intensidad_dolor: 3
duracion_dolor: mas_7_dias
inflamacion_encias: 6
sangrado_encias: moderado
color_encias: rojo_claro
mal_aliento: leve
movilidad_dental: no
```

**Diagnóstico Esperado**: Gingivitis
**Recomendación**: Agendar limpieza dental profesional

---

## Caso 5: Sensibilidad Dental

**Paciente**: Patricia Ruiz, 25 años

**Síntomas Reportados**:
- Dolor breve y agudo al tomar bebidas frías
- También molestia con aire frío
- El dolor desaparece rápidamente
- No hay caries visibles
- Retraimiento leve de encías
- Duración: ocasional desde hace 1 mes

**Valores en el Sistema**:
```
tipo_dolor: agudo
intensidad_dolor: 4
duracion_dolor: menos_24h
sensibilidad_frio: 8
sensibilidad_calor: 1
caries_visible: no
retraimiento_encias: leve
desgaste_dental: leve
inflamacion_encias: 1
```

**Diagnóstico Esperado**: Sensibilidad Dental
**Recomendación**: Usar pasta para dientes sensibles, consultar si persiste

---

## Caso 6: Periodontitis

**Paciente**: Roberto Díaz, 50 años

**Síntomas Reportados**:
- Encías muy retraídas
- Sangrado frecuente
- Movilidad en varios dientes
- Mal aliento persistente
- Dolor moderado al masticar
- Duración: varios meses

**Valores en el Sistema**:
```
tipo_dolor: sordo
intensidad_dolor: 4
duracion_dolor: mas_7_dias
inflamacion_encias: 7
sangrado_encias: severo
retraimiento_encias: severo
movilidad_dental: moderado
mal_aliento: severo
color_encias: rojo_intenso
```

**Diagnóstico Esperado**: Periodontitis
**Recomendación**: Consultar periodoncista urgentemente

---

## Caso 7: Bruxismo

**Paciente**: Sofía Vargas, 32 años

**Síntomas Reportados**:
- Dolor mandibular al despertar
- Pareja reporta que rechina dientes por la noche
- Desgaste visible en dientes frontales
- Dolor de cabeza frecuente
- Sensibilidad dental leve
- Duración: 6 meses

**Valores en el Sistema**:
```
tipo_dolor: sordo
intensidad_dolor: 5
duracion_dolor: mas_7_dias
dolor_mandibula: 7
rechinar_dientes: si
desgaste_dental: moderado
sensibilidad_frio: 4
dolor_nocturno: 3
```

**Diagnóstico Esperado**: Bruxismo
**Recomendación**: Consultar para férula de descarga

---

## Caso 8: Problema de Ortodoncia

**Paciente**: Miguel Ángel, 16 años

**Síntomas Reportados**:
- Dificultad al morder
- Dolor al masticar ciertos alimentos
- Dolor de mandíbula después de comer
- Dientes visiblemente desalineados
- Sin otros síntomas significativos

**Valores en el Sistema**:
```
tipo_dolor: sordo
intensidad_dolor: 4
dolor_masticar: 6
dolor_mandibula: 5
problemas_mordida: si
todos_los_demas: valores_bajos_o_no
```

**Diagnóstico Esperado**: Problema de Ortodoncia
**Recomendación**: Consultar ortodoncista para evaluación

---

## Notas de Uso

1. **Estos casos son referenciales**: Basados en situaciones clínicas típicas
2. **Variabilidad individual**: Los síntomas pueden variar entre personas
3. **Múltiples diagnósticos**: Algunos casos pueden tener diagnósticos combinados
4. **Sistema de apoyo**: Recuerde que el sistema es solo orientativo

## Probar los Casos

Para probar estos casos en el sistema:
1. Ejecutar la aplicación
2. Ingresar los valores especificados
3. Hacer clic en "Diagnosticar"
4. Comparar con el diagnóstico esperado
5. Generar reporte PDF si se desea

---

© 2025 - Sistema Experto de Odontología
