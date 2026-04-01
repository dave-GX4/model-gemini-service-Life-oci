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
        userName=datos.name,
        userInterests=datos.interests,
        userTopics=datos.topics,
        userDescription=datos.description,
        userLeisureType=datos.leisureType,
        templateActivity=datos.activityTemplate,
        templateType=datos.typeTemplate,
        templateParticipants=datos.participantsTemplate,
        templateDuration=datos.durationTemplate,
        templateKidFriendly=datos.kidFriendlyTemplate
    )
    
    actividad = await use_case.execute(params)
    return actividad 