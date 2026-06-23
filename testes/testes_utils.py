import os
import json
import pytest
from utils import validar_matricula, validar_nota, salvar_dados, carregar_dados


# --- validar_matricula ---

def test_validar_matricula_inteiro_valido():
    assert validar_matricula(0) == True

def test_validar_matricula_string_numerica():
    assert validar_matricula("3") == True

def test_validar_matricula_negativa():
    assert validar_matricula(-1) == False

def test_validar_matricula_texto():
    assert validar_matricula("abc") == False

def test_validar_matricula_vazia():
    assert validar_matricula("") == False


# --- validar_nota ---

def test_validar_nota_valida():
    assert validar_nota(7.5) == True

def test_validar_nota_zero():
    assert validar_nota(0) == True

def test_validar_nota_dez():
    assert validar_nota(10) == True

def test_validar_nota_acima_de_dez():
    assert validar_nota(10.1) == False

def test_validar_nota_negativa():
    assert validar_nota(-1) == False


# --- salvar_dados e carregar_dados ---

@pytest.fixture
def arquivo_temp(tmp_path):
    """Retorna um caminho temporário para o arquivo JSON de teste."""
    return str(tmp_path / "dados_teste.json")


def test_salvar_e_carregar_dados(arquivo_temp):
    alunos = [{"matricula": 0, "nome": "Ana"}]
    notas = [[8.0, 7.0, 9.0, 6.0]]

    salvar_dados(arquivo_temp, alunos, notas)
    alunos_carregados, notas_carregadas = carregar_dados(arquivo_temp)

    assert alunos_carregados == alunos
    assert notas_carregadas == notas


def test_carregar_dados_arquivo_inexistente(arquivo_temp):
    alunos, notas = carregar_dados(arquivo_temp)
    assert alunos == []
    assert notas == []


def test_salvar_cria_arquivo(arquivo_temp):
    salvar_dados(arquivo_temp, [], [])
    assert os.path.exists(arquivo_temp)


def test_salvar_multiplos_alunos(arquivo_temp):
    alunos = [
        {"matricula": 0, "nome": "Ana"},
        {"matricula": 1, "nome": "Bruno"},
    ]
    notas = [
        [8.0, 7.0, 9.0, 6.0],
        [5.0, 6.0, 5.5, 7.0],
    ]
    salvar_dados(arquivo_temp, alunos, notas)
    alunos_carregados, notas_carregadas = carregar_dados(arquivo_temp)

    assert len(alunos_carregados) == 2
    assert alunos_carregados[1]["nome"] == "Bruno"
    assert notas_carregadas[1][0] == 5.0


def test_salvar_nome_com_acento(arquivo_temp):
    alunos = [{"matricula": 0, "nome": "João"}]
    salvar_dados(arquivo_temp, alunos, [[]])
    alunos_carregados, _ = carregar_dados(arquivo_temp)
    assert alunos_carregados[0]["nome"] == "João"
