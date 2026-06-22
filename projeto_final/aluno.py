"""
Módulo responsável pela entidade Aluno.

Representação escolhida: cada aluno é um dict no formato
    {"matricula": int, "nome": str}

A lista de todos os alunos cadastrados vive em main.py (lista_alunos = []).
O índice de um aluno nessa lista corresponde à linha dele na matriz de notas
(ver notas.py) — ou seja, lista_alunos[i] e matriz_notas[i] são do mesmo aluno.
"""


def criar_aluno(matricula, nome):
    """
    Cria e retorna um novo aluno no formato dict.

    Parâmetros:
        matricula (int): matrícula única do aluno.
        nome (str): nome completo do aluno.

    Retorno:
        dict: {"matricula": matricula, "nome": nome}
    """
    aluno_criado = {"matricula": matricula, "nome": nome}

    return aluno_criado

def listar_alunos(alunos):
    """
    Imprime na tela os dados de todos os alunos da lista.

    Parâmetros:
        alunos (list[dict]): lista de alunos.

    Retorno:
        None
    
    """

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print(f"\n{'ALUNOS':^35}")
    print("=" * 35)
    for i in alunos:
        print(f"  {i['matricula']}. {i['nome']}")
        
    print("=" * 35)

