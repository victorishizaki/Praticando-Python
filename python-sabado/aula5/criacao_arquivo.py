import csv
# criar e escrever um arquivo TXT
# w --> write --> Escrita
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome,Idade,Cidade\n")
    arquivo.write("João,25,São Paulo\n")
    arquivo.write("Maria,30,Rio de Janeiro\n")
    
# Ler o conteúdo
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Conteúdo do Arquivo txt:")
    print("")
    print(arquivo.read())
    
# Criando arquivo csv

dados = [
    ["Nome", "Idade", "Cidade"],
    ["João", 25, "São Paulo"],
    ["Maria", 30, "Rio de Janeiro"],
    ["Rafael", 35, "Belo Horizonte"]
]

# Criar arquivo csv
with open("dados.csv", "w", newline="" ,encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)
    
# Ler o arquivo csv
with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print("\n Conteúdo do Arquivo CSV:")
    for linha in leitor:
        print(linha)