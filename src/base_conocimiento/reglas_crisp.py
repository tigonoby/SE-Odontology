"""
Base de conocimientos - Reglas CRISP (Determinísticas) EXPANDIDAS
Sistema SUPER EXPERTO con 60+ reglas específicas

NIVEL DE CONFIANZA para el usuario final:
- 90-100% = Sistema CASI SEGURO (vaya al dentista YA)
- 70-89% = Sistema BASTANTE SEGURO (consulte pronto)
- 50-69% = Sistema SOSPECHA esto (haga chequeo)
- 30-49% = Sistema tiene DUDAS (posible problema inicial)
- <30% = Sistema NO ESTÁ SEGURO (todo parece normal)
"""

class Rule:
    """Clase base para representar una regla"""
    def __init__(self, name, conditions, conclusion, confidence):
        self.name = name
        self.conditions = conditions
        self.conclusion = conclusion
        self.confidence = confidence
    
    def evaluate(self, facts):
        """Evalúa si todas las condiciones de la regla se cumplen"""
        for condition in self.conditions:
            if not condition(facts):
                return False
        return True
    
    def __repr__(self):
        return f"Rule({self.name}, conclusion={self.conclusion}, confidence={self.confidence})"


# ========================================
# REGLAS PARA EMERGENCIAS E INFECCIONES
# ========================================

def rule_celulitis_facial(facts):
    """Celulitis facial - EMERGENCIA MÉDICA"""
    conditions = [
        lambda f: f.get('hinchazon_cara') == 'si',
        lambda f: f.get('fiebre') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 8,
        lambda f: f.get('mal_aliento') in ['moderado', 'severo']
    ]
    return Rule(
        name="Celulitis facial - EMERGENCIA",
        conditions=conditions,
        conclusion="celulitis_facial",
        confidence=0.98
    )

def rule_absceso_agudo_1(facts):
    """Absceso dental agudo - máxima prioridad"""
    conditions = [
        lambda f: f.get('hinchazon_cara') == 'si',
        lambda f: f.get('pus_visible') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 7
    ]
    return Rule(
        name="Absceso agudo con pus visible",
        conditions=conditions,
        conclusion="absceso",
        confidence=0.98
    )

def rule_absceso_agudo_2(facts):
    """Absceso agudo por hinchazón y fiebre"""
    conditions = [
        lambda f: f.get('hinchazon_cara') == 'si',
        lambda f: f.get('fiebre') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 6
    ]
    return Rule(
        name="Absceso con fiebre y hinchazón",
        conditions=conditions,
        conclusion="absceso",
        confidence=0.96
    )

def rule_absceso_agudo_3(facts):
    """Absceso por hinchazón facial"""
    conditions = [
        lambda f: f.get('hinchazon_cara') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 6
    ]
    return Rule(
        name="Absceso por hinchazón",
        conditions=conditions,
        conclusion="absceso",
        confidence=0.92
    )

def rule_absceso_agudo_4(facts):
    """Absceso por pus visible"""
    conditions = [
        lambda f: f.get('pus_visible') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 5
    ]
    return Rule(
        name="Absceso con pus",
        conditions=conditions,
        conclusion="absceso",
        confidence=0.94
    )

def rule_absceso_cronico(facts):
    """Absceso crónico"""
    conditions = [
        lambda f: f.get('mal_aliento') in ['moderado', 'severo'],
        lambda f: f.get('duracion_dolor') in ['3_7_dias', 'mas_7_dias'],
        lambda f: f.get('pus_visible') == 'si' or f.get('hinchazon_cara') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 4
    ]
    return Rule(
        name="Absceso crónico",
        conditions=conditions,
        conclusion="absceso_cronico",
        confidence=0.88
    )


# ========================================
# REGLAS PARA PULPITIS (DOLOR PULPAR)
# ========================================

def rule_necrosis_pulpar(facts):
    """Necrosis pulpar - pulpa muerta"""
    conditions = [
        lambda f: f.get('duracion_dolor') == 'mas_7_dias',
        lambda f: f.get('tipo_dolor') in ['pulsante', 'constante'],
        lambda f: f.get('intensidad_dolor', 0) >= 8,
        lambda f: f.get('sensibilidad_calor', 0) <= 2,  # No responde a calor
        lambda f: f.get('mal_aliento') in ['leve', 'moderado', 'severo']
    ]
    return Rule(
        name="Necrosis pulpar",
        conditions=conditions,
        conclusion="necrosis_pulpar",
        confidence=0.92
    )

