def menu():
    print("Menu da Calculadora")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("9 - Sair")
    
def somar(n1, n2):
        return  n1 + n2
    
def subtrair(n1, n2):
        return n1 - n2
    
def multiplicar(n1, n2):
        return n1 * n2
    
def dividir(n1, n2):
        if n2 == 0:
            return "Erro! Divisão por zero"
        return n1 / n2

def verificaOpcao(opcao):
        if opcao == 1:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(somar(num1, num2))
        elif opcao == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(subtrair(num1, num2))
        elif opcao == 3:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(multiplicar(num1, num2))
        elif opcao == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(dividir(num1, num2))
        elif opcao == 9:
            print("Saindo...")
            
def calculadora():
        while True:
            menu()
            opcao = int(input("Escolha uma opção: "))
            verificaOpcao(opcao)
    
calculadora()