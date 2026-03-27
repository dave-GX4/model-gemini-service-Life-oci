from dataclasses import dataclass

@dataclass
class ActividadSugerida:
    titulo: str
    descripcion: str
    categoria: str
    duracion_estimada: str

@dataclass
class GeneradorParametros:
    hora_actual: str
    estado_animo: str
    intereses: str
    tiempo_disponible: str