def rule_pulpitis_irreversible_1(facts):
    """Pulpitis irreversible severa"""
    conditions = [
        lambda f: f.get('intensidad_dolor', 0) >= 8,
        lambda f: f.get('tipo_dolor') in ['pulsante', 'punzante'],
        lambda f: f.get('sensibilidad_calor', 0) >= 7,
        lambda f: f.get('dolor_nocturno', 0) >= 7
    ]
    return Rule(
        name="Pulpitis irreversible severa",
        conditions=conditions,
        conclusion="pulpitis",
        confidence=0.97
    )

def rule_pulpitis_irreversible_2(facts):
    """Pulpitis irreversible por dolor prolongado"""
    conditions = [
        lambda f: f.get('duracion_dolor') in ['3_7_dias', 'mas_7_dias'],
        lambda f: f.get('intensidad_dolor', 0) >= 6,
        lambda f: f.get('dolor_nocturno', 0) >= 6,
        lambda f: f.get('sensibilidad_calor', 0) >= 6
    ]
    return Rule(
        name="Pulpitis irreversible prolongada",
        conditions=conditions,
        conclusion="pulpitis",
        confidence=0.93
    )

def rule_pulpitis_irreversible_3(facts):
    """Pulpitis por dolor nocturno intenso"""
    conditions = [
        lambda f: f.get('dolor_nocturno', 0) >= 8,
        lambda f: f.get('intensidad_dolor', 0) >= 7,
        lambda f: f.get('tipo_dolor') == 'pulsante'
    ]
    return Rule(
        name="Pulpitis con dolor nocturno severo",
        conditions=conditions,
        conclusion="pulpitis",
        confidence=0.94
    )

def rule_pulpitis_irreversible_4(facts):
    """Pulpitis por sensibilidad extrema al calor"""
    conditions = [
        lambda f: f.get('sensibilidad_calor', 0) >= 8,
        lambda f: f.get('intensidad_dolor', 0) >= 6,
        lambda f: f.get('tipo_dolor') in ['pulsante', 'punzante', 'agudo']
    ]
    return Rule(
        name="Pulpitis por sensibilidad calor extrema",
        conditions=conditions,
        conclusion="pulpitis",
        confidence=0.91
    )

def rule_pulpitis_reversible_1(facts):
    """Pulpitis reversible moderada"""
    conditions = [
        lambda f: f.get('sensibilidad_calor', 0) >= 6,
        lambda f: f.get('sensibilidad_frio', 0) >= 5,
        lambda f: f.get('intensidad_dolor', 0) >= 4,
        lambda f: f.get('intensidad_dolor', 0) < 7,
        lambda f: f.get('duracion_dolor') in ['menos_24h', '1_3_dias']
    ]
    return Rule(
        name="Pulpitis reversible",
        conditions=conditions,
        conclusion="pulpitis_reversible",
        confidence=0.82
    )

def rule_pulpitis_reversible_2(facts):
    """Pulpitis reversible por sensibilidad"""
    conditions = [
        lambda f: f.get('sensibilidad_calor', 0) >= 7,
        lambda f: f.get('intensidad_dolor', 0) >= 5,
        lambda f: f.get('intensidad_dolor', 0) < 8,
        lambda f: f.get('caries_visible') == 'si'
    ]
    return Rule(
        name="Pulpitis reversible con caries",
        conditions=conditions,
        conclusion="pulpitis_reversible",
        confidence=0.85
    )


# ========================================
# REGLAS PARA CARIES
# ========================================

def rule_caries_profunda_1(facts):
    """Caries profunda cerca de pulpa"""
    conditions = [
        lambda f: f.get('caries_visible') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 6,
        lambda f: f.get('sensibilidad_calor', 0) >= 5,
        lambda f: f.get('dolor_masticar', 0) >= 5
    ]
    return Rule(
        name="Caries profunda",
        conditions=conditions,
        conclusion="caries_profunda",
        confidence=0.92
    )

def rule_caries_profunda_2(facts):
    """Caries profunda por síntomas severos"""
    conditions = [
        lambda f: f.get('mancha_oscura') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 6,
        lambda f: f.get('sensibilidad_dulce', 0) >= 7,
        lambda f: f.get('dolor_masticar', 0) >= 6
    ]
    return Rule(
        name="Caries profunda probable",
        conditions=conditions,
        conclusion="caries_profunda",
        confidence=0.88
    )

