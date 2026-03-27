from core.services.interface import IA_ServiceInterface
from feature.generateActivity.domain.entity.activity import GeneradorParametros

class GenerarActividadUseCase:
    def __init__(self, ia_service: IA_ServiceInterface):
        self.ia_service = ia_service

    async def execute(self, datos: GeneradorParametros):
        return await self.ia_service.generar_actividad_dopamina(datos)