# Crie uma classe chamada ContaBancaria com os métodos depositar e sacar. Utilize tratamento de exceções para lidar com saques maiores que o saldo disponível, criando uma exceção personalizada.

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        super().__init__(f"Saldo insuficiente. Saldo atual: {saldo_atual}, Valor do saque: {valor_saque}")


class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")
    
    def sacar(self, valor):
        try:
            if valor > self.saldo:
                raise SaldoInsuficienteError(self.saldo, valor)
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")

        except SaldoInsuficienteError as e:
            print("Erro:", e)

try:
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    conta = ContaBancaria(saldo_inicial)

    while True:
        print("\nOpções:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor_deposito = float(input("Digite o valor do depósito: "))
            conta.depositar(valor_deposito)
        elif opcao == '2':
            valor_saque = float(input("Digite o valor do saque: "))
            conta.sacar(valor_saque)
        elif opcao == '3':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

except ValueError:
    print("Erro: Por favor, insira um valor numérico válido.")
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
except Exception as e:
    print("Erro inesperado:", e)