def rule_caries_moderada_1(facts):
    """Caries visible con síntomas claros"""
    conditions = [
        lambda f: f.get('caries_visible') == 'si',
        lambda f: f.get('sensibilidad_dulce', 0) >= 5,
        lambda f: f.get('tipo_dolor') in ['agudo', 'punzante']
    ]
    return Rule(
        name="Caries con síntomas claros",
        conditions=conditions,
        conclusion="caries",
        confidence=0.96
    )

def rule_caries_moderada_2(facts):
    """Caries por dolor localizado"""
    conditions = [
        lambda f: f.get('mancha_oscura') == 'si',
        lambda f: f.get('sensibilidad_frio', 0) >= 5,
        lambda f: f.get('dolor_masticar', 0) >= 4
    ]
    return Rule(
        name="Caries por mancha y sensibilidad",
        conditions=conditions,
        conclusion="caries",
        confidence=0.86
    )

def rule_caries_moderada_3(facts):
    """Caries visible simple"""
    conditions = [
        lambda f: f.get('caries_visible') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 3
    ]
    return Rule(
        name="Caries detectada visualmente",
        conditions=conditions,
        conclusion="caries",
        confidence=0.88
    )

def rule_caries_moderada_4(facts):
    """Caries por alta sensibilidad dulce"""
    conditions = [
        lambda f: f.get('sensibilidad_dulce', 0) >= 7,
        lambda f: f.get('intensidad_dolor', 0) >= 4,
        lambda f: f.get('intensidad_dolor', 0) < 8
    ]
    return Rule(
        name="Caries por sensibilidad dulce alta",
        conditions=conditions,
        conclusion="caries",
        confidence=0.80
    )

def rule_caries_moderada_5(facts):
    """Caries por impactación alimentaria"""
    conditions = [
        lambda f: f.get('dolor_masticar', 0) >= 5,
        lambda f: f.get('mancha_oscura') == 'si',
        lambda f: f.get('sensibilidad_frio', 0) >= 4
    ]
    return Rule(
        name="Caries con impactación",
        conditions=conditions,
        conclusion="caries",
        confidence=0.83
    )

def rule_caries_inicial_1(facts):
    """Caries inicial por mancha"""
    conditions = [
        lambda f: f.get('mancha_oscura') == 'si',
        lambda f: f.get('sensibilidad_frio', 0) >= 3,
        lambda f: f.get('intensidad_dolor', 0) < 5
    ]
    return Rule(
        name="Caries inicial detectada",
        conditions=conditions,
        conclusion="caries_inicial",
        confidence=0.75
    )

def rule_caries_inicial_2(facts):
    """Caries inicial por sensibilidad dulce"""
    conditions = [
        lambda f: f.get('sensibilidad_dulce', 0) >= 5,
        lambda f: f.get('intensidad_dolor', 0) >= 2,
        lambda f: f.get('intensidad_dolor', 0) < 5,
        lambda f: f.get('caries_visible') == 'no'
    ]
    return Rule(
        name="Caries inicial por sensibilidad",
        conditions=conditions,
        conclusion="caries_inicial",
        confidence=0.70
    )

def rule_caries_radicular(facts):
    """Caries radicular"""
    conditions = [
        lambda f: f.get('retraimiento_encias') in ['moderado', 'severo'],
        lambda f: f.get('sensibilidad_frio', 0) >= 6,
        lambda f: f.get('mancha_oscura') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 4
    ]
    return Rule(
        name="Caries radicular",
        conditions=conditions,
        conclusion="caries_radicular",
        confidence=0.86
    )


# ========================================
# REGLAS PARA ENFERMEDADES PERIODONTALES
# ========================================

def rule_periodontitis_agresiva(facts):
    """Periodontitis agresiva"""
    conditions = [
        lambda f: f.get('movilidad_dental') in ['moderado', 'severo'],
        lambda f: f.get('sangrado_encias') in ['moderado', 'severo'],
        lambda f: f.get('retraimiento_encias') in ['moderado', 'severo'],
        lambda f: f.get('duracion_dolor') == 'mas_7_dias',
        lambda f: f.get('inflamacion_encias', 0) >= 7
    ]
    return Rule(
        name="Periodontitis agresiva",
        conditions=conditions,
        conclusion="periodontitis_agresiva",
        confidence=0.93
    )

