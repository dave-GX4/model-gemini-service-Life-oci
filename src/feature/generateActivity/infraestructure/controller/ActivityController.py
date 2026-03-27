from fastapi import APIRouter, Depends
from src.feature.generateActivity.application.usecases.GenerarActividadUseCase import GenerarActividadUseCase
from src.feature.generateActivity.application.dto.DatosGeneradorDto import DatosGeneradorDto
from src.core.services.serviceimpl.GeminiServiceImpl import GeminiServiceImpl
import os

router = APIRouter(prefix="/activity", tags=["Activities"])

def get_activity_use_case():
    service = GeminiServiceImpl(api_key=os.getenv("GOOGLE_API_KEY"))
    return GenerarActividadUseCase(service)

@router.post("/generate")
async def generar(datos: DatosGeneradorDto, use_case: GenerarActividadUseCase = Depends(get_activity_use_case)):
    actividad = await use_case.execute(datos)
    return {"actividad_sugerida": actividad}