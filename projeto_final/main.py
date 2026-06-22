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
    utils.display_ansi_art()
    print("\n============//============\n")

    #Imprime as opções do menu principal.
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno")
    print("4. Ordenar alunos")
    print("5. Cadastrar notas")
    print("6. Calcular média de um aluno")
    print("7. Relatório geral")
    print("0. Salvar e sair")


def main():
    #Loop principal do programa.
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
            utils.retornar()


        elif opcao == "2":
            aluno.listar_alunos(lista_alunos)
            utils.retornar()

        elif opcao == "3":
            # TODO: perguntar se busca por nome ou matrícula e chamar
            # busca.busca_linear_por_nome ou busca.busca_binaria_por_matricula
            # (lembrar de ordenar por matrícula antes da busca binária).
            pass

        elif opcao == "4":

            metodo = input("Deseja ordenar por ordem alfabetica ou por media do aluno?\n1. Ordem alfabetica\n2. Media do aluno\n")
            if metodo == "1":
                aluno.listar_alunos(ordenacao.ordenar_por_nome(lista_alunos))
            
            elif metodo == "2":
                print(f"\n{'ALUNOS':^35}")
                print("=" * 35)
                for i in ordenacao.ordenar_por_media(lista_alunos,matriz_notas):
                    print(f"{i[0]} | {i[1]:.2f}")
                    
                print("=" * 35)
            
            else:
                print("Opcao invalida!")

            utils.retornar()
            # TODO: perguntar critério (nome ou média) e chamar
            # ordenacao.ordenar_por_nome ou ordenacao.ordenar_por_media,
            # depois exibir o resultado.
            pass

        elif opcao == "5":
            matricula = input("\nMatricula do aluno: ")
            utils.validar_matricula(matricula)
            print("\nDisciplinas:")
            for i, disciplina in enumerate(notas.DISCIPLINAS):
                print(f"{i}. {disciplina}")

            indice_disciplina = int(input("Escolha a disciplina: "))
            nota = float(input("Nota: "))

            sucesso = notas.cadastrar_nota(matriz_notas, matricula, indice_disciplina, nota)
            if sucesso:
                print("\nNota cadastrada com sucesso!")

            else:
                print("\nNota invalida! Digite um valor entre 0 e 10. ")

            utils.retornar()
            
        elif opcao == "6":
            indice = int(input("Digite a matricula do aluno: "))
            print(f"Media das notas do aluno: {notas.calcular_media(matriz_notas,indice)}")
            utils.retornar()

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

if __name__ == "__main__":
    main()