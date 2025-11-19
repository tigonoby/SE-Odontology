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

# Diagnósticos posibles - BASE DE CONOCIMIENTOS EXPANDIDA
DIAGNOSTICOS = {
    # CARIES Y LESIONES DEL ESMALTE
    "caries": {
        "nombre": "Caries Dental",
        "descripcion": "Deterioro del esmalte y dentina causado por ácidos bacterianos",
        "gravedad": "media",
        "urgencia": "moderada"
    },
    "caries_inicial": {
        "nombre": "Caries Inicial (Etapa Temprana)",
        "descripcion": "Inicio de desmineralización del esmalte, reversible con tratamiento",
        "gravedad": "baja",
        "urgencia": "moderada"
    },
    "caries_profunda": {
        "nombre": "Caries Profunda",
        "descripcion": "Caries que ha alcanzado la dentina profunda, cerca de la pulpa",
        "gravedad": "alta",
        "urgencia": "alta"
    },
    "caries_radicular": {
        "nombre": "Caries Radicular",
        "descripcion": "Caries en la raíz del diente expuesta por retracción gingival",
        "gravedad": "alta",
        "urgencia": "alta"
    },
    
    # PULPA DENTAL
    "pulpitis": {
        "nombre": "Pulpitis Irreversible",
        "descripcion": "Inflamación severa de la pulpa dental que no se puede revertir",
        "gravedad": "muy_alta",
        "urgencia": "urgente"
    },
    "pulpitis_reversible": {
        "nombre": "Pulpitis Reversible",
        "descripcion": "Inflamación leve de la pulpa que puede revertirse con tratamiento",
        "gravedad": "media",
        "urgencia": "alta"
    },
    "necrosis_pulpar": {
        "nombre": "Necrosis Pulpar",
        "descripcion": "Muerte del tejido pulpar, requiere tratamiento de conducto",
        "gravedad": "muy_alta",
        "urgencia": "urgente"
    },
    
    # INFECCIONES
    "absceso": {
        "nombre": "Absceso Dental Agudo",
        "descripcion": "Infección aguda con acumulación de pus",
        "gravedad": "muy_alta",
        "urgencia": "urgente"
    },
    "absceso_cronico": {
        "nombre": "Absceso Dental Crónico",
        "descripcion": "Infección de larga duración con drenaje intermitente",
        "gravedad": "alta",
        "urgencia": "alta"
    },
    "celulitis_facial": {
        "nombre": "Celulitis Facial",
        "descripcion": "Infección que se extiende a tejidos blandos faciales",
        "gravedad": "muy_alta",
        "urgencia": "emergencia"
    },
    
    # ENFERMEDADES PERIODONTALES
    "gingivitis": {
        "nombre": "Gingivitis",
        "descripcion": "Inflamación de las encías causada por placa bacteriana",
        "gravedad": "baja",
        "urgencia": "moderada"
    },
    "gingivitis_aguda": {
        "nombre": "Gingivitis Aguda",
        "descripcion": "Inflamación aguda de encías con dolor y sangrado intenso",
        "gravedad": "media",
        "urgencia": "alta"
    },
    "periodontitis": {
        "nombre": "Periodontitis Crónica",
        "descripcion": "Enfermedad periodontal con pérdida de soporte óseo",
        "gravedad": "alta",
        "urgencia": "alta"
    },
    "periodontitis_agresiva": {
        "nombre": "Periodontitis Agresiva",
        "descripcion": "Pérdida rápida de hueso y tejido periodontal",
        "gravedad": "muy_alta",
        "urgencia": "urgente"
    },
    "absceso_periodontal": {
        "nombre": "Absceso Periodontal",
        "descripcion": "Acumulación de pus en el tejido periodontal",
        "gravedad": "alta",
        "urgencia": "urgente"
    },
    
    # SENSIBILIDAD Y DESGASTE
    "sensibilidad": {
        "nombre": "Hipersensibilidad Dentinaria",
        "descripcion": "Sensibilidad dental a estímulos térmicos o táctiles",
        "gravedad": "baja",
        "urgencia": "baja"
    },
    "erosion_dental": {
        "nombre": "Erosión Dental",
        "descripcion": "Pérdida de esmalte por ácidos no bacterianos",
        "gravedad": "media",
        "urgencia": "moderada"
    },
    "abrasion_dental": {
        "nombre": "Abrasión Dental",
        "descripcion": "Desgaste dental por fricción mecánica",
        "gravedad": "media",
        "urgencia": "baja"
    },
    
    # TRAUMA Y FRACTURAS
    "fractura_dental": {
        "nombre": "Fractura Dental",
        "descripcion": "Rotura del diente por trauma o debilitamiento",
        "gravedad": "alta",
        "urgencia": "alta"
    },
    "fisura_dental": {
        "nombre": "Fisura o Grieta Dental",
        "descripcion": "Pequeña fractura en el esmalte dental",
        "gravedad": "media",
        "urgencia": "moderada"
    },
    
    # TRASTORNOS FUNCIONALES
    "bruxismo": {
        "nombre": "Bruxismo",
        "descripcion": "Rechinamiento involuntario de dientes",
        "gravedad": "media",
        "urgencia": "moderada"
    },
    "atm_disfuncion": {
        "nombre": "Disfunción de ATM",
        "descripcion": "Problemas en la articulación temporomandibular",
        "gravedad": "media",
        "urgencia": "moderada"
    },
    
    # PROBLEMAS POST-TRATAMIENTO
    "dolor_post_obturacion": {
        "nombre": "Dolor Post-Obturación",
        "descripcion": "Molestias después de empaste dental reciente",
        "gravedad": "baja",
        "urgencia": "baja"
    },
    "sensibilidad_post_tratamiento": {
        "nombre": "Sensibilidad Post-Tratamiento",
        "descripcion": "Sensibilidad temporal después de procedimiento dental",
        "gravedad": "baja",
        "urgencia": "baja"
    },
    "fracaso_endodoncia": {
        "nombre": "Fallo de Tratamiento de Conducto",
        "descripcion": "Reinfección o problemas tras endodoncia",
        "gravedad": "alta",
        "urgencia": "alta"
    },
    
    # OTROS
    "ortodoncia": {
        "nombre": "Problema de Ortodoncia",
        "descripcion": "Maloclusión o desalineación dental",
        "gravedad": "baja",
        "urgencia": "baja"
    },
    "impactacion_alimentaria": {
        "nombre": "Impactación de Alimentos",
        "descripcion": "Alimentos atrapados entre dientes causando molestia",
        "gravedad": "baja",
        "urgencia": "baja"
    },
    "evaluacion_general": {
        "nombre": "Evaluación Preventiva Recomendada",
        "descripcion": "No se detectaron problemas graves - chequeo preventivo sugerido",
        "gravedad": "baja",
        "urgencia": "baja"
    }
}

