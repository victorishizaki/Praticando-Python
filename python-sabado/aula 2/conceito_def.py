def carro_mateus():
    print("Pegeout 206 turbo")
    
carro_mateus()

def escrever_carro(nome):
    print(nome)
    
escrever_carro("marea turbo")

def somar_numeros(num1, num2):
    return num1 + num2

resultado = somar_numeros(5, 10)
print("O resultado é: ", resultado)

""" Exercício do Cinema utilizando def """

def verificaIdade(idade):
    if idade >= 18:
        return "Pode ver o filme"
    else:
        return "Não pode ver o filme"
    
print("Digite sua idade: ")
idade = int(input())

resultadoCinema = verificaIdade(idade)

print(resultadoCinema)

