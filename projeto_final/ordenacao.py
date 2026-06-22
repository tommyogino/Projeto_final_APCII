"""
Módulo responsável pelos algoritmos de ordenação.

Importante: o objetivo da disciplina é implementar o algoritmo de ordenação
manualmente (ex.: bubble sort, insertion sort ou selection sort) em vez de
usar sorted()/list.sort() prontos do Python.
"""


def ordenar_por_nome(alunos):
    """
    Retorna uma nova lista de alunos ordenada por nome (ordem alfabética
    crescente).

    Parâmetros:
        alunos (list[dict]): lista de alunos.

    Retorno:
        list[dict]: nova lista ordenada por nome. Não deve modificar a
        lista original (faça uma cópia, ex.: alunos.copy(), antes de ordenar).

    """
    alunos_copia = alunos.copy()
    n = len(alunos_copia)

    for i in range(n):
        trocou = False

        for j in range(0, n - i - 1):
            if alunos_copia[j]["nome"] > alunos_copia[j + 1]["nome"]:
                alunos_copia[j], alunos_copia[j + 1] = alunos_copia[j + 1], alunos_copia[j]
                trocou = True

        if not trocou:
            break
        
    return alunos_copia



def ordenar_por_media(alunos, matriz_notas):
    """
    Retorna uma nova lista de alunos ordenada pela média de notas, da maior
    para a menor.

    Atenção: como a matriz de notas usa o índice do aluno na lista original
    como linha (matriz_notas[i] pertence a alunos[i]), ao reordenar é preciso
    manter essa associação aluno <-> notas (sugestão: ordenar uma lista de
    pares (aluno, média) em vez de só os alunos).

    Parâmetros:
        alunos (list[dict]): lista de alunos.
        matriz_notas (list[list[float]]): matriz de notas correspondente.

    Retorno:
        list[dict]: nova lista de alunos ordenada por média decrescente.

    """
    from notas import calcular_media

    pares = []
    for i in range(len(alunos)):
        nome = alunos[i]["nome"]
        media = calcular_media(matriz_notas, i)
        pares.append((nome, media))
    
    n = len(pares)

    for i in range(n):
        trocou = False
        
        for j in range(0, n - i - 1):
            if pares[j][1] < pares[j + 1][1]:
                pares[j], pares[j + 1] =  pares[j + 1], pares[j]
                trocou = True

        if not trocou:
            break

    return pares 

