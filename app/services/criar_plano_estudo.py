from fastapi import HTTPException
from app.models.schemas import EstudoInput, EstudoOutput, MateriaOutput

def criar_plano_estudo(dados: EstudoInput) -> EstudoOutput:
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

    return EstudoOutput(
        horas_disponiveis=total_horas,
        minutos_disponives=total_minutos,
        sugestao_de_plano_de_estudo=plano_estudo
    )
