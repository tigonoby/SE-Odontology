"""
Base de conocimientos - Reglas Difusas (Fuzzy Logic)
Implementa lógica difusa para casos con síntomas ambiguos
"""

import numpy as np
try:
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
    FUZZY_AVAILABLE = True
except ImportError:
    FUZZY_AVAILABLE = False
    print("Advertencia: scikit-fuzzy no está instalado. Lógica difusa limitada.")


class FuzzyDiagnosisSystem:
    """Sistema de diagnóstico basado en lógica difusa"""
    
    def __init__(self):
        if not FUZZY_AVAILABLE:
            self.system = None
            return
            
        # Definir variables de entrada (antecedentes)
        self.intensidad_dolor = ctrl.Antecedent(np.arange(0, 11, 1), 'intensidad_dolor')
        self.sensibilidad = ctrl.Antecedent(np.arange(0, 11, 1), 'sensibilidad')
        self.inflamacion = ctrl.Antecedent(np.arange(0, 11, 1), 'inflamacion')
        self.duracion = ctrl.Antecedent(np.arange(0, 8, 1), 'duracion_dias')
        
        # Definir variables de salida (consecuentes)
        self.prob_caries = ctrl.Consequent(np.arange(0, 101, 1), 'prob_caries')
        self.prob_pulpitis = ctrl.Consequent(np.arange(0, 101, 1), 'prob_pulpitis')
        self.prob_infeccion = ctrl.Consequent(np.arange(0, 101, 1), 'prob_infeccion')
        self.prob_encias = ctrl.Consequent(np.arange(0, 101, 1), 'prob_encias')
        
        self._define_membership_functions()
        self._define_rules()
        
    def _define_membership_functions(self):
        """Define funciones de pertenencia para variables difusas"""
        
        # Intensidad del dolor
        self.intensidad_dolor['bajo'] = fuzz.trimf(self.intensidad_dolor.universe, [0, 0, 4])
        self.intensidad_dolor['medio'] = fuzz.trimf(self.intensidad_dolor.universe, [2, 5, 8])
        self.intensidad_dolor['alto'] = fuzz.trimf(self.intensidad_dolor.universe, [6, 10, 10])
        
        # Sensibilidad
        self.sensibilidad['baja'] = fuzz.trimf(self.sensibilidad.universe, [0, 0, 4])
        self.sensibilidad['media'] = fuzz.trimf(self.sensibilidad.universe, [2, 5, 8])
        self.sensibilidad['alta'] = fuzz.trimf(self.sensibilidad.universe, [6, 10, 10])
        
        # Inflamación
        self.inflamacion['baja'] = fuzz.trimf(self.inflamacion.universe, [0, 0, 4])
        self.inflamacion['media'] = fuzz.trimf(self.inflamacion.universe, [2, 5, 8])
        self.inflamacion['alta'] = fuzz.trimf(self.inflamacion.universe, [6, 10, 10])
        
        # Duración (días)
        self.duracion['corta'] = fuzz.trimf(self.duracion.universe, [0, 0, 2])
        self.duracion['media'] = fuzz.trimf(self.duracion.universe, [1, 3, 5])
        self.duracion['larga'] = fuzz.trimf(self.duracion.universe, [4, 7, 7])
        
        # Probabilidades de salida (0-100%)
        for prob in [self.prob_caries, self.prob_pulpitis, self.prob_infeccion, self.prob_encias]:
            prob['baja'] = fuzz.trimf(prob.universe, [0, 0, 40])
            prob['media'] = fuzz.trimf(prob.universe, [20, 50, 80])
            prob['alta'] = fuzz.trimf(prob.universe, [60, 100, 100])
    
    def _define_rules(self):
        """Define reglas difusas para diagnóstico"""
        
        # Reglas para CARIES
        rule_caries_1 = ctrl.Rule(
            self.sensibilidad['alta'] & self.intensidad_dolor['medio'],
            self.prob_caries['media']
        )
        rule_caries_2 = ctrl.Rule(
            self.sensibilidad['alta'] & self.intensidad_dolor['alto'] & self.duracion['corta'],
            self.prob_caries['alta']
        )
        rule_caries_3 = ctrl.Rule(
            self.sensibilidad['media'] & self.intensidad_dolor['bajo'],
            self.prob_caries['baja']
        )
        
        # Reglas para PULPITIS
        rule_pulpitis_1 = ctrl.Rule(
            self.intensidad_dolor['alto'] & self.duracion['media'],
            self.prob_pulpitis['alta']
        )
        rule_pulpitis_2 = ctrl.Rule(
            self.intensidad_dolor['alto'] & self.duracion['larga'],
            self.prob_pulpitis['alta']
        )
        rule_pulpitis_3 = ctrl.Rule(
            self.intensidad_dolor['medio'] & self.sensibilidad['alta'] & self.duracion['media'],
            self.prob_pulpitis['media']
        )
        
        # Reglas para INFECCIÓN (Absceso)
        rule_infeccion_1 = ctrl.Rule(
            self.intensidad_dolor['alto'] & self.inflamacion['alta'],
            self.prob_infeccion['alta']
        )
        rule_infeccion_2 = ctrl.Rule(
            self.inflamacion['alta'] & self.duracion['larga'],
            self.prob_infeccion['alta']
        )
        rule_infeccion_3 = ctrl.Rule(
            self.intensidad_dolor['medio'] & self.inflamacion['media'],
            self.prob_infeccion['media']
        )
        
        # Reglas para PROBLEMAS DE ENCÍAS
        rule_encias_1 = ctrl.Rule(
            self.inflamacion['alta'] & self.intensidad_dolor['bajo'],
            self.prob_encias['alta']
        )
        rule_encias_2 = ctrl.Rule(
            self.inflamacion['media'] & self.duracion['larga'],
            self.prob_encias['media']
        )
        rule_encias_3 = ctrl.Rule(
            self.inflamacion['alta'] & self.duracion['larga'],
            self.prob_encias['alta']
        )
        
        # Crear sistemas de control
        self.caries_ctrl = ctrl.ControlSystem([
            rule_caries_1, rule_caries_2, rule_caries_3
        ])
        self.pulpitis_ctrl = ctrl.ControlSystem([
            rule_pulpitis_1, rule_pulpitis_2, rule_pulpitis_3
        ])
        self.infeccion_ctrl = ctrl.ControlSystem([
            rule_infeccion_1, rule_infeccion_2, rule_infeccion_3
        ])
        self.encias_ctrl = ctrl.ControlSystem([
            rule_encias_1, rule_encias_2, rule_encias_3
        ])
        
        # Crear simulaciones
        try:
            self.caries_sim = ctrl.ControlSystemSimulation(self.caries_ctrl)
            self.pulpitis_sim = ctrl.ControlSystemSimulation(self.pulpitis_ctrl)
            self.infeccion_sim = ctrl.ControlSystemSimulation(self.infeccion_ctrl)
            self.encias_sim = ctrl.ControlSystemSimulation(self.encias_ctrl)
            self.system = True
        except Exception as e:
            print(f"Error al crear simulaciones fuzzy: {e}")
            self.system = None
    
    def evaluate(self, facts):
        """
        Evalúa síntomas usando lógica difusa
        facts: diccionario con síntomas del paciente
        """
        if not FUZZY_AVAILABLE or self.system is None:
            return self._evaluate_simple(facts)
        
        try:
            # Extraer valores
            intensidad = facts.get('intensidad_dolor', 0)
            sensibilidad = max(
                facts.get('sensibilidad_frio', 0),
                facts.get('sensibilidad_calor', 0),
                facts.get('sensibilidad_dulce', 0)
            )
            inflamacion = facts.get('inflamacion_encias', 0)
            
            # Convertir duración a días numéricos
            duracion_map = {
                'menos_24h': 0,
                '1_3_dias': 2,
                '3_7_dias': 5,
                'mas_7_dias': 7
            }
            duracion = duracion_map.get(facts.get('duracion_dolor', 'menos_24h'), 0)
            
            results = []
            
            # Evaluar Caries
            try:
                self.caries_sim.input['intensidad_dolor'] = intensidad
                self.caries_sim.input['sensibilidad'] = sensibilidad
                self.caries_sim.input['duracion_dias'] = duracion
                self.caries_sim.compute()
                prob_caries = self.caries_sim.output['prob_caries']
                if prob_caries > 30:
                    results.append({
                        'diagnostico': 'caries',
                        'confianza': prob_caries / 100,
                        'regla': 'Fuzzy Logic - Caries',
                        'tipo': 'fuzzy'
                    })
            except Exception as e:
                pass
            
            # Evaluar Pulpitis
            try:
                self.pulpitis_sim.input['intensidad_dolor'] = intensidad
                self.pulpitis_sim.input['sensibilidad'] = sensibilidad
                self.pulpitis_sim.input['duracion_dias'] = duracion
                self.pulpitis_sim.compute()
                prob_pulpitis = self.pulpitis_sim.output['prob_pulpitis']
                if prob_pulpitis > 30:
                    results.append({
                        'diagnostico': 'pulpitis',
                        'confianza': prob_pulpitis / 100,
                        'regla': 'Fuzzy Logic - Pulpitis',
                        'tipo': 'fuzzy'
                    })
            except Exception as e:
                pass
            
            # Evaluar Infección
            try:
                self.infeccion_sim.input['intensidad_dolor'] = intensidad
                self.infeccion_sim.input['inflamacion'] = inflamacion
                self.infeccion_sim.input['duracion_dias'] = duracion
                self.infeccion_sim.compute()
                prob_infeccion = self.infeccion_sim.output['prob_infeccion']
                if prob_infeccion > 30:
                    results.append({
                        'diagnostico': 'absceso',
                        'confianza': prob_infeccion / 100,
                        'regla': 'Fuzzy Logic - Infección',
                        'tipo': 'fuzzy'
                    })
            except Exception as e:
                pass
            
            # Evaluar Encías
            try:
                self.encias_sim.input['inflamacion'] = inflamacion
                self.encias_sim.input['intensidad_dolor'] = intensidad
                self.encias_sim.input['duracion_dias'] = duracion
                self.encias_sim.compute()
                prob_encias = self.encias_sim.output['prob_encias']
                if prob_encias > 30:
                    # Determinar si es gingivitis o periodontitis
                    movilidad = facts.get('movilidad_dental', 'no')
                    if movilidad in ['moderado', 'severo']:
                        diag = 'periodontitis'
                    else:
                        diag = 'gingivitis'
                    results.append({
                        'diagnostico': diag,
                        'confianza': prob_encias / 100,
                        'regla': 'Fuzzy Logic - Encías',
                        'tipo': 'fuzzy'
                    })
            except Exception as e:
                pass
            
            return results
            
        except Exception as e:
            print(f"Error en evaluación fuzzy: {e}")
            return self._evaluate_simple(facts)
    
    def _evaluate_simple(self, facts):
        """
        Evaluación difusa simplificada sin scikit-fuzzy
        Usa funciones de pertenencia básicas
        """
        results = []
        
        intensidad = facts.get('intensidad_dolor', 0)
        sensibilidad = max(
            facts.get('sensibilidad_frio', 0),
            facts.get('sensibilidad_calor', 0),
            facts.get('sensibilidad_dulce', 0)
        )
        inflamacion = facts.get('inflamacion_encias', 0)
        
        # Caries: sensibilidad alta + dolor medio
        if sensibilidad >= 5 and intensidad >= 3 and intensidad <= 7:
            confianza = min(sensibilidad, intensidad) / 10
            results.append({
                'diagnostico': 'caries',
                'confianza': confianza,
                'regla': 'Fuzzy Simple - Caries',
                'tipo': 'fuzzy_simple'
            })
        
        # Pulpitis: dolor alto + duración
        if intensidad >= 7:
            duracion = facts.get('duracion_dolor', 'menos_24h')
            if duracion in ['3_7_dias', 'mas_7_dias']:
                confianza = intensidad / 10
                results.append({
                    'diagnostico': 'pulpitis',
                    'confianza': confianza,
                    'regla': 'Fuzzy Simple - Pulpitis',
                    'tipo': 'fuzzy_simple'
                })
        
        # Absceso: inflamación alta + dolor alto
        if inflamacion >= 7 and intensidad >= 7:
            confianza = min(inflamacion, intensidad) / 10
            results.append({
                'diagnostico': 'absceso',
                'confianza': confianza,
                'regla': 'Fuzzy Simple - Infección',
                'tipo': 'fuzzy_simple'
            })
        
        # Problemas de encías: inflamación alta + dolor bajo
        if inflamacion >= 5 and intensidad <= 5:
            movilidad = facts.get('movilidad_dental', 'no')
            if movilidad in ['moderado', 'severo']:
                diag = 'periodontitis'
            else:
                diag = 'gingivitis'
            confianza = inflamacion / 10
            results.append({
                'diagnostico': diag,
                'confianza': confianza,
                'regla': 'Fuzzy Simple - Encías',
                'tipo': 'fuzzy_simple'
            })
        
        return results


# Instancia global del sistema fuzzy
_fuzzy_system = None

def get_fuzzy_system():
    """Obtiene la instancia del sistema fuzzy (singleton)"""
    global _fuzzy_system
    if _fuzzy_system is None:
        _fuzzy_system = FuzzyDiagnosisSystem()
    return _fuzzy_system


def evaluate_fuzzy_rules(facts):
    """
    Evalúa reglas difusas y retorna diagnósticos
    """
    fuzzy_sys = get_fuzzy_system()
    return fuzzy_sys.evaluate(facts)
