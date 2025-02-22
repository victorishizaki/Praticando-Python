print("Conforme sua idade iremos categorizar sua fixa etária para filmes no nosso cinema:")
idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Você é maior de idade e pode assistir filmes +18")

elif idade >= 16 and idade <= 18:
    print("Você tem:", idade, "anos de idade e pode assistir filmes de 16 anos")

elif idade >= 14 and idade <= 16:
    print("Você tem: ", idade, "anos de idade e pode assistir filmes de 14 anos")

elif idade >= 12 and idade <= 14:
    print("Você tem: ", idade, "anos de idade e pode assistir filmes de 12 anos")

elif idade >= 10 and idade <= 12:
    print("Você tem: ", idade, "anos de idade e pode assistir filmes de 10 anos")

else:
    print("Você tem: ", idade,
          "anos de idade e pode assistir filmes de classificação Livre")