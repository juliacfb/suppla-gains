from classes.produto import Produto

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"ID: {produto.id} | Nome: {produto.nome} | Preço: R${produto.preco:.2f} | Estoque: {produto.estoque}")

    def obter_produto_por_id(self, id):
        for produto in self.produtos:
            if produto.id == id:
                return produto
        return None
