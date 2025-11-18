"""
Base de conocimientos - Hechos y Síntomas
Define los síntomas y características evaluados por el sistema experto
"""

# Tipos de dolor
TIPOS_DOLOR = [
    "agudo",
    "punzante", 
    "constante",
    "pulsante",
    "sordo",
    "intermitente"
]

# Factores desencadenantes
DESENCADENANTES = [
    "frio",
    "calor",
    "dulce",
    "acido",
    "presion",
    "masticacion"
]

# Síntomas
SINTOMAS = {
    # Dolor
    "tipo_dolor": TIPOS_DOLOR,
    "intensidad_dolor": (0, 10),  # Escala numérica
    "duracion_dolor": ["menos_24h", "1_3_dias", "3_7_dias", "mas_7_dias"],
    
    # Sensibilidad
    "sensibilidad_frio": (0, 10),
    "sensibilidad_calor": (0, 10),
    "sensibilidad_dulce": (0, 10),
    
    # Dolor específico
    "dolor_masticar": (0, 10),
    "dolor_presion": (0, 10),
    "dolor_nocturno": (0, 10),
    
    # Encías
    "inflamacion_encias": (0, 10),
    "sangrado_encias": ["no", "leve", "moderado", "severo"],
    "color_encias": ["normal", "rojo_claro", "rojo_intenso", "purpura"],
    "retraimiento_encias": ["no", "leve", "moderado", "severo"],
    
    # Visual
    "caries_visible": ["si", "no", "no_seguro"],
    "mancha_oscura": ["si", "no"],
    "fractura_diente": ["si", "no"],
    "desgaste_dental": ["no", "leve", "moderado", "severo"],
    
    # Infección
    "hinchazon_cara": ["si", "no"],
    "pus_visible": ["si", "no"],
    "mal_aliento": ["no", "leve", "moderado", "severo"],
    "fiebre": ["si", "no"],
    
    # Otros
    "movilidad_dental": ["no", "leve", "moderado", "severo"],
    "rechinar_dientes": ["si", "no", "no_seguro"],
    "dolor_mandibula": (0, 10),
    "problemas_mordida": ["si", "no"],
    
    # Antecedentes
    "tratamiento_reciente": ["si", "no"],
    "tiempo_tratamiento": ["menos_1_semana", "1_4_semanas", "mas_1_mes", "ninguno"],
    "trauma_reciente": ["si", "no"]
}

# Diagnósticos posibles
DIAGNOSTICOS = {
    "caries": {
        "nombre": "Caries Dental",
        "descripcion": "Deterioro del esmalte y dentina causado por ácidos bacterianos",
        "gravedad": "media",
        "urgencia": "moderada"
    },
    "pulpitis": {
        "nombre": "Pulpitis (Inflamación de la Pulpa)",
        "descripcion": "Inflamación del tejido blando interior del diente (pulpa dental)",
        "gravedad": "alta",
        "urgencia": "alta"
    },
    "absceso": {
        "nombre": "Absceso Dental",
        "descripcion": "Infección con acumulación de pus en la raíz del diente",
        "gravedad": "muy_alta",
        "urgencia": "urgente"
    },
    "sensibilidad": {
        "nombre": "Sensibilidad Dental",
        "descripcion": "Hipersensibilidad dentinaria a estímulos externos",
        "gravedad": "baja",
        "urgencia": "baja"
    },
    "gingivitis": {
        "nombre": "Gingivitis",
        "descripcion": "Inflamación de las encías causada por placa bacteriana",
        "gravedad": "media",
        "urgencia": "moderada"
    },
    "periodontitis": {
        "nombre": "Periodontitis",
        "descripcion": "Enfermedad periodontal avanzada con pérdida de soporte óseo",
        "gravedad": "alta",
        "urgencia": "alta"
    },
    "bruxismo": {
        "nombre": "Bruxismo",
        "descripcion": "Rechinamiento o apretamiento involuntario de dientes",
        "gravedad": "media",
        "urgencia": "moderada"
    },
    "ortodoncia": {
        "nombre": "Problema de Ortodoncia",
        "descripcion": "Maloclusión o desalineación dental",
        "gravedad": "media",
        "urgencia": "baja"
    },
    "evaluacion_general": {
        "nombre": "Evaluación General Recomendada",
        "descripcion": "No se identificaron síntomas graves, pero se recomienda evaluación preventiva",
        "gravedad": "baja",
        "urgencia": "baja"
    },
    "caries_inicial": {
        "nombre": "Posible Caries Inicial",
        "descripcion": "Indicios de inicio de caries dental, requiere evaluación profesional",
        "gravedad": "media",
        "urgencia": "moderada"
    },
    "pulpitis_reversible": {
        "nombre": "Posible Pulpitis Reversible",
        "descripcion": "Inflamación leve de la pulpa que puede revertirse con tratamiento",
        "gravedad": "media",
        "urgencia": "moderada"
    }
}

