"""
Motor de Diagnóstico
Coordina el uso de reglas crisp y fuzzy para generar diagnósticos
"""

from ..base_conocimiento import (
    evaluate_crisp_rules,
    evaluate_fuzzy_rules,
    get_diagnostico_info,
    get_recomendaciones
)
from .encadenamiento_adelante import ForwardChainingEngine, apply_conflict_resolution
from ..base_conocimiento.reglas_crisp import get_all_rules


class MotorDiagnostico:
    """
    Motor de diagnóstico que combina reglas crisp y fuzzy
    """
    
    def __init__(self):
        self.crisp_engine = ForwardChainingEngine(get_all_rules())
        self.last_facts = None
        self.last_results = None
    
    def diagnose(self, facts, use_fuzzy=True, strategy='combine'):
        """
        Realiza el diagnóstico basado en los síntomas
        SIEMPRE retorna un resultado, incluso con datos mínimos
        
        Args:
            facts: diccionario con síntomas del paciente
            use_fuzzy: si se debe usar lógica difusa
            strategy: estrategia de resolución de conflictos
        
        Returns:
            diccionario con diagnósticos y recomendaciones
        """
        self.last_facts = facts.copy()
        
        # Evaluar reglas crisp
        crisp_results = evaluate_crisp_rules(facts)
        
        # Evaluar reglas fuzzy si está habilitado
        fuzzy_results = []
        if use_fuzzy:
            try:
                fuzzy_results = evaluate_fuzzy_rules(facts)
            except Exception as e:
                print(f"Error en evaluación fuzzy: {e}")
        
        # Combinar resultados
        all_results = crisp_results + fuzzy_results
        
        # Si no hay resultados, generar diagnóstico por defecto basado en síntomas
        if not all_results:
            all_results = self._generate_fallback_diagnosis(facts)
        
        # Aplicar resolución de conflictos
        resolved_results = apply_conflict_resolution(all_results, strategy)
        
        # Ordenar por confianza
        resolved_results.sort(key=lambda x: x['confianza'], reverse=True)
        
        # Enriquecer con información adicional
        enriched_results = []
        for result in resolved_results:
            diagnostico = result['diagnostico']
            info = get_diagnostico_info(diagnostico)
            recomendaciones = get_recomendaciones(diagnostico)
            
            enriched = {
                'diagnostico': diagnostico,
                'nombre': info['nombre'] if info else diagnostico,
                'descripcion': info['descripcion'] if info else '',
                'gravedad': info['gravedad'] if info else 'desconocida',
                'urgencia': info['urgencia'] if info else 'desconocida',
                'confianza': result['confianza'],
                'confianza_porcentaje': round(result['confianza'] * 100, 1),
                'regla': result['regla'],
                'tipo_regla': result['tipo'],
                'recomendaciones': recomendaciones
            }
            enriched_results.append(enriched)
        
        self.last_results = enriched_results
        
        return {
            'diagnosticos': enriched_results,
            'num_diagnosticos': len(enriched_results),
            'principal': enriched_results[0] if enriched_results else None,
            'sintomas_evaluados': len(facts),
            'usa_logica_fuzzy': use_fuzzy
        }
    
    def _generate_fallback_diagnosis(self, facts):
        """
        Genera diagnóstico de respaldo cuando no hay coincidencias de reglas
        Analiza los síntomas principales y sugiere posibles condiciones
        """
        fallback_results = []
        
        # Extraer síntomas
        intensidad_dolor = facts.get('intensidad_dolor', 0)
        sensibilidad_frio = facts.get('sensibilidad_frio', 0)
        sensibilidad_calor = facts.get('sensibilidad_calor', 0)
        sensibilidad_dulce = facts.get('sensibilidad_dulce', 0)
        inflamacion_encias = facts.get('inflamacion_encias', 0)
        dolor_masticar = facts.get('dolor_masticar', 0)
        dolor_nocturno = facts.get('dolor_nocturno', 0)
        dolor_presion = facts.get('dolor_presion', 0)
        
        # Variables categóricas importantes
        caries_visible = facts.get('caries_visible', 'no')
        mancha_oscura = facts.get('mancha_oscura', 'no')
        hinchazon_cara = facts.get('hinchazon_cara', 'no')
        sangrado_encias = facts.get('sangrado_encias', 'no')
        movilidad_dental = facts.get('movilidad_dental', 'no')
        
        # Análisis por prioridad de gravedad
        
        # 1. ABSCESO/INFECCIÓN (Prioridad máxima)
        if hinchazon_cara == 'si' or facts.get('pus_visible') == 'si' or facts.get('fiebre') == 'si':
            confianza = 0.7 if hinchazon_cara == 'si' else 0.65
            if intensidad_dolor >= 7:
                confianza = min(confianza + 0.15, 0.95)
            fallback_results.append({
                'diagnostico': 'absceso',
                'confianza': confianza,
                'regla': 'Análisis Inteligente - Signos de infección detectados',
                'tipo': 'fallback_inteligente'
            })
            return fallback_results  # Retornar inmediatamente por gravedad
        
        # 2. PULPITIS (Dolor intenso con sensibilidad al calor)
        if intensidad_dolor >= 7 or (dolor_nocturno >= 6 and sensibilidad_calor >= 6):
            confianza = 0.6 + (intensidad_dolor / 30) + (sensibilidad_calor / 40)
            confianza = min(confianza, 0.85)
            fallback_results.append({
                'diagnostico': 'pulpitis',
                'confianza': confianza,
                'regla': 'Análisis Inteligente - Dolor severo y características de pulpitis',
                'tipo': 'fallback_inteligente'
            })
        
        # 3. CARIES (Caries visible o mancha + sensibilidad)
        if caries_visible == 'si' or (mancha_oscura == 'si' and (sensibilidad_dulce >= 4 or sensibilidad_frio >= 4)):
            base_conf = 0.75 if caries_visible == 'si' else 0.6
            confianza = base_conf + (sensibilidad_dulce / 40)
            confianza = min(confianza, 0.88)
            fallback_results.append({
                'diagnostico': 'caries',
                'confianza': confianza,
                'regla': 'Análisis Inteligente - Evidencia visual de caries',
                'tipo': 'fallback_inteligente'
            })
        
        # 4. PERIODONTITIS (Movilidad dental + sangrado)
        if movilidad_dental in ['moderado', 'severo'] or (movilidad_dental == 'leve' and sangrado_encias in ['moderado', 'severo']):
            confianza = 0.65 + (inflamacion_encias / 30)
            confianza = min(confianza, 0.82)
            fallback_results.append({
                'diagnostico': 'periodontitis',
                'confianza': confianza,
                'regla': 'Análisis Inteligente - Signos de enfermedad periodontal',
                'tipo': 'fallback_inteligente'
            })
        
        # 5. GINGIVITIS (Inflamación de encías sin movilidad)
        elif inflamacion_encias >= 5 or sangrado_encias in ['moderado', 'severo']:
            confianza = 0.55 + (inflamacion_encias / 25)
            confianza = min(confianza, 0.8)
            fallback_results.append({
                'diagnostico': 'gingivitis',
                'confianza': confianza,
                'regla': 'Análisis Inteligente - Inflamación gingival',
                'tipo': 'fallback_inteligente'
            })
        
        # 6. SENSIBILIDAD (Sensibilidad sin caries visible)
        if sensibilidad_frio >= 5 and caries_visible != 'si' and intensidad_dolor <= 6:
            confianza = 0.5 + (sensibilidad_frio / 25)
            confianza = min(confianza, 0.75)
            fallback_results.append({
                'diagnostico': 'sensibilidad',
                'confianza': confianza,
                'regla': 'Análisis Inteligente - Hipersensibilidad dentinaria',
                'tipo': 'fallback_inteligente'
            })
        
        # 7. CARIES INICIAL (Sensibilidad leve sin otros signos)
        if (sensibilidad_dulce >= 3 or sensibilidad_frio >= 3) and intensidad_dolor >= 2 and intensidad_dolor < 7:
            if not fallback_results:  # Solo si no hay otros diagnósticos
                confianza = 0.45 + ((sensibilidad_dulce + sensibilidad_frio) / 40)
                confianza = min(confianza, 0.68)
                fallback_results.append({
                    'diagnostico': 'caries_inicial',
                    'confianza': confianza,
                    'regla': 'Análisis Inteligente - Posible inicio de caries',
                    'tipo': 'fallback_inteligente'
                })
        
        # 8. Evaluación general (solo si realmente no hay síntomas)
        if not fallback_results:
            # Verificar si hay ALGÚN síntoma
            sintomas_presentes = (
                intensidad_dolor > 0 or sensibilidad_frio > 0 or sensibilidad_calor > 0 or
                sensibilidad_dulce > 0 or inflamacion_encias > 0 or dolor_masticar > 0 or
                dolor_nocturno > 0 or dolor_presion > 0
            )
            
            if sintomas_presentes:
                # Hay síntomas pero son muy leves
                max_sintoma = max(intensidad_dolor, sensibilidad_frio, sensibilidad_calor,
                                 sensibilidad_dulce, inflamacion_encias, dolor_masticar,
                                 dolor_nocturno, dolor_presion)
                
                if max_sintoma >= 2:
                    confianza = 0.4 + (max_sintoma / 30)
                    fallback_results.append({
                        'diagnostico': 'caries_inicial',
                        'confianza': min(confianza, 0.6),
                        'regla': 'Análisis Inteligente - Síntomas leves detectados',
                        'tipo': 'fallback_inteligente'
                    })
                else:
                    fallback_results.append({
                        'diagnostico': 'evaluacion_general',
                        'confianza': 0.3,
                        'regla': 'Recomendación - Evaluación preventiva sugerida',
                        'tipo': 'fallback_preventivo'
                    })
            else:
                # No hay síntomas en absoluto
                fallback_results.append({
                    'diagnostico': 'evaluacion_general',
                    'confianza': 0.25,
                    'regla': 'Recomendación - Sin síntomas significativos, evaluación preventiva',
                    'tipo': 'fallback_preventivo'
                })
        
        return fallback_results
    
    def get_explanation(self):
        """
        Proporciona una explicación del proceso de diagnóstico
        """
        if not self.last_facts or not self.last_results:
            return "No hay diagnóstico previo para explicar."
        
        explanation = {
            'sintomas_clave': self._identify_key_symptoms(),
            'reglas_aplicadas': [r['regla'] for r in self.last_results],
            'razonamiento': self._generate_reasoning()
        }
        
        return explanation
    
    def _identify_key_symptoms(self):
        """Identifica los síntomas más relevantes para el diagnóstico"""
        key_symptoms = []
        
        if not self.last_facts:
            return key_symptoms
        
        # Síntomas numéricos significativos
        numeric_symptoms = [
            'intensidad_dolor',
            'sensibilidad_frio',
            'sensibilidad_calor',
            'dolor_masticar',
            'inflamacion_encias'
        ]
        
        for symptom in numeric_symptoms:
            value = self.last_facts.get(symptom, 0)
            if value >= 5:
                key_symptoms.append({
                    'sintoma': symptom,
                    'valor': value,
                    'relevancia': 'alta' if value >= 7 else 'media'
                })
        
        # Síntomas categóricos importantes
        if self.last_facts.get('caries_visible') == 'si':
            key_symptoms.append({
                'sintoma': 'caries_visible',
                'valor': 'si',
                'relevancia': 'alta'
            })
        
        if self.last_facts.get('hinchazon_cara') == 'si':
            key_symptoms.append({
                'sintoma': 'hinchazon_cara',
                'valor': 'si',
                'relevancia': 'muy_alta'
            })
        
        return key_symptoms
    
    def _generate_reasoning(self):
        """Genera una explicación del razonamiento"""
        if not self.last_results:
            return "No se pudo generar un diagnóstico con los síntomas proporcionados."
        
        principal = self.last_results[0]
        
        reasoning = f"Basándose en los síntomas reportados, el diagnóstico más probable es "
        reasoning += f"{principal['nombre']} con una confianza del {principal['confianza_porcentaje']}%. "
        reasoning += f"\n\nEsto se determinó mediante {principal['regla']}. "
        reasoning += f"\n\nDescripción: {principal['descripcion']}"
        
        if len(self.last_results) > 1:
            reasoning += f"\n\nOtros diagnósticos posibles incluyen: "
            otros = [r['nombre'] for r in self.last_results[1:3]]
            reasoning += ", ".join(otros)
        
        return reasoning
    
    def validate_symptoms(self, facts):
        """
        Valida que los síntomas proporcionados sean coherentes
        """
        warnings = []
        
        # Validar rangos numéricos
        numeric_fields = [
            'intensidad_dolor', 'sensibilidad_frio', 'sensibilidad_calor',
            'sensibilidad_dulce', 'dolor_masticar', 'dolor_presion',
            'dolor_nocturno', 'inflamacion_encias', 'dolor_mandibula'
        ]
        
        for field in numeric_fields:
            value = facts.get(field, 0)
            if not isinstance(value, (int, float)) or value < 0 or value > 10:
                warnings.append(f"Valor inválido para {field}: debe estar entre 0 y 10")
        
        # Validaciones de coherencia
        # Si hay hinchazón facial, debería haber dolor alto
        if facts.get('hinchazon_cara') == 'si':
            if facts.get('intensidad_dolor', 0) < 5:
                warnings.append("Advertencia: hinchazón facial generalmente está asociada con dolor significativo")
        
        # Si hay pus, debería haber infección
        if facts.get('pus_visible') == 'si':
            if facts.get('hinchazon_cara') != 'si' and facts.get('inflamacion_encias', 0) < 5:
                warnings.append("Advertencia: presencia de pus usualmente indica inflamación significativa")
        
        return {
            'valido': len(warnings) == 0,
            'advertencias': warnings
        }
    
    def get_urgency_level(self):
        """
        Determina el nivel de urgencia basado en los diagnósticos
        """
        if not self.last_results:
            return 'desconocida'
        
        urgencias = [r['urgencia'] for r in self.last_results]
        
        if 'urgente' in urgencias:
            return 'urgente'
        elif 'alta' in urgencias:
            return 'alta'
        elif 'moderada' in urgencias:
            return 'moderada'
        else:
            return 'baja'
    
    def generate_summary(self):
        """
        Genera un resumen del diagnóstico
        """
        if not self.last_results:
            return {
                'tiene_diagnostico': False,
                'mensaje': 'No se pudo determinar un diagnóstico con los síntomas proporcionados.'
            }
        
        principal = self.last_results[0]
        urgencia = self.get_urgency_level()
        
        # Mensaje de urgencia
        urgencia_msg = {
            'urgente': '🚨 ATENCIÓN URGENTE REQUERIDA',
            'alta': '⚠️ Consulte a un odontólogo pronto',
            'moderada': '📅 Agende una cita odontológica',
            'baja': 'ℹ️ Considere una evaluación odontológica'
        }
        
        summary = {
            'tiene_diagnostico': True,
            'diagnostico_principal': principal['nombre'],
            'confianza': principal['confianza_porcentaje'],
            'descripcion': principal['descripcion'],
            'urgencia': urgencia,
            'mensaje_urgencia': urgencia_msg.get(urgencia, ''),
            'num_diagnosticos_alternativos': len(self.last_results) - 1,
            'recomendaciones_principales': principal['recomendaciones'][:3]
        }
        
        return summary
