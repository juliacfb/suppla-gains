class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.itens.append((produto, quantidade))
            produto.atualizar_estoque(quantidade)
        else:
            print("Quantidade indisponível em estoque.")

    def exibir_itens(self):
        if not self.itens:
            print("Carrinho vazio.")
            return
        for produto, qtd in self.itens:
            print(f"{produto.nome} - {qtd} un - R${produto.preco * qtd:.2f}")

    def calcular_total(self):
        return sum(produto.preco * qtd for produto, qtd in self.itens)

    def esvaziar(self):
        self.itens.clear()
