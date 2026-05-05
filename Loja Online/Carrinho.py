
class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)
        print(f"{produto.nome} foi adicionado ao carrinho")

    def exibir_resumo(self):
        print("\n --- Resumo do Carrinho ---")
        total = 0

        for item in self.itens:
            item.exibir_detalhes()
            total += item.get_preco()
            print(f"Total a pagar: R$ {total}")
            print("-"*45)

    def remover_produto(self, nome_do_produto):
        for item in self.itens:
            if item.nome == nome_do_produto:
                self.itens.remove(item)
                print(f"\n--- !{nome_do_produto} removido do Carrinho! ---")
                return
            print(f"\nProduto '{nome_do_produto}' não encontrado no carrinho.")