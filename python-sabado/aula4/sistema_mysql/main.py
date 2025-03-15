from src.controller import produto_controller
from src.controller import usuario_controller


def exibir_menu():
    print("\n MAREA TOCA TUDO LTDA!")
    print("\n ==========    MENU    ==========")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - Buscar Produto") 
    print("\n ============================")
    print("6 - Cadastrar Usuário")
    print("7 - Listar Usuário")
    print("8 - Atualizar Usuário")
    print("9 - Deletar Usuário")
    print("10 - Buscar Usuário")
    print("0 - Sair")
    print("\n ============================")
    
def listar_produtos():
    print("\n Produtos Cadastrados:")
    produtos = produto_controller.listar_produtos()
    if produtos:
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco: {produto['preco']}")
    else:
        print("Nenhum produto cadastrado")
            
def cadastrar_produto():
    print("\n--- Cadastrar Produto ---")
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preco do produto: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso! ID: {novo_id}")
        
def opcao_atualizar():
    print("\n--- Atualizando o Produto ---")
    produto_id = input("Digite o ID do produto: ")
    nome = input("Digite o novo nome do produto: ")
    preco = input("Digite o novo preco do produto: ")
        
    linhas = produto_controller.atualizar_produto(produto_id, nome, preco)

    if linhas > 0: # quantidade de linhas modificadas
        print(f"Produto atualizado com sucesso! ID: {produto_id}")
    else:
        print("Nenhum produto foi atualizado")  
            
def opcao_deletar():
    print("\n--- Deletando o Produto ---")
    produto_id = input("Digite o ID do produto: ")
    linhas = produto_controller.remover_produto(produto_id)
    if linhas > 0:
        print(f"Produto deletado com sucesso! ID: {produto_id}")
    else:
        print("Nenhum produto foi deletado")

def opcao_buscar():
    print("\n--- Buscando o Produto ---")
    produto_id = input("Digite o ID do produto: ")
    produto = produto_controller.obter_produto(produto_id)
    if produto:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco: {produto['preco']}")
    else:
        print("Produto não encontrado")
        
""" ======================  USUARIO ======================"""

def cadastrar_usuario():
    print("\n--- Cadastrar Usuario ---")
    nome = input("Digite o nome do usuario: ")
    email = input("Digite o email do usuario: ")
    idade = input("Digite a idade do usuario: ")
    novo_id = usuario_controller.cadastrar_usuario(nome, email, idade)
    print(f"Usuario cadastrado com sucesso! ID: {novo_id}")
    
def opcao_atualizar_usuario():
    print("\n--- Atualizando o Usuario ---")
    usuario_id = input("Digite o ID do usuario: ")
    nome = input("Digite o novo nome do usuario: ")
    email = input("Digite o novo email do usuario: ")
    idade = input("Digite a nova idade do usuario: ")
    
    linhas = usuario_controller.atualizar_usuario(usuario_id, nome, email, idade)
    
    if linhas > 0:
        print(f"Usuario atualizado com sucesso! ID: {usuario_id}")
    else:
        print("Nenhum usuario foi atualizado")
        
def opcao_deletar_usuario():
    print("\n--- Deletando o Usuario ---")
    usuario_id = input("Digite o ID do usuario: ")
    
    linhas = usuario_controller.remover_usuario(usuario_id)
    
    if linhas > 0:
        print(f"Usuario deletado com sucesso! ID: {usuario_id}")
    else:
        print("Nenhum usuario foi deletado")
        
def opcao_buscar_usuario():
    print("\n--- Buscando o Usuario ---")
    usuario_id = input("Digite o ID do usuario: ")
    usuario = usuario_controller.obter_usuario(usuario_id)
    if usuario:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")
    else:
        print("Usuario não encontrado")
 
            
def main():
    while True:
        exibir_menu()
        opc = input("Digite a opção desejada: ")
        
        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            opcao_atualizar()
        elif opc == "4":
            opcao_deletar()
        elif opc == "5":
            opcao_buscar()
        else:
            print("Opção inválida. Tente novamente!")    

if __name__ == "__main__":
    main()
