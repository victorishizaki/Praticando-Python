import mysql.connector
from config import Config

class UsuarioModel:

    def __init__(self):
        self.config = Config()
        
        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )
        
        self.cursor = self.connection.cursor(dictionary=True)
        
    def get_all_users(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()
    
    def insert_user(self, nome, idade, email):
        self.cursor.execute("INSERT INTO usuarios (nome, idade, email) VALUES (%s, %s, %s)", (nome, idade, email))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
        return self.cursor.fetchone()
    
    def delete_produto_by_id(self, user_id):
        self.cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
        self.connection.commit()
        return self.cursor.rowcount
    
    def update_user(self, user_id, nome, idade, email):
        self.cursor.execute("UPDATE usuarios SET nome = %s, idade = %s, email = %s WHERE id = %s", (nome, idade, email, user_id))
        self.connection.commit()
        return self.cursor.rowcount
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        
