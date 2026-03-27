import json
import google.generativeai as genai
from src.core.services.interface.IA_ServiceInterface import IA_ServiceInterface
from src.feature.chat.domain.entity.Message import UsuarioContexto
from src.feature.generateActivity.domain.entity.Activity import ActividadSugerida, GeneradorParametros

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
        prompt = f"""
            Actúa como experto en neurociencia.
            Datos: {params.estado_animo}, intereses: {params.intereses}, tiempo: {params.tiempo_disponible}.
            Responde ÚNICAMENTE en JSON: {{"titulo": "...", "descripcion": "...", "categoria": "...", "duracion_estimada": "..."}}
        """
        
        response = self.model.generate_content(prompt)
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_json)
        return ActividadSugerida(**data)