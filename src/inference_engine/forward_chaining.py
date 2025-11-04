"""
Motor de Inferencia - Encadenamiento Hacia Adelante (Forward Chaining)
Procesa los hechos (síntomas) y aplica reglas para llegar a conclusiones
"""

from collections import defaultdict


class ForwardChainingEngine:
    """
    Motor de inferencia que utiliza encadenamiento hacia adelante
    Parte de los hechos conocidos y aplica reglas para derivar nuevas conclusiones
    """
    
    def __init__(self, rules):
        """
        Inicializa el motor con un conjunto de reglas
        rules: lista de funciones que retornan objetos Rule
        """
        self.rules = rules
        self.working_memory = {}  # Memoria de trabajo (hechos conocidos)
        self.fired_rules = []  # Reglas que se han activado
        self.inferred_facts = []  # Hechos inferidos
        
    def reset(self):
        """Reinicia el estado del motor"""
        self.working_memory = {}
        self.fired_rules = []
        self.inferred_facts = []
    
    def add_facts(self, facts):
        """
        Añade hechos a la memoria de trabajo
        facts: diccionario con síntomas del paciente
        """
        self.working_memory.update(facts)
    
    def run(self, facts):
        """
        Ejecuta el motor de inferencia con los hechos proporcionados
        Retorna: lista de conclusiones alcanzadas
        """
        self.reset()
        self.add_facts(facts)
        
        conclusions = []
        
        # Evaluar cada regla
        for rule_func in self.rules:
            try:
                rule = rule_func(self.working_memory)
                
                # Si la regla se activa
                if rule.evaluate(self.working_memory):
                    self.fired_rules.append(rule)
                    
                    # Añadir conclusión
                    conclusion = {
                        'diagnostico': rule.conclusion,
                        'confianza': rule.confidence,
                        'regla': rule.name,
                        'tipo': 'crisp'
                    }
                    conclusions.append(conclusion)
                    
                    # Registrar el hecho inferido
                    self.inferred_facts.append({
                        'hecho': f"diagnostico_{rule.conclusion}",
                        'valor': True,
                        'confianza': rule.confidence
                    })
            
            except Exception as e:
                print(f"Error al evaluar regla: {e}")
                continue
        
        return conclusions
    
    def explain_reasoning(self):
        """
        Proporciona una explicación del razonamiento seguido
        """
        explanation = {
            'facts_used': len(self.working_memory),
            'rules_fired': len(self.fired_rules),
            'conclusions': len(self.inferred_facts),
            'fired_rules_names': [rule.name for rule in self.fired_rules],
            'inferred_facts': self.inferred_facts
        }
        return explanation
    
    def get_conclusion_chain(self, conclusion):
        """
        Obtiene la cadena de razonamiento para una conclusión específica
        """
        chain = []
        for rule in self.fired_rules:
            if rule.conclusion == conclusion:
                chain.append({
                    'rule': rule.name,
                    'confidence': rule.confidence,
                    'conclusion': rule.conclusion
                })
        return chain


class ConflictResolution:
    """
    Estrategias para resolver conflictos cuando múltiples reglas se activan
    """
    
    @staticmethod
    def highest_confidence(conclusions):
        """
        Retorna la conclusión con mayor confianza
        """
        if not conclusions:
            return None
        return max(conclusions, key=lambda x: x['confianza'])
    
    @staticmethod
    def most_specific(conclusions):
        """
        Retorna la conclusión más específica (más condiciones)
        """
        # En este caso, asumimos que todas tienen igual especificidad
        # En una implementación más avanzada, se contarían las condiciones
        return ConflictResolution.highest_confidence(conclusions)
    
    @staticmethod
    def combine_evidence(conclusions):
        """
        Combina evidencia de múltiples reglas para el mismo diagnóstico
        Usa promedio ponderado
        """
        if not conclusions:
            return []
        
        # Agrupar conclusiones por diagnóstico
        by_diagnosis = defaultdict(list)
        for conclusion in conclusions:
            by_diagnosis[conclusion['diagnostico']].append(conclusion)
        
        # Combinar evidencia
        combined = []
        for diagnostico, evidences in by_diagnosis.items():
            if len(evidences) == 1:
                combined.append(evidences[0])
            else:
                # Usar el máximo de confianza entre las evidencias
                max_conf = max(e['confianza'] for e in evidences)
                combined.append({
                    'diagnostico': diagnostico,
                    'confianza': max_conf,
                    'regla': f"Combinación de {len(evidences)} reglas",
                    'tipo': 'combinado',
                    'evidencias': evidences
                })
        
        return combined
    
    @staticmethod
    def recency(conclusions):
        """
        Retorna la conclusión más reciente (última en la lista)
        """
        if not conclusions:
            return None
        return conclusions[-1]


def apply_conflict_resolution(conclusions, strategy='combine'):
    """
    Aplica una estrategia de resolución de conflictos
    
    Args:
        conclusions: lista de conclusiones
        strategy: 'combine', 'highest', 'specific', 'recent'
    
    Returns:
        conclusiones procesadas según la estrategia
    """
    resolver = ConflictResolution()
    
    if strategy == 'combine':
        return resolver.combine_evidence(conclusions)
    elif strategy == 'highest':
        result = resolver.highest_confidence(conclusions)
        return [result] if result else []
    elif strategy == 'specific':
        result = resolver.most_specific(conclusions)
        return [result] if result else []
    elif strategy == 'recent':
        result = resolver.recency(conclusions)
        return [result] if result else []
    else:
        return conclusions
