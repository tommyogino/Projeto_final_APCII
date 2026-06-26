from unittest.mock import patch, call
import main


def rodar_menu(inputs):
    """
    Roda main() com uma sequência de inputs simulados.
    Suprime limpeza de tela e logo ANSI para não poluir o teste.
    """
    with patch("builtins.input", side_effect=inputs), \
         patch("utils.limpar_tela"), \
         patch("utils.display_ansi_art"), \
         patch("utils.carregar_dados", return_value=([], [])), \
         patch("utils.salvar_dados"):
        main.main()


# --- opção 0: sair ---

def test_sair_encerra_programa():
    rodar_menu(["0"])


# --- opção 1: cadastrar aluno ---

def test_cadastrar_aluno_valido(capsys):
    rodar_menu(["1", "Ana Silva", "", "0"])
    saida = capsys.readouterr().out
    assert "cadastrado com sucesso" in saida.lower()


def test_cadastrar_aluno_nome_vazio(capsys):
    rodar_menu(["1", "", "", "0"])
    saida = capsys.readouterr().out
    assert "inválido" in saida.lower()


def test_cadastrar_aluno_nome_com_numero(capsys):
    rodar_menu(["1", "Ana123", "", "0"])
    saida = capsys.readouterr().out
    assert "inválido" in saida.lower()


# --- opção 2: listar alunos ---

def test_listar_alunos_vazia(capsys):
    rodar_menu(["2", "", "0"])
    saida = capsys.readouterr().out
    assert "nenhum" in saida.lower()


def test_listar_alunos_com_aluno(capsys):
    with patch("builtins.input", side_effect=["1", "Bruno", "", "2", "", "0"]), \
         patch("utils.limpar_tela"), \
         patch("utils.display_ansi_art"), \
         patch("utils.carregar_dados", return_value=([], [])), \
         patch("utils.salvar_dados"):
        main.main()
    saida = capsys.readouterr().out
    assert "Bruno" in saida


# --- opção 3: buscar aluno ---

def test_buscar_por_nome_encontrado(capsys):
    with patch("builtins.input", side_effect=["1", "Ana Silva", "", "3", "1", "Ana Silva", "", "0"]), \
         patch("utils.limpar_tela"), \
         patch("utils.display_ansi_art"), \
         patch("utils.carregar_dados", return_value=([], [])), \
         patch("utils.salvar_dados"):
        main.main()
    saida = capsys.readouterr().out
    assert "Ana Silva" in saida


def test_buscar_por_nome_nao_encontrado(capsys):
    rodar_menu(["3", "1", "Zé Ninguém", "", "0"])
    saida = capsys.readouterr().out
    assert "não encontrado" in saida.lower()


def test_buscar_por_matricula_nao_encontrada(capsys):
    rodar_menu(["3", "2", "99", "", "0"])
    saida = capsys.readouterr().out
    assert "não encontrado" in saida.lower()


# --- opção 5: matrícula inválida ---

def test_cadastrar_nota_matricula_invalida(capsys):
    rodar_menu(["5", "99", "", "0"])
    saida = capsys.readouterr().out
    assert "inválid" in saida.lower()


# --- opção inválida ---

def test_opcao_invalida(capsys):
    rodar_menu(["9", "", "0"])
    saida = capsys.readouterr().out
    assert "inválid" in saida.lower()