# Recomendaciones por diagnóstico - EXPANDIDAS
RECOMENDACIONES = {
    # CARIES
    "caries": [
        "Consulte a su odontólogo lo antes posible",
        "Evite alimentos y bebidas azucaradas",
        "Mantenga higiene oral rigurosa (cepillado 3x/día)",
        "Use hilo dental diariamente",
        "Enjuague con agua tibia con sal si hay molestias",
        "No mastique del lado afectado"
    ],
    "caries_inicial": [
        "Agende cita odontológica pronto",
        "Mejore su higiene dental inmediatamente",
        "Reduzca drásticamente consumo de azúcares",
        "Use pasta dental con flúor",
        "El tratamiento temprano evita complicaciones",
        "Evite bebidas ácidas y carbonatadas"
    ],
    "caries_profunda": [
        "URGENTE: Requiere atención odontológica inmediata",
        "Puede necesitar tratamiento de conducto",
        "Evite masticar en el área afectada",
        "No consuma alimentos muy fríos o calientes",
        "Tome analgésicos si el dolor es severo",
        "No demore la consulta - riesgo de infección"
    ],
    "caries_radicular": [
        "Consulte a su odontólogo urgentemente",
        "Requiere tratamiento especializado",
        "Use pasta para dientes sensibles",
        "Evite cepillado agresivo",
        "Puede necesitar restauración o injerto",
        "Control periodontal es esencial"
    ],
    
    # PULPA
    "pulpitis": [
        "¡URGENTE! Consulte odontólogo HOY mismo",
        "Evite temperaturas extremas en alimentos",
        "Puede tomar analgésicos (ibuprofeno, paracetamol)",
        "NO aplique calor externo en la mejilla",
        "Evite masticar con el diente afectado",
        "Probablemente necesite tratamiento de conducto"
    ],
    "pulpitis_reversible": [
        "Visite a su odontólogo en 24-48 horas",
        "Evite alimentos muy fríos o calientes",
        "Puede requerir obturación profunda",
        "No ignore el síntoma - puede empeorar rápidamente",
        "Mantenga excelente higiene dental",
        "Evite dulces y ácidos"
    ],
    "necrosis_pulpar": [
        "EMERGENCIA: Atención odontológica inmediata",
        "Requiere tratamiento de conducto urgente",
        "Alto riesgo de infección y absceso",
        "NO espere - busque atención hoy",
        "Puede necesitar antibióticos",
        "Evite presionar el diente afectado"
    ],
    
    # INFECCIONES
    "absceso": [
        "¡EMERGENCIA DENTAL! Busque atención inmediata",
        "NO drene el absceso por su cuenta",
        "Enjuagues con agua tibia y sal (cada 2 horas)",
        "Tome analgésicos para el dolor",
        "Si hay fiebre >38°C, vaya a urgencias médicas",
        "Puede requerir antibióticos y drenaje quirúrgico"
    ],
    "absceso_cronico": [
        "Consulte a su odontólogo urgentemente",
        "Requiere tratamiento definitivo pronto",
        "Enjuagues antisépticos bucales",
        "Puede necesitar extracción o endodoncia",
        "No ignore - puede causar daño óseo",
        "Evite el tabaco absolutamente"
    ],
    "celulitis_facial": [
        "¡EMERGENCIA MÉDICA! Vaya a urgencias YA",
        "Infección grave que puede diseminarse",
        "Requiere antibióticos intravenosos",
        "Puede necesitar hospitalización",
        "NO espere - busque atención inmediata",
        "Riesgo de complicaciones sistémicas graves"
    ],
    
    # PERIODONTALES
    "gingivitis": [
        "Mejore técnica de cepillado (2-3 min, 3x/día)",
        "Use hilo dental TODOS los días",
        "Enjuague bucal antiséptico (clorhexidina)",
        "Agende limpieza dental profesional",
        "Evite el tabaco completamente",
        "Controle estrés y alimentación"
    ],
    "gingivitis_aguda": [
        "Consulte a su odontólogo en 24 horas",
        "Enjuagues con agua tibia y sal frecuentes",
        "Cepillado suave pero completo",
        "Use cepillo de cerdas suaves",
        "Puede necesitar limpieza profesional urgente",
        "Evite alimentos muy duros o irritantes"
    ],
    "periodontitis": [
        "Consulte a periodoncista URGENTEMENTE",
        "Requiere limpieza profunda (raspado/alisado radicular)",
        "Higiene oral impecable es crítica",
        "NO fume - empeora severamente",
        "Puede necesitar cirugía periodontal",
        "Control cada 3-4 meses es esencial"
    ],
    "periodontitis_agresiva": [
        "URGENTE: Atención periodontal especializada HOY",
        "Pérdida ósea rápida - no demore",
        "Requiere tratamiento agresivo inmediato",
        "Probablemente necesite antibióticos",
        "Puede necesitar cirugía",
        "Elimine tabaco y controle diabetes si la tiene"
    ],
    "absceso_periodontal": [
        "Consulte periodoncista urgentemente (hoy)",
        "Requiere drenaje y limpieza profunda",
        "Enjuagues antisépticos frecuentes",
        "Puede necesitar antibióticos",
        "NO drene usted mismo",
        "Evite presionar la zona afectada"
    ],
    
    # SENSIBILIDAD Y DESGASTE
    "sensibilidad": [
        "Use pasta dental para dientes sensibles",
        "Cepillo de cerdas extra suaves",
        "Evite cepillado horizontal agresivo",
        "Limite alimentos ácidos (cítricos, refrescos)",
        "Consulte para descartar causas subyacentes",
        "Puede necesitar barniz de flúor profesional"
    ],
    "erosion_dental": [
        "Consulte a su odontólogo",
        "Identifique fuente de ácido (reflujo, dieta, etc)",
        "Evite bebidas ácidas (sodas, jugos cítricos)",
        "Enjuague con agua después de vómitos/reflujo",
        "No cepille inmediatamente después de ácidos",
        "Puede necesitar restauraciones protectoras"
    ],
    "abrasion_dental": [
        "Corrija técnica de cepillado (circular suave)",
        "Use cepillo de cerdas suaves",
        "Evite pastas abrasivas/blanqueadoras",
        "Consulte para evaluar restauraciones",
        "Identifique hábitos abrasivos",
        "Puede necesitar coronas o carillas"
    ],
    
    # TRAUMA
    "fractura_dental": [
        "Consulte a su odontólogo HOY mismo",
        "Guarde el fragmento si lo encuentra (en leche/saliva)",
        "Evite masticar en ese lado",
        "Enjuague suavemente con agua tibia",
        "Tome analgésico si hay dolor",
        "Tratamiento depende de extensión de fractura"
    ],
    "fisura_dental": [
        "Agende cita odontológica pronto",
        "Evite alimentos muy duros",
        "No muerda hielo o objetos duros",
        "Puede necesitar corona protectora",
        "Monitoree síntomas (dolor, sensibilidad)",
        "Tratamiento temprano previene fractura completa"
    ],
    
    # FUNCIONALES
    "bruxismo": [
        "Consulte para férula de descarga nocturna",
        "Técnicas de manejo de estrés/ansiedad",
        "Evite cafeína 4-6 horas antes de dormir",
        "Ejercicios de relajación mandibular",
        "No mastique chicle",
        "Fisioterapia de ATM si hay dolor"
    ],
    "atm_disfuncion": [
        "Consulte especialista en ATM",
        "Dieta blanda por 2-3 semanas",
        "Evite abrir boca en exceso",
        "Compresas tibias en la articulación",
        "Antiinflamatorios si hay dolor",
        "Puede necesitar férula oclusal"
    ],
    
    # POST-TRATAMIENTO
    "dolor_post_obturacion": [
        "Normal hasta 2-3 días post-tratamiento",
        "Evite masticar en ese lado 24 horas",
        "Analgésicos leves si es necesario",
        "Si persiste >1 semana, contacte odontólogo",
        "Evite temperaturas extremas inicialmente",
        "Mejorará gradualmente"
    ],
    "sensibilidad_post_tratamiento": [
        "Sensibilidad temporal es común",
        "Use pasta para dientes sensibles",
        "Evite temperaturas extremas 1-2 semanas",
        "Debería mejorar en 2-4 semanas",
        "Si empeora o persiste, consulte",
        "Mantenga buena higiene oral"
    ],
    "fracaso_endodoncia": [
        "Consulte endodoncista urgentemente",
        "Puede necesitar retratamiento",
        "Posible reinfección - requiere evaluación",
        "No demore - puede empeorar",
        "Radiografías necesarias para diagnóstico",
        "Alternativa: extracción e implante"
    ],
    
    # OTROS
    "ortodoncia": [
        "Consulte a ortodoncista",
        "Evaluación para tratamiento ortodóntico",
        "Mejora función masticatoria y estética",
        "Tratamiento temprano previene complicaciones",
        "Considere alineadores invisibles si prefiere",
        "Inversión en salud y autoestima"
    ],
    "impactacion_alimentaria": [
        "Use hilo dental para remover alimentos",
        "Irrigador bucal puede ayudar",
        "Consulte si es recurrente",
        "Puede indicar problema en contacto dental",
        "Restauraciones o ajustes pueden ser necesarios",
        "No use palillos - pueden dañar encías"
    ],
    "evaluacion_general": [
        "Mantenga chequeos dentales cada 6 meses",
        "Continue con buena higiene oral",
        "Cepillado 2-3 veces al día (2 minutos)",
        "Use hilo dental diariamente",
        "Dieta balanceada, limite azúcares",
        "¡Felicidades por mantener salud dental!"
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
