from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_plano_estudo():
    payload = {
        "horas_disponiveis": 4,
        "materias_estudo": {
            "Matemática": {"dificuldade": 3, "peso": 5, "numero_topicos": 10},
            "História": {"dificuldade": 2, "peso": 3, "numero_topicos": 5},
        }
    }

    response = client.post("/criar_plano_estudo", json=payload)
    assert response.status_code == 200
    data = response.json()
    
    assert data["horas_disponiveis"] == 4
    assert data["minutos_disponives"] == 240
    assert "Matemática" in data["sugestao_de_plano_de_estudo"]
    assert "História" in data["sugestao_de_plano_de_estudo"]
    assert data["sugestao_de_plano_de_estudo"]["Matemática"]["recomendacao_minutos_estudos"] > 0
    assert data["sugestao_de_plano_de_estudo"]["História"]["recomendacao_minutos_estudos"] > 0

def test_criar_plano_estudo_sem_materias():
    payload = {
        "horas_disponiveis": 4,
        "materias_estudo": {}
    }

    response = client.post("/criar_plano_estudo", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "A soma dos scores das matérias não pode ser zero."
