"""
Ponto de entrada do Sistema Acadêmico.

Mantém o estado em memória (lista_alunos e matriz_notas) e oferece um menu
em texto para o usuário interagir com as funcionalidades dos outros módulos.
"""

import aluno
import notas
import busca
import ordenacao
import utils

ARQUIVO_DADOS = "dados.json"

def exibir_menu():
    display_ansi_art()
    print("\n============//============\n")
    """Imprime as opções do menu principal."""
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno")
    print("4. Ordenar alunos")
    print("5. Cadastrar notas")
    print("6. Calcular média de um aluno")
    print("7. Relatório geral")
    print("0. Salvar e sair")


def main():
    """Loop principal do programa."""
    # TODO: carregar dados existentes com utils.carregar_dados(ARQUIVO_DADOS)
    lista_alunos = []
    matriz_notas = []

    while True:
        utils.limpar_tela()
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("\nNome do aluno: ").strip().title()
            matricula = len(lista_alunos)
            novo_aluno = aluno.criar_aluno(matricula, nome)
            lista_alunos.append(novo_aluno)
            matriz_notas.append(notas.criar_matriz_notas(1)[0])
            print("\nAluno cadastrado com sucesso!")
            input("\nPressione ENTER para continuar...")

            # TODO: validar com utils.validar_matricula, adicionar uma nova linha em matriz_notas com notas.criar_matriz_notas(1) ou similar.

        elif opcao == "2":
            #chamar aluno.listar_alunos(lista_alunos)
            aluno.listar_alunos(lista_alunos)
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            # TODO: perguntar se busca por nome ou matrícula e chamar
            # busca.busca_linear_por_nome ou busca.busca_binaria_por_matricula
            # (lembrar de ordenar por matrícula antes da busca binária).
            pass

        elif opcao == "4":
            # TODO: perguntar critério (nome ou média) e chamar
            # ordenacao.ordenar_por_nome ou ordenacao.ordenar_por_media,
            # depois exibir o resultado.
            pass

        elif opcao == "5":
            matricula = int(input("\nMatricula do aluno: "))

            print("\nDisciplinas:")
            for i, disciplina in enumerate(notas.DISCIPLINAS):
                print(f"{i}. {disciplina}")

            indice_disciplina = int(input("Escolha a disciplina: "))
            nota = float(input("Nota: "))

            notas.cadastrar_nota(matriz_notas, matricula, indice_disciplina, nota)
            # TODO: pedir índice/matrícula do aluno, disciplina e nota,
            # validar com utils.validar_nota e chamar notas.cadastrar_nota.
            pass

        elif opcao == "6":
            # TODO: pedir o aluno e chamar notas.calcular_media.
            pass

        elif opcao == "7":
            # TODO: montar um relatório combinando listagem de alunos,
            # médias individuais (notas.calcular_media) e média geral
            # (notas.calcular_media_geral).
            pass

        elif opcao == "0":
            # TODO: chamar utils.salvar_dados(ARQUIVO_DADOS, lista_alunos, matriz_notas)
            print("Dados salvos. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar...")

# Generated Python ANSI Art

ansi_art_lines = [
    "[38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m  [38;2;229;229;229m▀[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m█[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m [38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m      [38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m       [38;2;229;229;229m█[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m [38;2;229;229;229m▄[0m   [38;2;229;229;229m▀[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m ",
    " [38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m█[0m    [38;2;229;229;229m█[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m   [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m     [38;2;229;229;229m█[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m [38;2;229;229;229m█[0m       [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m▀[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m      [38;2;229;229;229m█[0m   [38;2;229;229;229m█[0m",
    "[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m  [38;2;229;229;229m█[0m  [38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m     [38;2;229;229;229m█[0m   [38;2;229;229;229m█[0m [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m   [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m [38;2;229;229;229m█[0m  [38;2;229;229;229m█[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m  [38;2;229;229;229m▀[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▄[0m[38;2;229;229;229m▀[0m",
]

def display_ansi_art():
    for line in ansi_art_lines:
        print(line)

if __name__ == "__main__":
    main()
