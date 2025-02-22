from app.controllers.clienteController import clienteController
from app.controllers.produtoController import produtoController

def exibir_menu():
    print("\n===== Menu =====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produto")
    print("4 - Listar Produtos")
    print("0 - Sair do Sistema")

def main():
    cntrlCliente = clienteController()
    cntrlProduto = produtoController()

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome do Cliente: ")
            email = input("E-mail: ")
            idade = int(input("Idade: "))
            cntrlCliente.criar_cliente(nome, email, idade)

        elif opc == "2":
            clientes = cntrlCliente.listar_clientes()
            for index, cliente in enumerate(clientes, 1):
                print(f"{index}. {cliente}")

        elif opc == "3":
            nome = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            cntrlProduto.criar_produto(nome, preco)

        elif opc == "4":
            produtos = cntrlProduto.listar_produtos()
            for index, produto in enumerate(produtos, 1):
                print(f"{index}. Produto(nome={produto['nome']}, preco={produto['preco']})")

        elif opc == "0":
            print("Saindo do Sistema...")
            break
        else:
            print("Opção Inválida. Tente novamente.")

if __name__ == "__main__":
    main()