import json
from pathlib import Path

class BancoFake:
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()  # Carrega os dados do arquivo JSON, se existir

    def _carregar(self):
        """
        Carregar os dados do arquivo JSON, se existir.
        Caso não exista, inicia com dados vazios.
        """
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            # Abrindo arquivo no modo de leitura em UTF-8 (PT-BR)
            with open(caminho, 'r', encoding="utf-8") as data:
                # Salvando dados que já existem no arquivo na variável dados
                self.dados = json.load(data)
        else:
            self._salvar()

    def _salvar(self):
        """
        Salvar os dados (self.dados) no arquivo JSON.
        """
        # Abrindo arquivo no modo de escrita W
        with open(self.arquivo_db, 'w', encoding="utf-8") as data:
            # Realizando DUMP (Python para JSON) para salvar no banco
            json.dump(self.dados, data, ensure_ascii=False, indent=4)

    def adicionar_cliente(self, cliente_dict):
        """
        Adiciona um cliente ao banco de dados.
        """
        self.dados["clientes"].append(cliente_dict)
        self._salvar()

    def listar_clientes(self):
        """
        Retorna a lista de clientes.
        """
        return self.dados["clientes"]

    def adicionar_produto(self, produto_dict):
        """
        Adiciona um produto ao banco de dados.
        """
        self.dados["produtos"].append(produto_dict)
        self._salvar()

    def listar_produtos(self):
        """
        Retorna a lista de produtos.
        """
        return self.dados["produtos"]