# Recomendaciones por diagnóstico
RECOMENDACIONES = {
    "caries": [
        "Agende una cita con su odontólogo lo antes posible",
        "Evite alimentos y bebidas azucaradas",
        "Mantenga una higiene oral rigurosa",
        "Use hilo dental diariamente",
        "Enjuague con agua tibia con sal si hay molestias"
    ],
    "pulpitis": [
        "URGENTE: Consulte a su odontólogo inmediatamente",
        "Evite alimentos muy fríos o calientes",
        "Puede tomar analgésicos de venta libre (según indicación)",
        "No aplique calor externo en la zona",
        "Evite masticar con el diente afectado"
    ],
    "absceso": [
        "¡EMERGENCIA! Busque atención odontológica de emergencia",
        "NO drene el absceso por su cuenta",
        "Enjuague con agua tibia con sal",
        "Tome analgésicos según necesidad",
        "Si hay fiebre alta, considere atención médica general"
    ],
    "sensibilidad": [
        "Use pasta dental para dientes sensibles",
        "Evite cepillado agresivo",
        "Limite alimentos ácidos",
        "Consulte a su odontólogo para descartar causas subyacentes",
        "Use cepillo de cerdas suaves"
    ],
    "gingivitis": [
        "Mejore su técnica de cepillado",
        "Use hilo dental diariamente",
        "Enjuague bucal antiséptico",
        "Agende una limpieza dental profesional",
        "Evite el tabaco"
    ],
    "periodontitis": [
        "Consulte a un periodoncista urgentemente",
        "Requiere limpieza profunda (raspado y alisado radicular)",
        "Mejore higiene oral inmediatamente",
        "No fume",
        "Puede requerir tratamiento antibiótico"
    ],
    "bruxismo": [
        "Consulte para evaluar férula de descarga nocturna",
        "Reduzca el estrés",
        "Evite cafeína antes de dormir",
        "Practique ejercicios de relajación mandibular",
        "Evite masticar chicle"
    ],
    "ortodoncia": [
        "Consulte a un ortodoncista",
        "Evaluación para posible tratamiento ortodóntico",
        "Puede mejorar función y estética dental",
        "El tratamiento temprano puede prevenir complicaciones"
    ],
    "evaluacion_general": [
        "Agende una revisión dental preventiva",
        "Mantenga una higiene oral adecuada",
        "Cepille sus dientes 2-3 veces al día",
        "Use hilo dental diariamente",
        "Visite al odontólogo cada 6 meses para prevención"
    ],
    "caries_inicial": [
        "Consulte a su odontólogo pronto",
        "Mejore su higiene dental inmediatamente",
        "Reduzca consumo de azúcares",
        "Use pasta dental con flúor",
        "El tratamiento temprano evita complicaciones mayores"
    ],
    "pulpitis_reversible": [
        "Visite a su odontólogo en los próximos días",
        "Evite temperaturas extremas en alimentos",
        "Puede requerir tratamiento conservador",
        "No ignore el síntoma, puede empeorar",
        "Mantenga excelente higiene dental"
    ]
}

def get_sintoma_info(sintoma):
    """Obtiene información sobre un síntoma específico"""
    return SINTOMAS.get(sintoma, None)

def get_diagnostico_info(diagnostico):
    """Obtiene información sobre un diagnóstico específico"""
    return DIAGNOSTICOS.get(diagnostico, None)

def get_recomendaciones(diagnostico):
    """Obtiene recomendaciones para un diagnóstico"""
    return RECOMENDACIONES.get(diagnostico, [])
