from fastapi import APIRouter, HTTPException
from app.models.schemas import EstudoInput, EstudoOutput, MateriaOutput
from app.services.calcular_divisao_tempo import calcular_divisao_tempo

router = APIRouter()

@router.post("/criar_plano_estudo", response_model=EstudoOutput)
def criar_plano_estudo(dados: EstudoInput):
    return calcular_divisao_tempo(dados)
