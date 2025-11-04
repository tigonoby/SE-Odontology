"""
Motor de Lógica Difusa
Maneja razonamiento difuso para síntomas ambiguos
"""

import numpy as np


class FuzzySet:
    """Representa un conjunto difuso"""
    
    def __init__(self, name, universe, membership_function):
        """
        name: nombre del conjunto
        universe: rango de valores posibles
        membership_function: función que calcula el grado de pertenencia
        """
        self.name = name
        self.universe = universe
        self.membership_function = membership_function
    
    def membership_degree(self, value):
        """Calcula el grado de pertenencia de un valor"""
        return self.membership_function(value)


class TriangularMF:
    """Función de pertenencia triangular"""
    
    def __init__(self, a, b, c):
        """
        a: límite inferior
        b: punto medio (máxima pertenencia)
        c: límite superior
        """
        self.a = a
        self.b = b
        self.c = c
    
    def __call__(self, x):
        """Calcula el grado de pertenencia"""
        if x <= self.a or x >= self.c:
            return 0.0
        elif x == self.b:
            return 1.0
        elif x < self.b:
            return (x - self.a) / (self.b - self.a)
        else:
            return (self.c - x) / (self.c - self.b)


class TrapezoidalMF:
    """Función de pertenencia trapezoidal"""
    
    def __init__(self, a, b, c, d):
        """
        a: límite inferior
        b: inicio de la meseta
        c: fin de la meseta
        d: límite superior
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def __call__(self, x):
        """Calcula el grado de pertenencia"""
        if x <= self.a or x >= self.d:
            return 0.0
        elif self.b <= x <= self.c:
            return 1.0
        elif x < self.b:
            return (x - self.a) / (self.b - self.a)
        else:
            return (self.d - x) / (self.d - self.c)


class FuzzyVariable:
    """Variable lingüística difusa"""
    
    def __init__(self, name, universe):
        """
        name: nombre de la variable
        universe: rango de valores posibles
        """
        self.name = name
        self.universe = universe
        self.fuzzy_sets = {}
    
    def add_fuzzy_set(self, set_name, membership_function):
        """Añade un conjunto difuso a la variable"""
        fuzzy_set = FuzzySet(set_name, self.universe, membership_function)
        self.fuzzy_sets[set_name] = fuzzy_set
    
    def fuzzify(self, value):
        """
        Fuzzifica un valor crisp
        Retorna un diccionario con grados de pertenencia a cada conjunto
        """
        result = {}
        for set_name, fuzzy_set in self.fuzzy_sets.items():
            result[set_name] = fuzzy_set.membership_degree(value)
        return result


class FuzzyRule:
    """Regla difusa IF-THEN"""
    
    def __init__(self, antecedents, consequent, operator='AND'):
        """
        antecedents: lista de tuplas (variable, conjunto, valor_pertenencia)
        consequent: tupla (variable_salida, conjunto)
        operator: 'AND' o 'OR'
        """
        self.antecedents = antecedents
        self.consequent = consequent
        self.operator = operator
    
    def evaluate(self):
        """
        Evalúa la regla y retorna el grado de activación
        """
        if not self.antecedents:
            return 0.0
        
        # Extraer grados de pertenencia
        degrees = [ant[2] for ant in self.antecedents]
        
        # Aplicar operador
        if self.operator == 'AND':
            return min(degrees)
        elif self.operator == 'OR':
            return max(degrees)
        else:
            return min(degrees)


class FuzzyInferenceSystem:
    """Sistema de inferencia difusa simplificado"""
    
    def __init__(self):
        self.variables = {}
        self.rules = []
    
    def add_variable(self, variable):
        """Añade una variable lingüística"""
        self.variables[variable.name] = variable
    
    def add_rule(self, rule):
        """Añade una regla difusa"""
        self.rules.append(rule)
    
    def fuzzify_inputs(self, inputs):
        """
        Fuzzifica las entradas
        inputs: diccionario {nombre_variable: valor}
        """
        fuzzified = {}
        for var_name, value in inputs.items():
            if var_name in self.variables:
                fuzzified[var_name] = self.variables[var_name].fuzzify(value)
        return fuzzified
    
    def infer(self, inputs):
        """
        Realiza la inferencia difusa
        """
        # Fuzzificar entradas
        fuzzified = self.fuzzify_inputs(inputs)
        
        # Evaluar reglas
        activated_rules = []
        for rule in self.rules:
            # Construir antecedentes con grados de pertenencia
            antecedents_with_degrees = []
            for var_name, fuzzy_set, _ in rule.antecedents:
                if var_name in fuzzified and fuzzy_set in fuzzified[var_name]:
                    degree = fuzzified[var_name][fuzzy_set]
                    antecedents_with_degrees.append((var_name, fuzzy_set, degree))
            
            # Crear regla con grados
            temp_rule = FuzzyRule(antecedents_with_degrees, rule.consequent, rule.operator)
            activation = temp_rule.evaluate()
            
            if activation > 0:
                activated_rules.append({
                    'rule': rule,
                    'activation': activation,
                    'consequent': rule.consequent
                })
        
        return activated_rules
    
    def defuzzify(self, activated_rules, method='centroid'):
        """
        Defuzzifica el resultado
        Simplificación: usa promedio ponderado
        """
        if not activated_rules:
            return 0.0
        
        # Agrupar por consecuente
        consequents = {}
        for rule_info in activated_rules:
            cons = rule_info['consequent']
            key = f"{cons[0]}_{cons[1]}"
            if key not in consequents:
                consequents[key] = []
            consequents[key].append(rule_info['activation'])
        
        # Para cada consecuente, usar el máximo grado de activación
        results = {}
        for key, activations in consequents.items():
            results[key] = max(activations)
        
        return results


def create_fuzzy_diagnosis_system():
    """
    Crea un sistema de inferencia difusa para diagnóstico odontológico
    """
    system = FuzzyInferenceSystem()
    
    # Definir variables
    dolor = FuzzyVariable('intensidad_dolor', (0, 10))
    dolor.add_fuzzy_set('bajo', TriangularMF(0, 0, 4))
    dolor.add_fuzzy_set('medio', TriangularMF(2, 5, 8))
    dolor.add_fuzzy_set('alto', TriangularMF(6, 10, 10))
    
    sensibilidad = FuzzyVariable('sensibilidad', (0, 10))
    sensibilidad.add_fuzzy_set('baja', TriangularMF(0, 0, 4))
    sensibilidad.add_fuzzy_set('media', TriangularMF(2, 5, 8))
    sensibilidad.add_fuzzy_set('alta', TriangularMF(6, 10, 10))
    
    system.add_variable(dolor)
    system.add_variable(sensibilidad)
    
    # Definir reglas ejemplo
    # Regla: SI dolor es alto Y sensibilidad es alta ENTONCES pulpitis probable
    rule1 = FuzzyRule(
        [('intensidad_dolor', 'alto', 0), ('sensibilidad', 'alta', 0)],
        ('diagnostico', 'pulpitis'),
        'AND'
    )
    system.add_rule(rule1)
    
    # Regla: SI dolor es medio Y sensibilidad es alta ENTONCES caries probable
    rule2 = FuzzyRule(
        [('intensidad_dolor', 'medio', 0), ('sensibilidad', 'alta', 0)],
        ('diagnostico', 'caries'),
        'AND'
    )
    system.add_rule(rule2)
    
    return system
