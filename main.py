from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Annotated
import uvicorn

app = FastAPI()


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


@app.post("/criar_plano_estudo", response_model=EstudoOutput)
def calcular_plano_de_estudo(dados: EstudoInput):
    total_horas = dados.horas_disponiveis
    total_minutos = total_horas * 60

    soma_pesos = 0
    pesos_por_materia = {}
    for nome, materia in dados.materias_estudo.items():
        score = materia.dificuldade * materia.peso * materia.numero_topicos
        pesos_por_materia[nome] = score
        soma_pesos += score

    if soma_pesos == 0:
        raise HTTPException(status_code=400, detail="A soma dos scores das matérias não pode ser zero.")

    plano_estudo = {}
    for nome, materia in dados.materias_estudo.items():
        recomendacao = int((pesos_por_materia[nome] / soma_pesos) * total_minutos)
        plano_estudo[nome] = MateriaOutput(
            dificuldade=materia.dificuldade,
            peso=materia.peso,
            numero_topicos=materia.numero_topicos,
            recomendacao_minutos_estudos=recomendacao
        )

    resposta = EstudoOutput(
        horas_disponiveis=total_horas,
        minutos_disponives=total_minutos,
        sugestao_de_plano_de_estudo=plano_estudo
    )
    return resposta


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