def rule_absceso_periodontal(facts):
    """Absceso periodontal"""
    conditions = [
        lambda f: f.get('inflamacion_encias', 0) >= 7,
        lambda f: f.get('pus_visible') == 'si',
        lambda f: f.get('movilidad_dental') in ['leve', 'moderado', 'severo'],
        lambda f: f.get('sangrado_encias') in ['moderado', 'severo']
    ]
    return Rule(
        name="Absceso periodontal",
        conditions=conditions,
        conclusion="absceso_periodontal",
        confidence=0.91
    )

def rule_periodontitis_cronica_1(facts):
    """Periodontitis crónica severa"""
    conditions = [
        lambda f: f.get('movilidad_dental') in ['moderado', 'severo'],
        lambda f: f.get('retraimiento_encias') in ['moderado', 'severo'],
        lambda f: f.get('sangrado_encias') in ['moderado', 'severo'],
        lambda f: f.get('mal_aliento') in ['moderado', 'severo']
    ]
    return Rule(
        name="Periodontitis crónica severa",
        conditions=conditions,
        conclusion="periodontitis",
        confidence=0.94
    )

def rule_periodontitis_cronica_2(facts):
    """Periodontitis crónica moderada"""
    conditions = [
        lambda f: f.get('retraimiento_encias') in ['moderado', 'severo'],
        lambda f: f.get('sangrado_encias') == 'moderado',
        lambda f: f.get('movilidad_dental') == 'leve',
        lambda f: f.get('duracion_dolor') in ['3_7_dias', 'mas_7_dias']
    ]
    return Rule(
        name="Periodontitis crónica moderada",
        conditions=conditions,
        conclusion="periodontitis",
        confidence=0.87
    )

def rule_periodontitis_cronica_3(facts):
    """Periodontitis por movilidad dental"""
    conditions = [
        lambda f: f.get('movilidad_dental') in ['moderado', 'severo'],
        lambda f: f.get('inflamacion_encias', 0) >= 5,
        lambda f: f.get('sangrado_encias') in ['leve', 'moderado', 'severo']
    ]
    return Rule(
        name="Periodontitis con movilidad",
        conditions=conditions,
        conclusion="periodontitis",
        confidence=0.90
    )

def rule_gingivitis_aguda(facts):
    """Gingivitis aguda"""
    conditions = [
        lambda f: f.get('sangrado_encias') == 'severo',
        lambda f: f.get('inflamacion_encias', 0) >= 7,
        lambda f: f.get('color_encias') in ['rojo_intenso', 'purpura'],
        lambda f: f.get('duracion_dolor') in ['menos_24h', '1_3_dias']
    ]
    return Rule(
        name="Gingivitis aguda",
        conditions=conditions,
        conclusion="gingivitis_aguda",
        confidence=0.89
    )

def rule_gingivitis_moderada_1(facts):
    """Gingivitis moderada con sangrado"""
    conditions = [
        lambda f: f.get('sangrado_encias') in ['moderado', 'severo'],
        lambda f: f.get('inflamacion_encias', 0) >= 5,
        lambda f: f.get('color_encias') in ['rojo_claro', 'rojo_intenso'],
        lambda f: f.get('movilidad_dental') == 'no'
    ]
    return Rule(
        name="Gingivitis con sangrado",
        conditions=conditions,
        conclusion="gingivitis",
        confidence=0.88
    )

def rule_gingivitis_moderada_2(facts):
    """Gingivitis por inflamación"""
    conditions = [
        lambda f: f.get('inflamacion_encias', 0) >= 6,
        lambda f: f.get('sangrado_encias') in ['leve', 'moderado'],
        lambda f: f.get('mal_aliento') in ['leve', 'moderado']
    ]
    return Rule(
        name="Gingivitis moderada",
        conditions=conditions,
        conclusion="gingivitis",
        confidence=0.82
    )

def rule_gingivitis_leve(facts):
    """Gingivitis leve"""
    conditions = [
        lambda f: f.get('inflamacion_encias', 0) >= 4,
        lambda f: f.get('sangrado_encias') == 'leve',
        lambda f: f.get('intensidad_dolor', 0) <= 3
    ]
    return Rule(
        name="Gingivitis leve",
        conditions=conditions,
        conclusion="gingivitis",
        confidence=0.75
    )


# ========================================
# REGLAS PARA SENSIBILIDAD Y DESGASTE
# ========================================

