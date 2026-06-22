"""
Módulo de utilidades: validação de dados e persistência em arquivo JSON.
"""

import os
import json

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def retornar():
    input("\nPressione ENTER para continuar...")

def validar_matricula(matricula):
    """
    Verifica se a matrícula é válida (ex.: número inteiro positivo).

    Parâmetros:
        matricula: valor a validar (pode vir como str do input()).

    Retorno:
        bool: True se válida, False caso contrário.

    TODO: implementar.
    """
    pass


def validar_nota(valor):
    """
    Verifica se a nota é válida (ex.: número entre 0 e 10).

    Parâmetros:
        valor: valor a validar (pode vir como str do input()).

    Retorno:
        bool: True se válida, False caso contrário.

    TODO: implementar.
    """
    if valor >= 0 and valor <= 10:
        return True
    else:
        return False


def salvar_dados(caminho, alunos, matriz_notas):
    """
    Salva alunos e matriz de notas em um arquivo JSON.

    Parâmetros:
        caminho (str): caminho do arquivo (ex.: "dados.json").
        alunos (list[dict]): lista de alunos.
        matriz_notas (list[list[float]]): matriz de notas.

    Retorno:
        None

    TODO: implementar. Sugestão de formato do JSON:
        {"alunos": alunos, "notas": matriz_notas}
    Use json.dump(dados, arquivo) com o arquivo aberto em modo "w".
    """
    pass


def carregar_dados(caminho):
    """
    Carrega alunos e matriz de notas a partir de um arquivo JSON.
    Se o arquivo não existir, deve retornar listas vazias (sistema começa
    "do zero") em vez de lançar erro.

    Parâmetros:
        caminho (str): caminho do arquivo (ex.: "dados.json").

    Retorno:
        tuple[list[dict], list[list[float]]]: (alunos, matriz_notas)

    TODO: implementar. Lembrar de tratar o caso de arquivo inexistente
    (ex.: with try/except FileNotFoundError ou verificando com os.path.exists).
    """
    pass
