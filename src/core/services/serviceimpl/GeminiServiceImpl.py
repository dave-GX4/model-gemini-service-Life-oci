import json

from core.services.interface.IA_ServiceInterface import IA_ServiceInterface
from feature.chat.domain.entity.message import UsuarioContexto
from feature.generateActivity.domain.entity.activity import ActividadSugerida, GeneradorParametros


class GeminiServiceImpl(IA_ServiceInterface):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model="gemini-1.5-flash",
            system_instruction="Eres un asistente financiero sarcástico. Responde brevemente."
        )

    async def generar_chat(self, contexto: UsuarioContexto) -> str:
        prompt = f"Contexto: {contexto.contexto_extra}\nPregunta: {contexto.mensaje}"
        response = self.model.generate_content(prompt)
        return response.text

    async def generar_actividad_dopamina(self, params: GeneradorParametros) -> ActividadSugerida:
        prompt = f"""Actúa como experto en neurociencia... 
        Datos: {params.estado_animo}, {params.intereses}... 
        Responde ÚNICAMENTE en JSON: {{titulo, descripcion, categoria, duracion_estimada}}"""
        
        response = self.model.generate_content(prompt)
        # Limpieza simple de la respuesta JSON de Gemini
        data = json.loads(response.text.replace("```json", "").replace("```", ""))
        return ActividadSugerida(**data)