class Cliente:
    
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
        
    def __str__(self):
        return f'Cliente: {self.nome}, Email: {self.email}, Idade: {self.idade}'