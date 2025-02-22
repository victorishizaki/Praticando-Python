from ..models.produto import Produto
from ..database.database import BancoFake

class produtoController:
    def __init__(self):
        # Conexão com o banco
        self.db = BancoFake()

    def criar_produto(self, nome, preco):
        """
        Cria um novo produto e salva no banco de dados.
        """
        # Cria o objeto Produto
        novo_produto = Produto(nome, preco)
        # Converte para dict (JSON)
        dict_produto = {
            "nome": novo_produto.nome,
            "preco": novo_produto.preco
        }
        # Salva no banco
        self.db.adicionar_produto(dict_produto)
        print("Produto cadastrado com sucesso!")

    def listar_produtos(self):
        """
        Retorna uma lista com todos os produtos cadastrados.
        """
        return self.db.listar_produtos()