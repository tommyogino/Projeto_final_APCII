from ordenacao import ordenar_por_nome, ordenar_por_media

ALUNOS = [
    {"matricula": 0, "nome": "Carlos Lima"},
    {"matricula": 1, "nome": "Ana Silva"},
    {"matricula": 2, "nome": "Bruno Costa"},
]


# --- ordenar_por_nome ---

def test_ordenar_por_nome_ordem_alfabetica():
    resultado = ordenar_por_nome(ALUNOS)
    nomes = [a["nome"] for a in resultado]
    assert nomes == ["Ana Silva", "Bruno Costa", "Carlos Lima"]


def test_ordenar_por_nome_nao_modifica_original():
    copia = ALUNOS.copy()
    ordenar_por_nome(ALUNOS)
    assert ALUNOS == copia


def test_ordenar_por_nome_lista_vazia():
    assert ordenar_por_nome([]) == []


def test_ordenar_por_nome_um_elemento():
    alunos = [{"matricula": 0, "nome": "Ana"}]
    assert ordenar_por_nome(alunos) == alunos


def test_ordenar_por_nome_ja_ordenada():
    alunos = [
        {"matricula": 0, "nome": "Ana"},
        {"matricula": 1, "nome": "Bruno"},
    ]
    resultado = ordenar_por_nome(alunos)
    assert resultado[0]["nome"] == "Ana"
    assert resultado[1]["nome"] == "Bruno"


# --- ordenar_por_media ---

def test_ordenar_por_media_decrescente():
    alunos = [
        {"matricula": 0, "nome": "Ana"},
        {"matricula": 1, "nome": "Bruno"},
        {"matricula": 2, "nome": "Carlos"},
    ]
    matriz = [
        [5.0, 5.0, 5.0, 5.0],   # Ana: média 5
        [9.0, 9.0, 9.0, 9.0],   # Bruno: média 9
        [7.0, 7.0, 7.0, 7.0],   # Carlos: média 7
    ]
    resultado = ordenar_por_media(alunos, matriz)
    medias = [par[1] for par in resultado]
    assert medias == sorted(medias, reverse=True)


def test_ordenar_por_media_primeiro_e_maior():
    alunos = [
        {"matricula": 0, "nome": "Ana"},
        {"matricula": 1, "nome": "Bruno"},
    ]
    matriz = [
        [4.0, 4.0, 4.0, 4.0],
        [8.0, 8.0, 8.0, 8.0],
    ]
    resultado = ordenar_por_media(alunos, matriz)
    assert resultado[0][0] == "Bruno"
    assert resultado[0][1] == 8.0


def test_ordenar_por_media_retorna_tuplas():
    alunos = [{"matricula": 0, "nome": "Ana"}]
    matriz = [[6.0, 6.0, 6.0, 6.0]]
    resultado = ordenar_por_media(alunos, matriz)
    assert isinstance(resultado[0], tuple)
    assert resultado[0][0] == "Ana"
    assert resultado[0][1] == 6.0
