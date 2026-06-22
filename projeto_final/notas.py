"""
Módulo responsável pela matriz de notas.

A matriz de notas é uma lista de listas (matriz_notas), onde:
- a linha i corresponde ao aluno lista_alunos[i]
- a coluna j corresponde à disciplina DISCIPLINAS[j]

Exemplo de matriz com 2 alunos e 4 disciplinas:
    matriz_notas = [
        [7.5, 8.0, 6.0, 9.0],   # notas do aluno 0
        [5.0, 6.5, 7.0, 8.0],   # notas do aluno 1
    ]
"""
import utils

DISCIPLINAS = ["Matemática", "Português", "Ciências", "História"]


def criar_matriz_notas(qtd_alunos, qtd_disciplinas=len(DISCIPLINAS)):
    """
    Cria uma matriz de notas com todas as posições inicializadas em 0.0.

    Parâmetros:
        qtd_alunos (int): número de linhas da matriz.
        qtd_disciplinas (int): número de colunas da matriz.

    Retorno:
        list[list[float]]: matriz qtd_alunos x qtd_disciplinas preenchida com 0.0.
    """
    notas = []

    for i in range(qtd_alunos):
        linha = []
        for j in range(qtd_disciplinas):
            linha.append(0.0)
        notas.append(linha)
    
    return notas


def cadastrar_nota(matriz, indice_aluno, indice_disciplina, valor):
    """
    Atualiza o valor de uma nota na matriz.

    Parâmetros:
        matriz (list[list[float]]): matriz de notas.
        indice_aluno (int): linha (índice do aluno em lista_alunos).
        indice_disciplina (int): coluna (índice em DISCIPLINAS).
        valor (float): nova nota.

    TODO: implementar (lembrar de validar a nota antes — ver utils.validar_nota).
    """
    if utils.validar_nota(valor) == True:
        matriz[indice_aluno][indice_disciplina] = valor
        return True
    
    else:
        return False

    


def calcular_media(matriz, indice_aluno):
    """
    Calcula a média das notas de um aluno (uma linha da matriz).

    Parâmetros:
        matriz (list[list[float]]): matriz de notas.
        indice_aluno (int): linha do aluno.

    Retorno:
        float: média das notas do aluno.

    """
    linha = matriz[indice_aluno]
    soma = 0
    for nota in linha:
        soma += nota
    
    return soma / len(linha)


def calcular_media_geral(matriz):
    """
    Calcula a média geral da turma (média de todas as notas da matriz).
    Útil para o relatório geral.

    Parâmetros:
        matriz (list[list[float]]): matriz de notas.

    Retorno:
        float: média geral de todas as notas.

    """
    soma = 0
    for i in range(len(matriz)):
        soma += calcular_media(matriz, i)
    
    return soma / len(matriz)