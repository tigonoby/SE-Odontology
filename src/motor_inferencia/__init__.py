"""
Módulo de inicialización del motor de inferencia
"""

from .encadenamiento_adelante import (
    ForwardChainingEngine,
    ConflictResolution,
    apply_conflict_resolution
)

from .logica_difusa import (
    FuzzySet,
    TriangularMF,
    TrapezoidalMF,
    FuzzyVariable,
    FuzzyRule,
    FuzzyInferenceSystem,
    create_fuzzy_diagnosis_system
)

from .diagnostico import MotorDiagnostico

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
    'MotorDiagnostico'
]
