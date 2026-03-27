import json
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

    async def generar_chat(self, contexto: UsuarioContexto) -> str:
        prompt = f"Contexto: {contexto.contexto_extra}\nPregunta: {contexto.mensaje}"
        response = self.model.generate_content(prompt)
        return response.text

    async def generar_actividad_dopamina(self, params: GeneradorParametros) -> ActividadSugerida:
        prompt = f"""
            Genera una actividad de ocio saludable para un usuario con estas características:
            - Estado de ánimo: {params.estado_animo}
            - Intereses: {params.intereses}
            - Tiempo disponible: {params.tiempo_disponible}
            - Hora del día: {params.hora_actual}

            REGLAS PARA LA DESCRIPCIÓN:
            1. Explica el 'QUÉ' hacer de forma sencilla y motivadora.
            2. Explica el 'POR QUÉ' le ayudará (enfocado al bienestar emocional, no médico).
            3. Usa un tono que invite a la acción inmediata.
            4. Máximo 3 oraciones cortas.

            Responde ÚNICAMENTE en este formato JSON:
            {{
                "titulo": "Nombre creativo de la actividad",
                "descripcion": "Descripción amigable y clara",
                "categoria": "Ocio Creativo / Relajación / Activo",
                "duracion_estimada": "{params.tiempo_disponible}"
            }}
        """
        
        response = self.model.generate_content(prompt)
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_json)
        return ActividadSugerida(**data)