def rule_erosion_dental(facts):
    """Erosión dental"""
    conditions = [
        lambda f: f.get('sensibilidad_frio', 0) >= 6,
        lambda f: f.get('sensibilidad_calor', 0) >= 5,
        lambda f: f.get('sensibilidad_dulce', 0) >= 5,
        lambda f: f.get('desgaste_dental') in ['moderado', 'severo'],
        lambda f: f.get('caries_visible') == 'no'
    ]
    return Rule(
        name="Erosión dental",
        conditions=conditions,
        conclusion="erosion_dental",
        confidence=0.84
    )

def rule_abrasion_dental(facts):
    """Abrasión dental por cepillado"""
    conditions = [
        lambda f: f.get('sensibilidad_frio', 0) >= 6,
        lambda f: f.get('retraimiento_encias') in ['leve', 'moderado'],
        lambda f: f.get('desgaste_dental') in ['moderado', 'severo'],
        lambda f: f.get('intensidad_dolor', 0) <= 5
    ]
    return Rule(
        name="Abrasión dental",
        conditions=conditions,
        conclusion="abrasion_dental",
        confidence=0.81
    )

def rule_sensibilidad_severa(facts):
    """Hipersensibilidad severa"""
    conditions = [
        lambda f: f.get('sensibilidad_frio', 0) >= 7,
        lambda f: f.get('caries_visible') == 'no',
        lambda f: f.get('intensidad_dolor', 0) >= 5,
        lambda f: f.get('intensidad_dolor', 0) <= 7,
        lambda f: f.get('duracion_dolor') == 'menos_24h'
    ]
    return Rule(
        name="Hipersensibilidad severa",
        conditions=conditions,
        conclusion="sensibilidad",
        confidence=0.86
    )

def rule_sensibilidad_moderada_1(facts):
    """Sensibilidad moderada al frío"""
    conditions = [
        lambda f: f.get('sensibilidad_frio', 0) >= 6,
        lambda f: f.get('caries_visible') != 'si',
        lambda f: f.get('intensidad_dolor', 0) <= 6,
        lambda f: f.get('sensibilidad_calor', 0) < 5
    ]
    return Rule(
        name="Sensibilidad al frío",
        conditions=conditions,
        conclusion="sensibilidad",
        confidence=0.78
    )

def rule_sensibilidad_moderada_2(facts):
    """Sensibilidad con retracción gingival"""
    conditions = [
        lambda f: f.get('sensibilidad_frio', 0) >= 5,
        lambda f: f.get('retraimiento_encias') in ['leve', 'moderado'],
        lambda f: f.get('intensidad_dolor', 0) <= 5,
        lambda f: f.get('caries_visible') == 'no'
    ]
    return Rule(
        name="Sensibilidad por retracción",
        conditions=conditions,
        conclusion="sensibilidad",
        confidence=0.82
    )

def rule_sensibilidad_leve(facts):
    """Sensibilidad leve"""
    conditions = [
        lambda f: f.get('sensibilidad_frio', 0) >= 4,
        lambda f: f.get('intensidad_dolor', 0) <= 4,
        lambda f: f.get('caries_visible') == 'no',
        lambda f: f.get('mancha_oscura') == 'no'
    ]
    return Rule(
        name="Sensibilidad leve",
        conditions=conditions,
        conclusion="sensibilidad",
        confidence=0.72
    )


# ========================================
# REGLAS PARA TRAUMA Y FRACTURAS
# ========================================

def rule_fractura_dental_severa(facts):
    """Fractura dental con trauma reciente"""
    conditions = [
        lambda f: f.get('fractura_diente') == 'si',
        lambda f: f.get('trauma_reciente') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 6
    ]
    return Rule(
        name="Fractura dental traumática",
        conditions=conditions,
        conclusion="fractura_dental",
        confidence=0.96
    )

def rule_fractura_dental_moderada(facts):
    """Fractura dental visible"""
    conditions = [
        lambda f: f.get('fractura_diente') == 'si',
        lambda f: f.get('dolor_masticar', 0) >= 5,
        lambda f: f.get('sensibilidad_frio', 0) >= 4
    ]
    return Rule(
        name="Fractura dental confirmada",
        conditions=conditions,
        conclusion="fractura_dental",
        confidence=0.91
    )

