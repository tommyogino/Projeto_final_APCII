"""
Módulo de utilidades: validação de dados e persistência em arquivo JSON.
"""

import os
import json

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Generated Python ANSI Art

ansi_art_lines = [
    "[38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m  [38;2;229;229;229m▀[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m█[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m [38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m      [38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m       [38;2;229;229;229m█[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m [38;2;229;229;229m▄[0m   [38;2;229;229;229m▀[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m ",
    " [38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m█[0m    [38;2;229;229;229m█[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m     [38;2;229;229;229m█[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m [38;2;229;229;229m█[0m       [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m      [38;2;229;229;229m█[0m   [38;2;229;229;229m█[0m",
    "[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m  [38;2;229;229;229m█[0m  [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m     [38;2;229;229;229m█[0m   [38;2;229;229;229m█[0m [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m",
]

def display_ansi_art():
    for line in ansi_art_lines:
        print(line)

def retornar():
    input("\nPressione ENTER para continuar...")

def validar_matricula(matricula):
    """
    Verifica se a matrícula é válida (ex.: número inteiro positivo).

    Parâmetros:
        matricula: valor a validar (pode vir como str do input()).

    Retorno:
        bool: True se válida, False caso contrário.

    """
    try:
        matricula = int(matricula)
        return matricula >= 0
       
    except (ValueError, TypeError):
        return False

def validar_nota(valor):
    """
    Verifica se a nota é válida (ex.: número entre 0 e 10).

    Parâmetros:
        valor: valor a validar (pode vir como str do input()).

    Retorno:
        bool: True se válida, False caso contrário.
    
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

    """
    dados = {
        "alunos": alunos,
        "notas": matriz_notas

    }
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


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
    if not os.path.exists(caminho):
        return [], []
    
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["alunos"], dados ["notas"]
