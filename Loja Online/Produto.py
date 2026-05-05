
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    def get_preco(self):
        return self._preco
    
    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preco: R$ {self._preco}")
