eleitores = int(input("Digite o nº de eleitores: "))
branco = int(input("Digite o nº de branco: "))
nulos = int(input("Digite o nº de nulos: "))
validos = int(input("Digite o nº de validos: "))

total_votos = branco + nulos + validos

if total_votos  > eleitores:
    print("Total votantes nao registrados: ")
    exit()
else:
    total_votos == eleitores
    print("_________________________________________________")
    print("Todos municipios foram registrados")
    print("")
    
porcentagem_branco = branco/eleitores*100
porcentagem_nulos = nulos/eleitores*100
porcentagem_validos = validos/eleitores*100

print("Porcentagem de votos brancos: ", porcentagem_branco,"%")
print("Porcentagem de votos nulos: ", porcentagem_nulos,"%")
print("Porcentagem de votos validos:", porcentagem_validos,"%")


