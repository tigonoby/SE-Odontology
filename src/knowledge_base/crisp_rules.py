"""
Base de conocimientos - Reglas CRISP (Determinísticas)
Define reglas IF-THEN para el diagnóstico odontológico
"""

class Rule:
    """Clase base para representar una regla"""
    def __init__(self, name, conditions, conclusion, confidence):
        self.name = name
        self.conditions = conditions  # Lista de condiciones a evaluar
        self.conclusion = conclusion  # Diagnóstico resultante
        self.confidence = confidence  # Nivel de confianza (0-1)
    
    def evaluate(self, facts):
        """
        Evalúa si todas las condiciones de la regla se cumplen
        facts: diccionario con los síntomas del paciente
        """
        for condition in self.conditions:
            if not condition(facts):
                return False
        return True
    
    def __repr__(self):
        return f"Rule({self.name}, conclusion={self.conclusion}, confidence={self.confidence})"


# ===== REGLAS PARA CARIES =====

def rule_caries_1(facts):
    """Caries con dolor al dulce y caries visible"""
    conditions = [
        lambda f: f.get('caries_visible') == 'si',
        lambda f: f.get('sensibilidad_dulce', 0) >= 5,
        lambda f: f.get('tipo_dolor') in ['agudo', 'punzante']
    ]
    return Rule(
        name="Caries con síntomas claros",
        conditions=conditions,
        conclusion="caries",
        confidence=0.9
    )

def rule_caries_2(facts):
    """Caries por dolor localizado y sensibilidad"""
    conditions = [
        lambda f: f.get('mancha_oscura') == 'si',
        lambda f: f.get('sensibilidad_frio', 0) >= 4 or f.get('sensibilidad_dulce', 0) >= 4,
        lambda f: f.get('dolor_masticar', 0) >= 3
    ]
    return Rule(
        name="Caries probable",
        conditions=conditions,
        conclusion="caries",
        confidence=0.75
    )


# ===== REGLAS PARA PULPITIS =====

def rule_pulpitis_1(facts):
    """Pulpitis aguda con dolor severo"""
    conditions = [
        lambda f: f.get('intensidad_dolor', 0) >= 7,
        lambda f: f.get('tipo_dolor') in ['pulsante', 'punzante'],
        lambda f: f.get('sensibilidad_calor', 0) >= 6,
        lambda f: f.get('dolor_nocturno', 0) >= 6
    ]
    return Rule(
        name="Pulpitis aguda",
        conditions=conditions,
        conclusion="pulpitis",
        confidence=0.9
    )

def rule_pulpitis_2(facts):
    """Pulpitis por dolor persistente"""
    conditions = [
        lambda f: f.get('duracion_dolor') in ['3_7_dias', 'mas_7_dias'],
        lambda f: f.get('intensidad_dolor', 0) >= 5,
        lambda f: f.get('dolor_nocturno', 0) >= 5,
        lambda f: f.get('sensibilidad_calor', 0) >= 5
    ]
    return Rule(
        name="Pulpitis probable",
        conditions=conditions,
        conclusion="pulpitis",
        confidence=0.8
    )


# ===== REGLAS PARA ABSCESO =====

def rule_absceso_1(facts):
    """Absceso con signos de infección"""
    conditions = [
        lambda f: f.get('hinchazon_cara') == 'si',
        lambda f: f.get('pus_visible') == 'si' or f.get('fiebre') == 'si',
        lambda f: f.get('intensidad_dolor', 0) >= 7
    ]
    return Rule(
        name="Absceso dental con infección",
        conditions=conditions,
        conclusion="absceso",
        confidence=0.95
    )

def rule_absceso_2(facts):
    """Absceso sin pus visible"""
    conditions = [
        lambda f: f.get('hinchazon_cara') == 'si',
        lambda f: f.get('mal_aliento') in ['moderado', 'severo'],
        lambda f: f.get('dolor_presion', 0) >= 7,
        lambda f: f.get('tipo_dolor') == 'pulsante'
    ]
    return Rule(
        name="Absceso dental probable",
        conditions=conditions,
        conclusion="absceso",
        confidence=0.85
    )


# ===== REGLAS PARA SENSIBILIDAD =====

