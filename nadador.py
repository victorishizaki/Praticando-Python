
idade = int(input("Digite sua idade: "))

if (idade >= 5) and (idade <= 7):
    print("Sua categoria é Infantil A")
    
elif (idade >= 8) and (idade <= 10):
    print("Sua categoria é Infantil B")

elif (idade >= 11) and (idade <= 13):
    print("Sua categoria é Juvenil A")

elif (idade >= 14) and (idade <= 17):
    print("Sua categoria é Juvenil B")

elif (idade > 18) and (idade <=25):
    print("Sua categoria é Senior")
    
else:
    print("O nadador não pertence a uma categoria")
    


