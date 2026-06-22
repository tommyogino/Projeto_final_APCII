from aluno import criar_aluno, listar_alunos


def test_criar_aluno_retorna_dict_correto():
    resultado = criar_aluno(0, "Maria")
    assert resultado == {"matricula": 0, "nome": "Maria"}


def test_criar_aluno_matricula_zero():
    resultado = criar_aluno(0, "Primeiro Aluno")
    assert resultado["matricula"] == 0


def test_criar_aluno_nomes_diferentes_geram_dicts_diferentes():
    aluno1 = criar_aluno(0, "Ana")
    aluno2 = criar_aluno(1, "Bruno")
    assert aluno1 != aluno2
    assert aluno1["matricula"] != aluno2["matricula"]


def test_listar_alunos_nao_lanca_erro_com_lista_vazia():
    listar_alunos([])


def test_listar_alunos_imprime_matricula_e_nome(capsys):
    alunos = [
        {"matricula": 0, "nome": "Ana"},
        {"matricula": 1, "nome": "Bruno"},
    ]
    listar_alunos(alunos)

    saida = capsys.readouterr().out
    assert "Ana" in saida
    assert "Bruno" in saida
    assert "0" in saida
    assert "1" in saida
