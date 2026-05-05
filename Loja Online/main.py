
from Roupa import Roupa
from Eletronico import Eletronico
from Carrinho import CarrinhoDeCompras
import os

def back():
    back = input("0 --> Back: ")

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    limpar()
    print("\n" + "="*45)
    print("🌐 Loja Online".center(45))
    print("="*45)
    print("1- Adicionar Roupa")
    print("2- Adicionar Eletronico")
    print("3- Ver Resumo do Carrinho")
    print("4- Remover item do carrinho")
    print("0- Sair")
    print("="*45)

def main():

    carrinho = CarrinhoDeCompras()

    print("\n Bem-vindo ao Sistema do Gestão de Loja")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar()
            print("\n --- Cadastrando Roupa ---")
            nome = input("Nome da roupa: ")

            try:
                preco = float(input("Preco: R$ "))
                tamanho = input("Tamanho (P/M/G): ")
                nova_roupa = Roupa(nome, preco, tamanho)
                carrinho.adicionar_produto(nova_roupa)
                back()
            except ValueError:
                print("ERRO: Por favor, digite um número! 3:<")

        elif opcao == "2":
            limpar()
            print("\n --- Cadastrando Eletrônico ---")
            nome = input("Nome do Eletrônico: ")

            try:
                preco = float(input("Preco: R$ "))
                voltagem = input("Voltagem (ex: 110V/220V): ")
                novo_eletronico = Eletronico(nome, preco, voltagem)
                carrinho.adicionar_produto(novo_eletronico)
                back()
            except ValueError:
                print("ERRO: Por favor, digite um número! 3:<")
                back()

        elif opcao == "3":
            limpar()
            carrinho.exibir_resumo()
            back()

        elif opcao == "4":
            limpar()
            carrinho.remover_produto()
            back()

        elif opcao == "0":
            print("Encerrando programa...")
            break
        else:
            print("\n ERRO: Opção inválida! Tente novamente...")
            back()

if __name__ == "__main__":
    main()
