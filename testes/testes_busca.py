from busca import busca_linear_por_nome, busca_binaria_por_matricula

ALUNOS = [
    {"matricula": 0, "nome": "Ana Silva"},
    {"matricula": 1, "nome": "Bruno Costa"},
    {"matricula": 2, "nome": "Carlos Lima"},
]


# --- busca_linear_por_nome ---

def test_busca_linear_encontra_aluno():
    resultado = busca_linear_por_nome(ALUNOS, "Bruno Costa")
    assert resultado == {"matricula": 1, "nome": "Bruno Costa"}


def test_busca_linear_case_insensitive():
    resultado = busca_linear_por_nome(ALUNOS, "ana silva")
    assert resultado == {"matricula": 0, "nome": "Ana Silva"}


def test_busca_linear_nao_encontrado():
    resultado = busca_linear_por_nome(ALUNOS, "Zé Ninguém")
    assert resultado is None


def test_busca_linear_lista_vazia():
    resultado = busca_linear_por_nome([], "Ana")
    assert resultado is None


def test_busca_linear_primeiro_elemento():
    resultado = busca_linear_por_nome(ALUNOS, "Ana Silva")
    assert resultado["matricula"] == 0


def test_busca_linear_ultimo_elemento():
    resultado = busca_linear_por_nome(ALUNOS, "Carlos Lima")
    assert resultado["matricula"] == 2


# --- busca_binaria_por_matricula ---

def test_busca_binaria_encontra_aluno():
    resultado = busca_binaria_por_matricula(ALUNOS, 1)
    assert resultado == {"matricula": 1, "nome": "Bruno Costa"}


def test_busca_binaria_primeiro_elemento():
    resultado = busca_binaria_por_matricula(ALUNOS, 0)
    assert resultado["nome"] == "Ana Silva"


def test_busca_binaria_ultimo_elemento():
    resultado = busca_binaria_por_matricula(ALUNOS, 2)
    assert resultado["nome"] == "Carlos Lima"


def test_busca_binaria_nao_encontrado():
    resultado = busca_binaria_por_matricula(ALUNOS, 99)
    assert resultado is None


def test_busca_binaria_lista_vazia():
    resultado = busca_binaria_por_matricula([], 0)
    assert resultado is None
