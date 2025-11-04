"""
Módulo de inicialización de la base de conocimientos
"""

from .facts import (
    SINTOMAS,
    DIAGNOSTICOS,
    RECOMENDACIONES,
    get_sintoma_info,
    get_diagnostico_info,
    get_recomendaciones
)

from .crisp_rules import (
    Rule,
    get_all_rules,
    evaluate_crisp_rules
)

from .fuzzy_rules import (
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
