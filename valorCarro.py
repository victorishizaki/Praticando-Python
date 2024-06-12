custo_fabrica = float(input("Digite o valor de fabrica: R$"))
print("") #Pular uma linha

custo_fabrica_final = custo_fabrica

valor_distribuidora = custo_fabrica * 28/100
print("Valor da distribuidora: R$", valor_distribuidora)
print("")

custo_imposto = custo_fabrica * 45/100
print("Valor do imposto: R$", custo_imposto)
print("")

valor_consumidor = (valor_distribuidora + custo_imposto + custo_fabrica_final)
print("O valor do consumidor é: R$", valor_consumidor)
print("\n") #pular duas linhas
