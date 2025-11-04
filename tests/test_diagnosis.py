"""
Pruebas Unitarias para el Motor de Inferencia
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.inference_engine import DiagnosisEngine


def test_caries_diagnosis():
    """Prueba diagnóstico de caries"""
    print("=== Test: Diagnóstico de Caries ===")
    
    engine = DiagnosisEngine()
    
    symptoms = {
        'tipo_dolor': 'agudo',
        'intensidad_dolor': 5,
        'duracion_dolor': '1_3_dias',
        'sensibilidad_frio': 7,
        'sensibilidad_calor': 3,
        'sensibilidad_dulce': 8,
        'dolor_masticar': 4,
        'dolor_presion': 3,
        'dolor_nocturno': 2,
        'inflamacion_encias': 1,
        'sangrado_encias': 'no',
        'color_encias': 'normal',
        'retraimiento_encias': 'no',
        'caries_visible': 'si',
        'mancha_oscura': 'si',
        'fractura_diente': 'no',
        'desgaste_dental': 'no',
        'hinchazon_cara': 'no',
        'pus_visible': 'no',
        'mal_aliento': 'no',
        'fiebre': 'no',
        'movilidad_dental': 'no',
        'rechinar_dientes': 'no',
        'dolor_mandibula': 0,
        'problemas_mordida': 'no',
        'tratamiento_reciente': 'no',
        'trauma_reciente': 'no'
    }
    
    result = engine.diagnose(symptoms)
    
    print(f"Diagnósticos encontrados: {result['num_diagnosticos']}")
    if result['principal']:
        print(f"Principal: {result['principal']['nombre']}")
        print(f"Confianza: {result['principal']['confianza_porcentaje']}%")
    
    assert result['num_diagnosticos'] > 0, "Debería encontrar al menos un diagnóstico"
    print("✓ Test pasado\n")


def test_pulpitis_diagnosis():
    """Prueba diagnóstico de pulpitis"""
    print("=== Test: Diagnóstico de Pulpitis ===")
    
    engine = DiagnosisEngine()
    
    symptoms = {
        'tipo_dolor': 'pulsante',
        'intensidad_dolor': 8,
        'duracion_dolor': '3_7_dias',
        'sensibilidad_frio': 5,
        'sensibilidad_calor': 8,
        'sensibilidad_dulce': 6,
        'dolor_masticar': 6,
        'dolor_presion': 7,
        'dolor_nocturno': 9,
        'inflamacion_encias': 2,
        'sangrado_encias': 'no',
        'color_encias': 'normal',
        'retraimiento_encias': 'no',
        'caries_visible': 'no_seguro',
        'mancha_oscura': 'no',
        'fractura_diente': 'no',
        'desgaste_dental': 'no',
        'hinchazon_cara': 'no',
        'pus_visible': 'no',
        'mal_aliento': 'leve',
        'fiebre': 'no',
        'movilidad_dental': 'no',
        'rechinar_dientes': 'no',
        'dolor_mandibula': 0,
        'problemas_mordida': 'no',
        'tratamiento_reciente': 'no',
        'trauma_reciente': 'no'
    }
    
    result = engine.diagnose(symptoms)
    
    print(f"Diagnósticos encontrados: {result['num_diagnosticos']}")
    if result['principal']:
        print(f"Principal: {result['principal']['nombre']}")
        print(f"Confianza: {result['principal']['confianza_porcentaje']}%")
    
    assert result['num_diagnosticos'] > 0, "Debería encontrar al menos un diagnóstico"
    print("✓ Test pasado\n")


def test_absceso_diagnosis():
    """Prueba diagnóstico de absceso"""
    print("=== Test: Diagnóstico de Absceso ===")
    
    engine = DiagnosisEngine()
    
    symptoms = {
        'tipo_dolor': 'pulsante',
        'intensidad_dolor': 9,
        'duracion_dolor': 'mas_7_dias',
        'sensibilidad_frio': 4,
        'sensibilidad_calor': 7,
        'sensibilidad_dulce': 3,
        'dolor_masticar': 8,
        'dolor_presion': 9,
        'dolor_nocturno': 8,
        'inflamacion_encias': 7,
        'sangrado_encias': 'moderado',
        'color_encias': 'rojo_intenso',
        'retraimiento_encias': 'no',
        'caries_visible': 'si',
        'mancha_oscura': 'si',
        'fractura_diente': 'no',
        'desgaste_dental': 'no',
        'hinchazon_cara': 'si',
        'pus_visible': 'si',
        'mal_aliento': 'severo',
        'fiebre': 'si',
        'movilidad_dental': 'leve',
        'rechinar_dientes': 'no',
        'dolor_mandibula': 6,
        'problemas_mordida': 'no',
        'tratamiento_reciente': 'no',
        'trauma_reciente': 'no'
    }
    
    result = engine.diagnose(symptoms)
    
    print(f"Diagnósticos encontrados: {result['num_diagnosticos']}")
    if result['principal']:
        print(f"Principal: {result['principal']['nombre']}")
        print(f"Confianza: {result['principal']['confianza_porcentaje']}%")
        print(f"Urgencia: {result['principal']['urgencia']}")
    
    assert result['num_diagnosticos'] > 0, "Debería encontrar al menos un diagnóstico"
    assert result['principal']['urgencia'] in ['urgente', 'alta'], "Debería ser urgente"
    print("✓ Test pasado\n")


def test_gingivitis_diagnosis():
    """Prueba diagnóstico de gingivitis"""
    print("=== Test: Diagnóstico de Gingivitis ===")
    
    engine = DiagnosisEngine()
    
    symptoms = {
        'tipo_dolor': 'sordo',
        'intensidad_dolor': 3,
        'duracion_dolor': '3_7_dias',
        'sensibilidad_frio': 2,
        'sensibilidad_calor': 1,
        'sensibilidad_dulce': 1,
        'dolor_masticar': 2,
        'dolor_presion': 2,
        'dolor_nocturno': 1,
        'inflamacion_encias': 6,
        'sangrado_encias': 'moderado',
        'color_encias': 'rojo_claro',
        'retraimiento_encias': 'no',
        'caries_visible': 'no',
        'mancha_oscura': 'no',
        'fractura_diente': 'no',
        'desgaste_dental': 'no',
        'hinchazon_cara': 'no',
        'pus_visible': 'no',
        'mal_aliento': 'leve',
        'fiebre': 'no',
        'movilidad_dental': 'no',
        'rechinar_dientes': 'no',
        'dolor_mandibula': 0,
        'problemas_mordida': 'no',
        'tratamiento_reciente': 'no',
        'trauma_reciente': 'no'
    }
    
    result = engine.diagnose(symptoms)
    
    print(f"Diagnósticos encontrados: {result['num_diagnosticos']}")
    if result['principal']:
        print(f"Principal: {result['principal']['nombre']}")
        print(f"Confianza: {result['principal']['confianza_porcentaje']}%")
    
    assert result['num_diagnosticos'] > 0, "Debería encontrar al menos un diagnóstico"
    print("✓ Test pasado\n")


def test_sensibilidad_diagnosis():
    """Prueba diagnóstico de sensibilidad dental"""
    print("=== Test: Diagnóstico de Sensibilidad Dental ===")
    
    engine = DiagnosisEngine()
    
    symptoms = {
        'tipo_dolor': 'agudo',
        'intensidad_dolor': 4,
        'duracion_dolor': 'menos_24h',
        'sensibilidad_frio': 7,
        'sensibilidad_calor': 2,
        'sensibilidad_dulce': 3,
        'dolor_masticar': 1,
        'dolor_presion': 0,
        'dolor_nocturno': 0,
        'inflamacion_encias': 1,
        'sangrado_encias': 'no',
        'color_encias': 'normal',
        'retraimiento_encias': 'leve',
        'caries_visible': 'no',
        'mancha_oscura': 'no',
        'fractura_diente': 'no',
        'desgaste_dental': 'leve',
        'hinchazon_cara': 'no',
        'pus_visible': 'no',
        'mal_aliento': 'no',
        'fiebre': 'no',
        'movilidad_dental': 'no',
        'rechinar_dientes': 'no',
        'dolor_mandibula': 0,
        'problemas_mordida': 'no',
        'tratamiento_reciente': 'no',
        'trauma_reciente': 'no'
    }
    
    result = engine.diagnose(symptoms)
    
    print(f"Diagnósticos encontrados: {result['num_diagnosticos']}")
    if result['principal']:
        print(f"Principal: {result['principal']['nombre']}")
        print(f"Confianza: {result['principal']['confianza_porcentaje']}%")
    
    assert result['num_diagnosticos'] > 0, "Debería encontrar al menos un diagnóstico"
    print("✓ Test pasado\n")


def run_all_tests():
    """Ejecuta todas las pruebas"""
    print("\n" + "="*60)
    print("EJECUTANDO PRUEBAS DEL SISTEMA EXPERTO")
    print("="*60 + "\n")
    
    try:
        test_caries_diagnosis()
        test_pulpitis_diagnosis()
        test_absceso_diagnosis()
        test_gingivitis_diagnosis()
        test_sensibilidad_diagnosis()
        
        print("="*60)
        print("✓ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
        print("="*60)
        
    except AssertionError as e:
        print(f"\n✗ Test falló: {e}")
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_all_tests()
