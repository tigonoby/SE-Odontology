# Casos de Prueba del Sistema Experto de Odontología

Este directorio contiene casos de prueba para validar el funcionamiento del sistema experto.

## Casos de Prueba Implementados

### 1. test_diagnosis.py
Pruebas unitarias para el motor de diagnóstico:

- **test_caries_diagnosis()**: Valida diagnóstico de caries dental
  - Síntomas: dolor agudo, sensibilidad al frío y dulce, caries visible
  - Resultado esperado: Diagnóstico de caries con alta confianza

- **test_pulpitis_diagnosis()**: Valida diagnóstico de pulpitis
  - Síntomas: dolor pulsante intenso, sensibilidad al calor, dolor nocturno
  - Resultado esperado: Diagnóstico de pulpitis con alta confianza

- **test_absceso_diagnosis()**: Valida diagnóstico de absceso dental
  - Síntomas: dolor severo, hinchazón facial, pus visible, fiebre
  - Resultado esperado: Diagnóstico de absceso con urgencia alta

- **test_gingivitis_diagnosis()**: Valida diagnóstico de gingivitis
  - Síntomas: sangrado de encías, inflamación, dolor leve
  - Resultado esperado: Diagnóstico de gingivitis

- **test_sensibilidad_diagnosis()**: Valida diagnóstico de sensibilidad dental
  - Síntomas: sensibilidad al frío, sin caries visible, retraimiento leve
  - Resultado esperado: Diagnóstico de sensibilidad dental

## Ejecutar las Pruebas

```bash
# Ejecutar todas las pruebas
python tests/test_diagnosis.py

# Ejecutar con pytest (si está instalado)
pytest tests/

# Ejecutar con cobertura
pytest --cov=src tests/
```

## Resultados Esperados

Todas las pruebas deberían pasar exitosamente, indicando que:
- El motor de inferencia funciona correctamente
- Las reglas crisp se aplican adecuadamente
- La lógica difusa complementa el diagnóstico
- El sistema puede identificar múltiples condiciones odontológicas

## Agregar Nuevas Pruebas

Para agregar nuevas pruebas:

1. Crear una función de prueba siguiendo el patrón:
```python
def test_nueva_condicion():
    """Descripción de la prueba"""
    engine = DiagnosisEngine()
    symptoms = { ... }  # Definir síntomas
    result = engine.diagnose(symptoms)
    assert ...  # Validaciones
```

2. Agregar la prueba a `run_all_tests()`

3. Documentar el caso de prueba en este README
