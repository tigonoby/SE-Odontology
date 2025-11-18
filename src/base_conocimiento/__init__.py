"""
Módulo de inicialización de la base de conocimientos
"""

from .hechos import (
    SINTOMAS,
    DIAGNOSTICOS,
    RECOMENDACIONES,
    get_sintoma_info,
    get_diagnostico_info,
    get_recomendaciones
)

from .reglas_crisp import (
    Rule,
    get_all_rules,
    evaluate_crisp_rules
)

from .reglas_difusas import (
    FuzzyDiagnosisSystem,
    get_fuzzy_system,
    evaluate_fuzzy_rules
)

__all__ = [
    'SINTOMAS',
    'DIAGNOSTICOS',
    'RECOMENDACIONES',
    'get_sintoma_info',
    'get_diagnostico_info',
    'get_recomendaciones',
    'Rule',
    'get_all_rules',
    'evaluate_crisp_rules',
    'FuzzyDiagnosisSystem',
    'get_fuzzy_system',
    'evaluate_fuzzy_rules'
]