def rule_sensibilidad_1(facts):
    """Sensibilidad dental sin daño estructural"""
    conditions = [
        lambda f: f.get('sensibilidad_frio', 0) >= 5,
        lambda f: f.get('caries_visible') == 'no',
        lambda f: f.get('intensidad_dolor', 0) <= 5,
        lambda f: f.get('duracion_dolor') == 'menos_24h',
        lambda f: f.get('retraimiento_encias') in ['leve', 'moderado']
    ]
    return Rule(
        name="Sensibilidad dental",
        conditions=conditions,
        conclusion="sensibilidad",
        confidence=0.8
    )


# ===== REGLAS PARA GINGIVITIS =====

def rule_gingivitis_1(facts):
    """Gingivitis con sangrado"""
    conditions = [
        lambda f: f.get('sangrado_encias') in ['moderado', 'severo'],
        lambda f: f.get('inflamacion_encias', 0) >= 5,
        lambda f: f.get('color_encias') in ['rojo_claro', 'rojo_intenso'],
        lambda f: f.get('movilidad_dental') == 'no'
    ]
    return Rule(
        name="Gingivitis activa",
        conditions=conditions,
        conclusion="gingivitis",
        confidence=0.85
    )

def rule_gingivitis_2(facts):
    """Gingivitis leve"""
    conditions = [
        lambda f: f.get('inflamacion_encias', 0) >= 4,
        lambda f: f.get('sangrado_encias') in ['leve', 'moderado'],
        lambda f: f.get('mal_aliento') in ['leve', 'moderado']
    ]
    return Rule(
        name="Gingivitis leve",
        conditions=conditions,
        conclusion="gingivitis",
        confidence=0.75
    )


# ===== REGLAS PARA PERIODONTITIS =====

def rule_periodontitis_1(facts):
    """Periodontitis avanzada"""
    conditions = [
        lambda f: f.get('movilidad_dental') in ['moderado', 'severo'],
        lambda f: f.get('retraimiento_encias') in ['moderado', 'severo'],
        lambda f: f.get('sangrado_encias') in ['moderado', 'severo'],
        lambda f: f.get('mal_aliento') in ['moderado', 'severo']
    ]
    return Rule(
        name="Periodontitis avanzada",
        conditions=conditions,
        conclusion="periodontitis",
        confidence=0.9
    )

def rule_periodontitis_2(facts):
    """Periodontitis moderada"""
    conditions = [
        lambda f: f.get('retraimiento_encias') in ['moderado', 'severo'],
        lambda f: f.get('sangrado_encias') == 'moderado',
        lambda f: f.get('movilidad_dental') == 'leve',
        lambda f: f.get('duracion_dolor') in ['3_7_dias', 'mas_7_dias']
    ]
    return Rule(
        name="Periodontitis moderada",
        conditions=conditions,
        conclusion="periodontitis",
        confidence=0.8
    )


# ===== REGLAS PARA BRUXISMO =====

def rule_bruxismo_1(facts):
    """Bruxismo con desgaste"""
    conditions = [
        lambda f: f.get('rechinar_dientes') == 'si',
        lambda f: f.get('desgaste_dental') in ['moderado', 'severo'],
        lambda f: f.get('dolor_mandibula', 0) >= 5,
        lambda f: f.get('tipo_dolor') in ['sordo', 'constante']
    ]
    return Rule(
        name="Bruxismo confirmado",
        conditions=conditions,
        conclusion="bruxismo",
        confidence=0.9
    )

def rule_bruxismo_2(facts):
    """Bruxismo probable"""
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
        confidence=0.7
    )


# ===== REGLAS PARA PROBLEMAS DE ORTODONCIA =====

def rule_ortodoncia_1(facts):
    """Problema de ortodoncia"""
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
        confidence=0.75
    )


# Lista de todas las reglas
def get_all_rules():
    """Retorna todas las reglas crisp del sistema"""
    return [
        rule_caries_1,
        rule_caries_2,
        rule_pulpitis_1,
        rule_pulpitis_2,
        rule_absceso_1,
        rule_absceso_2,
        rule_sensibilidad_1,
        rule_gingivitis_1,
        rule_gingivitis_2,
        rule_periodontitis_1,
        rule_periodontitis_2,
        rule_bruxismo_1,
        rule_bruxismo_2,
        rule_ortodoncia_1
    ]


def evaluate_crisp_rules(facts):
    """
    Evalúa todas las reglas crisp y retorna los diagnósticos que aplican
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