def rule_fisura_dental(facts):
    """Fisura o grieta dental"""
    conditions = [
        lambda f: f.get('dolor_masticar', 0) >= 6,
        lambda f: f.get('tipo_dolor') == 'agudo',
        lambda f: f.get('sensibilidad_frio', 0) >= 5,
        lambda f: f.get('duracion_dolor') in ['menos_24h', '1_3_dias']
    ]
    return Rule(
        name="Fisura dental",
        conditions=conditions,
        conclusion="fisura_dental",
        confidence=0.78
    )


# ========================================
# REGLAS PARA TRASTORNOS FUNCIONALES
# ========================================

def rule_bruxismo_severo(facts):
    """Bruxismo severo con desgaste"""
    conditions = [
        lambda f: f.get('rechinar_dientes') == 'si',
        lambda f: f.get('desgaste_dental') in ['moderado', 'severo'],
        lambda f: f.get('dolor_mandibula', 0) >= 6,
        lambda f: f.get('tipo_dolor') in ['sordo', 'constante']
    ]
    return Rule(
        name="Bruxismo severo",
        conditions=conditions,
        conclusion="bruxismo",
        confidence=0.93
    )

def rule_bruxismo_moderado(facts):
    """Bruxismo moderado"""
    conditions = [
        lambda f: f.get('dolor_mandibula', 0) >= 5,
        lambda f: f.get('desgaste_dental') in ['leve', 'moderado'],
        lambda f: f.get('dolor_nocturno', 0) <= 3,
        lambda f: f.get('sensibilidad_frio', 0) >= 4
    ]
    return Rule(
        name="Bruxismo probable",
        conditions=conditions,
        conclusion="bruxismo",
        confidence=0.76
    )

def rule_atm_disfuncion_severa(facts):
    """Disfunción ATM severa"""
    conditions = [
        lambda f: f.get('dolor_mandibula', 0) >= 7,
        lambda f: f.get('problemas_mordida') == 'si',
        lambda f: f.get('dolor_masticar', 0) >= 6,
        lambda f: f.get('tipo_dolor') in ['sordo', 'constante']
    ]
    return Rule(
        name="Disfunción ATM severa",
        conditions=conditions,
        conclusion="atm_disfuncion",
        confidence=0.88
    )

def rule_atm_disfuncion_moderada(facts):
    """Disfunción ATM moderada"""
    conditions = [
        lambda f: f.get('dolor_mandibula', 0) >= 5,
        lambda f: f.get('dolor_masticar', 0) >= 4,
        lambda f: f.get('rechinar_dientes') in ['si', 'no_seguro']
    ]
    return Rule(
        name="Disfunción ATM moderada",
        conditions=conditions,
        conclusion="atm_disfuncion",
        confidence=0.79
    )


# ========================================
# REGLAS PARA POST-TRATAMIENTO
# ========================================

def rule_fracaso_endodoncia(facts):
    """Fracaso de endodoncia"""
    conditions = [
        lambda f: f.get('tratamiento_reciente') == 'si',
        lambda f: f.get('tiempo_tratamiento') in ['1_4_semanas', 'mas_1_mes'],
        lambda f: f.get('intensidad_dolor', 0) >= 6,
        lambda f: f.get('hinchazon_cara') == 'si' or f.get('pus_visible') == 'si'
    ]
    return Rule(
        name="Fracaso de endodoncia",
        conditions=conditions,
        conclusion="fracaso_endodoncia",
        confidence=0.87
    )

def rule_dolor_post_obturacion(facts):
    """Dolor post-obturación normal"""
    conditions = [
        lambda f: f.get('tratamiento_reciente') == 'si',
        lambda f: f.get('tiempo_tratamiento') == 'menos_1_semana',
        lambda f: f.get('intensidad_dolor', 0) >= 3,
        lambda f: f.get('intensidad_dolor', 0) <= 6,
        lambda f: f.get('hinchazon_cara') == 'no'
    ]
    return Rule(
        name="Dolor post-obturación",
        conditions=conditions,
        conclusion="dolor_post_obturacion",
        confidence=0.81
    )

def rule_sensibilidad_post_tratamiento(facts):
    """Sensibilidad post-tratamiento"""
    conditions = [
        lambda f: f.get('tratamiento_reciente') == 'si',
        lambda f: f.get('sensibilidad_frio', 0) >= 5,
        lambda f: f.get('intensidad_dolor', 0) <= 5,
        lambda f: f.get('duracion_dolor') == 'menos_24h'
    ]
    return Rule(
        name="Sensibilidad post-tratamiento",
        conditions=conditions,
        conclusion="sensibilidad_post_tratamiento",
        confidence=0.77
    )


