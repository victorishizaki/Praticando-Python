print("")

while True:
    carro = input("Qual o nome do veiculo?: ")
    print("")

    preco = float(input("Preço: "))
    print("")

    if preco <= 0:
        print("O preço não pode ser negativo. Tente novamente.")
        print("")
        continue

    if preco >= 80000:
        print("Seu verículo", carro, "tem desconto de 60%", "com valor final de R$", preco * 0.40)
        print("")
    elif preco >= 50000:
        print("Seu verículo", carro, "tem desconto de 30%", "com valor final de R$", preco * 0.70)
        print("")
    elif preco <= 50000:
        print("Seu verículo", carro, "não tem desconto", "com valor final de R$", preco)
        print("")
    else:
        print("")
        exit
    
    
