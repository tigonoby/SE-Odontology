"""
Modelos de Datos
Clases auxiliares para representar entidades
"""

from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class Paciente:
    """Representa un paciente"""
    id: Optional[int] = None
    nombre: str = ""
    edad: Optional[int] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    fecha_registro: Optional[datetime] = None
    notas: Optional[str] = None


@dataclass
class Diagnostico:
    """Representa un diagnóstico"""
    id: Optional[int] = None
    paciente_id: int = 0
    fecha_diagnostico: Optional[datetime] = None
    diagnostico_principal: str = ""
    confianza_principal: float = 0.0
    gravedad: str = ""
    urgencia: str = ""
    descripcion: str = ""
    diagnosticos_alternativos: Optional[List] = None
    num_sintomas_evaluados: int = 0
    usa_logica_fuzzy: bool = False


@dataclass
class Sintoma:
    """Representa un síntoma evaluado"""
    id: Optional[int] = None
    diagnostico_id: int = 0
    nombre_sintoma: str = ""
    valor_sintoma: str = ""
    tipo_sintoma: str = ""
