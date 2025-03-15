import mysql.connector
from config import Config

class ProdutoModel:
    
    def __init__(self):
        # Iniciando a configuração
        self.config = Config()
        
        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )
        
        # Faz o cursor trazendo os dados da base de dados (o resultado em dicionarios)
        self.cursor = self.connection.cursor(dictionary=True)
        
    def get_all_products(self):
        # Executa a query
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()
    
    def insert_product(self, nome, preco):
        self.cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco ))
        self.connection.commit() # Confirmando a transação
        return self.cursor.lastrowid # Retornando o id do produto inserido
    
    def get_product_by_id(self, product_id):
        self.cursor.execute("SELECT * FROM produtos WHERE id = %s", (product_id,))
        return self.cursor.fetchone()
    
    def delete_product_by_id(self, product_id):
        self.cursor.execute("DELETE FROM produtos WHERE id = %s", (product_id,))
        self.connection.commit()
        return self.cursor.rowcount # Retornando a quantidade de linhas afetadas
    
    def update_product_by_id(self, product_id, nome, preco):
        self.cursor.execute("UPDATE produtos SET nome = %s, preco = %s WHERE id = %s", (nome, preco, product_id))
        self.connection.commit()
        return self.cursor.rowcount # Retornando a quantidade de linhas afetadas

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
    
    
    
    
