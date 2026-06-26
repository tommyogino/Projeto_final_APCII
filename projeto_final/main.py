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
    lista_alunos, matriz_notas = utils.carregar_dados(ARQUIVO_DADOS)

    while True:
        utils.limpar_tela()
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("\nNome do aluno: ").strip().title()

            if not nome or not all(c.isalpha() or c.isspace() for c in nome):
                print("\nNome inválido! Use apenas letras e espaços.")
                utils.retornar()
                continue

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
            metodo = input("Deseja buscar o nome ou a matricula do aluno?\n1. Nome\n2. Matricula\n\n")
            
            if metodo == "1":
                nome = input("\nDigite o nome: ")
                resultado = busca.busca_linear_por_nome(lista_alunos, nome)

                if resultado:
                    print(f"\nAluno encontrado! \nNome: {resultado['nome']} | Matrícula: {resultado['matricula']}")

                else:
                    print("\nAluno não encontrado.")

            elif metodo == "2":
                matricula = int(input("\nDigite a matrícula: "))
                resultado = busca.busca_binaria_por_matricula(lista_alunos, matricula)

                if resultado:
                    print(f"\nAluno encontrado! \nNome: {resultado['nome']} | Matrícula: {resultado['matricula']}")

                else:
                    print("\nAluno não encontrado.")

            utils.retornar()

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

        elif opcao == "5":
            matricula = int(input("\nMatricula do aluno: "))

            if utils.validar_matricula(matricula, lista_alunos) == False:
                print("\nMatrícula inválida!")
                utils.retornar()
                continue

            nome_aluno = lista_alunos[matricula]["nome"]
            confirmacao = input(f"\nAluno selecionado: {nome_aluno}\nConfirmar? (s/n): ").strip().lower()

            if confirmacao != "s":
                print("\nOperação cancelada.")
                utils.retornar()
                continue

            for j, disciplina in enumerate(notas.DISCIPLINAS):
                while True:
                    nota = float(input(f"Nota de {disciplina}: "))
                    sucesso = notas.cadastrar_nota(matriz_notas, matricula, j, nota)
                    
                    if sucesso:
                        break
                    
                    print("Nota inválida! Digite um valor entre 0 e 10.")

            print("\nNotas cadastradas com sucesso!")
            utils.retornar()
            
        elif opcao == "6":
            indice = int(input("Digite a matricula do aluno: "))

            if utils.validar_matricula(indice, lista_alunos) == False:
                print("Matricula nao encontrada!")

            else:
                print(f"Media das notas do aluno {lista_alunos[indice]["nome"]}: {notas.calcular_media(matriz_notas,indice)}")

            utils.retornar()

        elif opcao == "7":
            print('\nRelatorio Geral\n')
            print("=" * 35)

            for i in range(len(lista_alunos)):
                print(f"Aluno: {lista_alunos[i]["nome"]} | Media: {notas.calcular_media(matriz_notas, i):.2f}")
            
            print(f"\nMedia geral dos alunos: {notas.calcular_media_geral(matriz_notas):.2f}\n")
            print("=" * 35)

            utils.retornar()


        elif opcao == "0":
            utils.salvar_dados(ARQUIVO_DADOS, lista_alunos, matriz_notas)
            print("Dados salvos. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()