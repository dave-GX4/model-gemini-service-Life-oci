import json
from fastapi import params
import google.generativeai as genai
from src.core.services.interface.IA_ServiceInterface import IA_ServiceInterface
from src.feature.chat.domain.entity.Message import UsuarioContexto
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
        prompt = f"""
            Actúa como un experto en Psicología del Ocio. 
            Tu tarea es crear una actividad personalizada basada en una 'Plantilla' y el 'Perfil del Usuario'.

            PERFIL DEL USUARIO:
            - Nombre: {params.user_name}
            - Intereses: {params.user_interests}
            - Temas actuales: {params.user_topics}
            - Estilo de ocio preferido: {params.user_leisure_type}

            PLANTILLA BASE (Inspiración):
            - Idea original: {params.template_activity}
            - Tipo: {params.template_type}
            - Participantes: {params.template_participants}
            - Duración sugerida: {params.template_duration}

            INSTRUCCIONES:
            1. No copies la plantilla, adáptala a los intereses del usuario.
            2. Si la plantilla es "{params.template_activity}", ¿cómo sería una versión para alguien que le gusta {params.user_interests}?
            3. Define si es una actividad "Social" o "Individual" basado en los participantes ({params.template_participants}).

            RESPONDE ÚNICAMENTE EN JSON CON ESTE FORMATO:
            {{
                "titulo": "Título creativo",
                "descripcion": "Máximo 120 caracteres (debe ser breve)",
                "categoria": "{params.template_type}",
                "duracion_estimada": "{params.template_duration}",
                "socialType": "Social o No social"
            }}
        """
        
        response = self.model.generate_content(prompt)
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_json)
        
        # Retornamos la entidad de dominio
        return ActividadSugerida(**data)