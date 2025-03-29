import pandas as pd
import matplotlib.pyplot as plt

# croar os dados para o nosso dataframe

dados = {
    "Nome": ["Arthur", "João", "Maria", "Pedro", "Lucas"],
    "Idade": [25, 30, 35, 40, 45],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Curitiba"]
}

df = pd.DataFrame(dados)
#Exibir os dados do dataframe
print(df)

# salvar o dataframe em um arquivo csv
df.to_csv("pandas_dados.csv", index=False)

# visualizar em dataframe o CSV
df = pd.read_csv("pandas_dados.csv")

df_filtrado = df[df["Idade"] > 20]
print(df_filtrado) # Todas as pessoas com menos de 20 anos não aparecem

df_ordenado = df.sort_values(by="Idade", ascending=False)
print(df_ordenado) # Do maior para o menor (Decrescente)

# Exibir estatisticas
print(df.describe())

media_cidade = df.groupby("Cidade") ["Idade"].mean()
print(media_cidade) # Média de idade por cidade

"""
# criando gráfico
# kind (bar - barras, line - linha, pie - pizza, scatter - pontos)
df.plot(kind="bar", x="Nome", y="Idade", color="blue")
plt.title("idade das Pessoas")
plt.xlabel("Nome")
plt.ylabel("Idade")
plt.show()
"""

df.boxplot(column="Idade", by="Cidade", grid="False")
plt.title("Distribuição de Idades por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Idade")
plt.show()
