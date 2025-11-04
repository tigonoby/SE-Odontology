"""
Módulo de inicialización del motor de inferencia
"""

from .forward_chaining import (
    ForwardChainingEngine,
    ConflictResolution,
    apply_conflict_resolution
)

from .fuzzy_logic import (
    FuzzySet,
    TriangularMF,
    TrapezoidalMF,
    FuzzyVariable,
    FuzzyRule,
    FuzzyInferenceSystem,
    create_fuzzy_diagnosis_system
)

from .diagnosis import DiagnosisEngine

__all__ = [
    'ForwardChainingEngine',
    'ConflictResolution',
    'apply_conflict_resolution',
    'FuzzySet',
    'TriangularMF',
    'TrapezoidalMF',
    'FuzzyVariable',
    'FuzzyRule',
    'FuzzyInferenceSystem',
    'create_fuzzy_diagnosis_system',
    'DiagnosisEngine'
]
