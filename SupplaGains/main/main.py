import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.estoque import Estoque
from classes.carrinho import Carrinho
from classes.produto import Produto
from classes.pagamento import Pagamento

class Loja:
    def __init__(self):
        self.estoque = Estoque()
        self.carrinho = Carrinho()
        self.pagamento = Pagamento()
        self.iniciar_produtos()
        self.menu()

    def iniciar_produtos(self):
        self.estoque.adicionar_produto(Produto(1, "Creatina", 250.0, 10))
        self.estoque.adicionar_produto(Produto(2, "Whey Protein", 119.90, 8))
        self.estoque.adicionar_produto(Produto(3, "Pré-treino", 109.90, 6))
        self.estoque.adicionar_produto(Produto(4, "Multivitamínico", 89.90, 12))

    def mostrar_produtos_e_comprar(self):
        while True:
            print("\n=== Nossos produtos ===")
            self.estoque.listar_produtos()
            try:
                id_prod = int(input("Digite o ID do produto para adicionar ao carrinho (0 para voltar): "))
                if id_prod == 0:
                    break
                qtd = int(input("Quantidade: "))
                produto = self.estoque.obter_produto_por_id(id_prod)
                if produto:
                    self.carrinho.adicionar_item(produto, qtd)
                    escolha = input("Deseja (C) Continuar comprando ou (F) Fechar pedido? ").lower()
                    if escolha == "f":
                        self.finalizar_compra()
                        break
                else:
                    print("Produto não encontrado.")
            except ValueError:
                print("Entrada inválida.")

    def exibir_carrinho(self):
        print("\n=== Seu carrinho ===")
        self.carrinho.exibir_itens()
        if self.carrinho.itens:
            print(f"Total: R${self.carrinho.calcular_total():.2f}")
            escolha = input("Deseja (F) Finalizar compra ou (V) Voltar ao menu? ").lower()
            if escolha == "f":
                self.finalizar_compra()

    def finalizar_compra(self):
        total = self.carrinho.calcular_total()
        print(f"Total sem desconto: R${total:.2f}")
        total_final = self.pagamento.simular_pagamento(total)
        print(f"Total final: R${total_final:.2f}")
        print("Pagamento realizado com sucesso!")
        self.carrinho.esvaziar()
        escolha = input("Deseja (V) Voltar ao menu principal ou (S) Sair? ").lower()
        if escolha == "s":
            print("Obrigado por comprar na Suppla Gains!")
            exit()

    def menu(self):
        while True:
            print("\n=== SuppLa Gains ===")
            print("1. Nossos produtos")
            print("2. Adicionar produtos ao carrinho")
            print("3. Ver carrinho")
            print("4. Finalizar compra")
            print("5. Sair")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1 or opcao == 2:
                    self.mostrar_produtos_e_comprar()
                elif opcao == 3:
                    self.exibir_carrinho()
                elif opcao == 4:
                    self.finalizar_compra()
                elif opcao == 5:
                    print("Saindo da loja. Volte sempre!")
                    break
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Por favor, insira um número válido.")

if __name__ == "__main__":
    Loja()
