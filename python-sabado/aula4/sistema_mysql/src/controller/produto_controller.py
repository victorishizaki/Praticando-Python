from ..model.produto_model import ProdutoModel
#from model.produto_model import ProdutoModel

def listar_produtos():
    # Retorna a lista de todos os produtos (dict)
    model = ProdutoModel()
    produtos = model.get_all_products()
    model.close_connection()
    return produtos

def cadastrar_produto(nome, preco):
    # Cadastra um novo produto
    model = ProdutoModel()
    novo_id = model.insert_product(nome, preco)
    model.close_connection()
    return novo_id

def atualizar_produto(produto_id, nome, preco):
    # Atualiza um produto existente
    model = ProdutoModel()
    linhas_afetadas = model.update_product_by_id(produto_id, nome, preco)
    model.close_connection()
    return linhas_afetadas

def remover_produto(produto_id):
    # Exclui um produto existente
    model = ProdutoModel()
    linhas_afetadas = model.delete_product_by_id(produto_id)
    model.close_connection()
    return linhas_afetadas

def obter_produto(produto_id):
    # Retorna um produto específico (dict)
    model = ProdutoModel()
    produto = model.get_product_by_id(produto_id)
    model.close_connection()
    return produto

