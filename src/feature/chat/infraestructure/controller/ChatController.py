from fastapi import APIRouter, Depends
from src.feature.chat.application.usecases.ChatUseCase import ChatUseCase
from src.feature.chat.application.dto.SolicitudUsuarioDto import SolicitudUsuarioDto
from src.core.services.serviceimpl.GeminiServiceImpl import GeminiServiceImpl
import os

router = APIRouter(prefix="/chat", tags=["Chat"])

# Inyección manual (puedes usar librerías de DI si el proyecto crece)
def get_chat_use_case():
    service = GeminiServiceImpl(api_key=os.getenv("GOOGLE_API_KEY"))
    return ChatUseCase(service)

@router.post("/")
async def conversar(datos: SolicitudUsuarioDto, use_case: ChatUseCase = Depends(get_chat_use_case)):
    respuesta = await use_case.execute(datos.mensaje, datos.contexto_extra)
    return {"respuesta_ia": respuesta}