from pydantic import BaseModel, Field
from typing import Dict, Annotated

class Materia(BaseModel):
    dificuldade: Annotated[int, Field(ge=1, le=3)]
    peso: Annotated[int, Field(ge=1, le=5)]
    numero_topicos: Annotated[int, Field(gt=0)]

class EstudoInput(BaseModel):
    horas_disponiveis: Annotated[int, Field(gt=0)]
    materias_estudo: Dict[str, Materia]

class MateriaOutput(Materia):
    recomendacao_minutos_estudos: int

class EstudoOutput(BaseModel):
    horas_disponiveis: int
    minutos_disponives: int  
    sugestao_de_plano_de_estudo: Dict[str, MateriaOutput]
