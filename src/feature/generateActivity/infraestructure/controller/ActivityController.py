import os
from fastapi import APIRouter, Depends
from src.feature.generateActivity.domain.entity.Activity import GeneradorParametros
from src.feature.generateActivity.application.usecases.GenerarActividadUseCase import GenerarActividadUseCase
from src.feature.generateActivity.application.dto.DatosGeneradorDTO import DatosGeneradorDTO
from src.core.services.serviceimpl.GeminiServiceImpl import GeminiServiceImpl

router = APIRouter(prefix="/activity", tags=["Activities"])

def get_activity_use_case():
    service = GeminiServiceImpl(api_key=os.getenv("GOOGLE_API_KEY"))
    return GenerarActividadUseCase(service)

@router.post("/generate")
async def generar(datos: DatosGeneradorDTO, use_case: GenerarActividadUseCase = Depends(get_activity_use_case)):
    # Mapeo manual del DTO a la entidad de parámetros de dominio
    params = GeneradorParametros(
        user_name=datos.name,
        user_interests=datos.interests,
        user_topic=datos.topic,
        user_description=datos.description,
        user_leisure_type=datos.leisureType,
        template_activity=datos.activity_template,
        template_type=datos.type_template,
        template_participants=datos.participants_template,
        template_duration=datos.duration_template,
        template_kid_friendly=datos.kidFriendly_template
    )
    
    actividad = await use_case.execute(params)
    return actividad 