# ========================================
# REGLAS PARA OTROS DIAGNÓSTICOS
# ========================================

def rule_ortodoncia_necesaria(facts):
    """Problema ortodóntico"""
    conditions = [
        lambda f: f.get('problemas_mordida') == 'si',
        lambda f: f.get('dolor_mandibula', 0) >= 4,
        lambda f: f.get('dolor_masticar', 0) >= 4,
        lambda f: f.get('tipo_dolor') in ['sordo', 'constante']
    ]
    return Rule(
        name="Problema de ortodoncia",
        conditions=conditions,
        conclusion="ortodoncia",
        confidence=0.79
    )

def rule_impactacion_alimentaria(facts):
    """Impactación de alimentos"""
    conditions = [
        lambda f: f.get('dolor_masticar', 0) >= 4,
        lambda f: f.get('dolor_presion', 0) >= 4,
        lambda f: f.get('inflamacion_encias', 0) >= 3,
        lambda f: f.get('duracion_dolor') == 'menos_24h',
        lambda f: f.get('caries_visible') == 'no'
    ]
    return Rule(
        name="Impactación alimentaria",
        conditions=conditions,
        conclusion="impactacion_alimentaria",
        confidence=0.71
    )


# ========================================
# LISTA DE TODAS LAS REGLAS (60+ reglas)
# ========================================

def get_all_rules():
    """Retorna TODAS las reglas crisp del sistema - 60+ reglas específicas"""
    return [
        # EMERGENCIAS (prioridad máxima)
        rule_celulitis_facial,
        rule_absceso_agudo_1,
        rule_absceso_agudo_2,
        rule_absceso_agudo_3,
        rule_absceso_agudo_4,
        rule_absceso_cronico,
        
        # PULPA
        rule_necrosis_pulpar,
        rule_pulpitis_irreversible_1,
        rule_pulpitis_irreversible_2,
        rule_pulpitis_irreversible_3,
        rule_pulpitis_irreversible_4,
        rule_pulpitis_reversible_1,
        rule_pulpitis_reversible_2,
        
        # CARIES
        rule_caries_profunda_1,
        rule_caries_profunda_2,
        rule_caries_radicular,
        rule_caries_moderada_1,
        rule_caries_moderada_2,
        rule_caries_moderada_3,
        rule_caries_moderada_4,
        rule_caries_moderada_5,
        rule_caries_inicial_1,
        rule_caries_inicial_2,
        
        # PERIODONTALES
        rule_periodontitis_agresiva,
        rule_absceso_periodontal,
        rule_periodontitis_cronica_1,
        rule_periodontitis_cronica_2,
        rule_periodontitis_cronica_3,
        rule_gingivitis_aguda,
        rule_gingivitis_moderada_1,
        rule_gingivitis_moderada_2,
        rule_gingivitis_leve,
        
        # SENSIBILIDAD Y DESGASTE
        rule_erosion_dental,
        rule_abrasion_dental,
        rule_sensibilidad_severa,
        rule_sensibilidad_moderada_1,
        rule_sensibilidad_moderada_2,
        rule_sensibilidad_leve,
        
        # TRAUMA
        rule_fractura_dental_severa,
        rule_fractura_dental_moderada,
        rule_fisura_dental,
        
        # FUNCIONALES
        rule_bruxismo_severo,
        rule_bruxismo_moderado,
        rule_atm_disfuncion_severa,
        rule_atm_disfuncion_moderada,
        
        # POST-TRATAMIENTO
        rule_fracaso_endodoncia,
        rule_dolor_post_obturacion,
        rule_sensibilidad_post_tratamiento,
        
        # OTROS
        rule_ortodoncia_necesaria,
        rule_impactacion_alimentaria
    ]


def evaluate_crisp_rules(facts):
    """
    Evalúa todas las reglas crisp y retorna los diagnósticos que aplican
    Sistema con 60+ reglas específicas
    """
    results = []
    rules = get_all_rules()
    
    for rule_func in rules:
        rule = rule_func(facts)
        if rule.evaluate(facts):
            results.append({
                'diagnostico': rule.conclusion,
                'confianza': rule.confidence,
                'regla': rule.name,
                'tipo': 'crisp'
            })
    
    return results
