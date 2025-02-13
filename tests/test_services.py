import pytest
from app.models.schemas import EstudoInput, Materia
from app.services.calcular_divisao_tempo import calcular_divisao_tempo
from fastapi.exceptions import HTTPException

def test_calcular_plano_estudo():
    dados = EstudoInput(
        horas_disponiveis=4,
        materias_estudo={
            "Matemática": Materia(dificuldade=3, peso=5, numero_topicos=10),
            "História": Materia(dificuldade=2, peso=3, numero_topicos=5),
        }
    )

    resultado = calcular_divisao_tempo(dados)
    
    assert resultado.horas_disponiveis == 4
    assert resultado.minutos_disponives == 240
    assert "Matemática" in resultado.sugestao_de_plano_de_estudo
    assert "História" in resultado.sugestao_de_plano_de_estudo
    assert resultado.sugestao_de_plano_de_estudo["Matemática"].recomendacao_minutos_estudos > 0
    assert resultado.sugestao_de_plano_de_estudo["História"].recomendacao_minutos_estudos > 0

def test_calcular_plano_estudo_sem_materias():
    dados = EstudoInput(horas_disponiveis=4, materias_estudo={})

    with pytest.raises(HTTPException) as exc:
        calcular_divisao_tempo(dados)
    
    assert exc.value.status_code == 400
    assert exc.value.detail == "A soma dos scores das matérias não pode ser zero."
