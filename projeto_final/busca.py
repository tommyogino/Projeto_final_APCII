"""
Módulo responsável pelos algoritmos de busca.
"""

def busca_linear_por_nome(alunos, nome):
    """
    Procura um aluno pelo nome percorrendo a lista do início ao fim
    (busca linear). Funciona em qualquer lista, ordenada ou não.

    Parâmetros:
        alunos (list[dict]): lista de alunos.
        nome (str): nome a procurar (sugestão: comparar ignorando
            maiúsculas/minúsculas).

    Retorno:
        dict | None: o aluno encontrado, ou None se não existir.

    """
    for i in range(len(alunos)):
        if alunos[i]["nome"].lower() == nome.lower():
            return alunos[i]

    return None

def busca_binaria_por_matricula(alunos_ordenados_por_matricula, matricula):
    """
    Procura um aluno pela matrícula usando busca binária.

    IMPORTANTE: a lista recebida PRECISA estar ordenada por matrícula antes
    de chamar esta função, senão o resultado pode ser incorreto. Ordene a
    lista (ex.: com sorted(alunos, key=lambda a: a["matricula"]) ou uma
    função própria) antes de chamar.

    Parâmetros:
        alunos_ordenados_por_matricula (list[dict]): lista de alunos já
            ordenada por matrícula, em ordem crescente.
        matricula (int): matrícula a procurar.

    Retorno:
        dict | None: o aluno encontrado, ou None se não existir.

    """
    inicio = 0
    fim = len(alunos_ordenados_por_matricula) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if alunos_ordenados_por_matricula[meio]["matricula"] == matricula:
            return alunos_ordenados_por_matricula[meio]
        
        elif alunos_ordenados_por_matricula[meio]["matricula"] < matricula:
            inicio = meio + 1
        
        else:
            fim = meio - 1

    return None