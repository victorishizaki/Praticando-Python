palavra = input("Digite uma palavra: ").lower().strip().replace(" ", "")
palindromo = palavra == palavra[::-1]

if palindromo:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")