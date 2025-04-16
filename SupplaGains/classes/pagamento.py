class Pagamento:
    def simular_pagamento(self, total):
        print("Formas de pagamento:")
        print("1. Dinheiro (10% de desconto)")
        print("2. PIX (5% de desconto)")
        print("3. Cartão (acréscimo de 5%)")
        opcao = input("Escolha a forma de pagamento: ")
        if opcao == "1":
            total *= 0.90
        elif opcao == "2":
            total *= 0.95
        elif opcao == "3":
            total *= 1.05
        else:
            print("Opção inválida. Valor não alterado.")
        return total
