from fastapi import APIRouter, HTTPException
from app.models.schemas import EstudoInput, EstudoOutput, MateriaOutput
from app.services.criar_plano_estudo import criar_plano_estudo

router = APIRouter()

@router.post("/criar_plano_estudo", response_model=EstudoOutput)
def criar_plano_estudo(dados: EstudoInput):
    return criar_plano_estudo(dados)
