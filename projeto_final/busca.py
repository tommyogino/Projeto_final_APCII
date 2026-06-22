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

    TODO: implementar.
    """
    pass


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

    TODO: implementar (lembrar de manter os índices início/fim e calcular o
    meio a cada iteração, comparando matricula do meio com o valor buscado).
    """
    pass
