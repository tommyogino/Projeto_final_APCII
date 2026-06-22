from notas import (
    criar_matriz_notas,
    cadastrar_nota,
    calcular_media,
    calcular_media_geral,
    DISCIPLINAS,
)


# --- criar_matriz_notas ---

def test_criar_matriz_notas_dimensoes_corretas():
    matriz = criar_matriz_notas(3)
    assert len(matriz) == 3
    assert len(matriz[0]) == len(DISCIPLINAS)


def test_criar_matriz_notas_inicializada_com_zero():
    matriz = criar_matriz_notas(2)
    for linha in matriz:
        for nota in linha:
            assert nota == 0.0


def test_criar_matriz_notas_uma_linha():
    matriz = criar_matriz_notas(1)
    assert len(matriz) == 1
    assert len(matriz[0]) == len(DISCIPLINAS)


# --- cadastrar_nota ---

def test_cadastrar_nota_atualiza_valor(capsys):
    matriz = criar_matriz_notas(1)
    cadastrar_nota(matriz, 0, 0, 8.5)
    assert matriz[0][0] == 8.5


def test_cadastrar_nota_invalida_nao_altera(capsys):
    matriz = criar_matriz_notas(1)
    cadastrar_nota(matriz, 0, 0, 11.0)
    assert matriz[0][0] == 0.0


def test_cadastrar_nota_zero_e_valida(capsys):
    matriz = criar_matriz_notas(1)
    cadastrar_nota(matriz, 0, 1, 0.0)
    assert matriz[0][1] == 0.0


def test_cadastrar_nota_dez_e_valida(capsys):
    matriz = criar_matriz_notas(1)
    cadastrar_nota(matriz, 0, 2, 10.0)
    assert matriz[0][2] == 10.0


# --- calcular_media ---

def test_calcular_media_notas_iguais():
    matriz = criar_matriz_notas(1)
    for j in range(len(DISCIPLINAS)):
        matriz[0][j] = 8.0
    assert calcular_media(matriz, 0) == 8.0


def test_calcular_media_notas_diferentes():
    matriz = [[5.0, 7.0, 9.0, 3.0]]
    media = calcular_media(matriz, 0)
    assert media == 6.0


def test_calcular_media_notas_zeradas():
    matriz = criar_matriz_notas(1)
    assert calcular_media(matriz, 0) == 0.0


# --- calcular_media_geral ---

def test_calcular_media_geral_dois_alunos():
    matriz = [
        [8.0, 8.0, 8.0, 8.0],
        [6.0, 6.0, 6.0, 6.0],
    ]
    assert calcular_media_geral(matriz) == 7.0


def test_calcular_media_geral_um_aluno():
    matriz = [[10.0, 10.0, 10.0, 10.0]]
    assert calcular_media_geral(matriz) == 10.0
