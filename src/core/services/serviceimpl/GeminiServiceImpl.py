import json
from fastapi import params
import google.generativeai as genai
from src.core.services.interface.IA_ServiceInterface import IA_ServiceInterface
from src.feature.generateActivity.domain.entity.Activity import ActividadSugerida, GeneradorParametros

class GeminiServiceImpl(IA_ServiceInterface):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=(
                "Eres un guía experto en bienestar y psicología del ocio. "
                "Tu objetivo es sugerir actividades que desconecten al usuario del estrés "
                "y recarguen su energía de forma creativa y amena. "
                "Evita el lenguaje demasiado técnico; habla de forma cercana y motivadora."
            )
        )

    async def generar_actividad_dopamina(self, params: GeneradorParametros) -> ActividadSugerida:
        intereses_texto = ", ".join(params.userInterests)
        temas_texto = ", ".join(params.userTopics)
        
        prompt = f"""
            Actúa como un experto en Psicología del Ocio. 
            Tu tarea es crear una actividad personalizada basada en una 'Plantilla' y el 'Perfil del Usuario'.

            PERFIL DEL USUARIO:
            - Nombre: {params.userName}
            - Intereses: {intereses_texto}
            - Temas actuales: {temas_texto}
            - Estilo de ocio preferido: {params.userLeisureType}

            PLANTILLA BASE (Inspiración):
            - Idea original: {params.templateActivity}
            - Tipo: {params.templateType}
            - Participantes: {params.templateParticipants}
            - Duración sugerida: {params.templateDuration}

            INSTRUCCIONES:
            1. No copies la plantilla, adáptala a los intereses del usuario.
            2. Si la plantilla es "{params.templateActivity}", ¿cómo sería una versión para alguien que le gusta {intereses_texto}?
            3. Define si es una actividad "Social" o "Individual" basado en los participantes ({params.templateParticipants}).

            RESPONDE ÚNICAMENTE EN JSON CON ESTE FORMATO:
            {{
                "titulo": "Título creativo",
                "descripcion": "Máximo 120 caracteres (debe ser breve)",
                "type": "tipo de ocio Pasivo o Activo",
                "categoria": "{params.templateType}",
                "duracionEstimada": "Duración en minutos numerico",
                "socialType": "Social o No social"
            }}
        """
        
        response = self.model.generate_content(prompt)
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_json)
        
        return ActividadSugerida(**data)