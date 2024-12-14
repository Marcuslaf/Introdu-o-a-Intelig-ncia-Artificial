import json
import os

class ControleEstoque:
    def __init__(self, arquivo_estoque='estoque.json'):
        self.arquivo_estoque = arquivo_estoque
        self.estoque = self.carregar_estoque()

    def carregar_estoque(self):
        """Carrega o estoque do arquivo JSON ou cria um novo se não existir."""
        if os.path.exists(self.arquivo_estoque):
            with open(self.arquivo_estoque, 'r') as arquivo:
                return json.load(arquivo)
        return {}

    def salvar_estoque(self):
        """Salva o estoque atual no arquivo JSON."""
        with open(self.arquivo_estoque, 'w') as arquivo:
            json.dump(self.estoque, arquivo, indent=4)

    def adicionar_produto(self, codigo, nome, quantidade, preco):
        """Adiciona um novo produto ao estoque."""
        if codigo in self.estoque:
            print(f"Produto com código {codigo} já existe. Use atualizar_produto().")
            return False
        
        self.estoque[codigo] = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco
        }
        self.salvar_estoque()
        print(f"Produto {nome} adicionado com sucesso!")
        return True

    def atualizar_produto(self, codigo, nome=None, quantidade=None, preco=None):
        """Atualiza as informações de um produto existente."""
        if codigo not in self.estoque:
            print(f"Produto com código {codigo} não encontrado.")
            return False
        
        if nome:
            self.estoque[codigo]['nome'] = nome
        if quantidade is not None:
            self.estoque[codigo]['quantidade'] = quantidade
        if preco is not None:
            self.estoque[codigo]['preco'] = preco
        
        self.salvar_estoque()
        print(f"Produto {codigo} atualizado com sucesso!")
        return True

    def remover_produto(self, codigo):
        """Remove um produto do estoque."""
        if codigo not in self.estoque:
            print(f"Produto com código {codigo} não encontrado.")
            return False
        
        del self.estoque[codigo]
        self.salvar_estoque()
        print(f"Produto {codigo} removido com sucesso!")
        return True

    def listar_produtos(self):
        """Lista todos os produtos em estoque."""
        if not self.estoque:
            print("Estoque vazio.")
            return
        
        print("\n--- ESTOQUE ATUAL ---")
        for codigo, dados in self.estoque.items():
            print(f"Código: {codigo}")
            print(f"Nome: {dados['nome']}")
            print(f"Quantidade: {dados['quantidade']}")
            print(f"Preço: R$ {dados['preco']:.2f}")
            print("--------------------")

    def buscar_produto(self, codigo):
        """Busca informações de um produto específico."""
        if codigo not in self.estoque:
            print(f"Produto com código {codigo} não encontrado.")
            return None
        
        return self.estoque[codigo]

def menu():
    """Menu interativo para manipulação do estoque."""
    controle = ControleEstoque()
    
    while True:
        print("\n--- CONTROLE DE ESTOQUE ---")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Remover Produto")
        print("4. Listar Produtos")
        print("5. Buscar Produto")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        try:
            if opcao == '1':
                codigo = input("Código do produto: ")
                nome = input("Nome do produto: ")
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço: R$ "))
                controle.adicionar_produto(codigo, nome, quantidade, preco)
            
            elif opcao == '2':
                codigo = input("Código do produto a atualizar: ")
                nome = input("Novo nome (deixe em branco para não alterar): ") or None
                quantidade = input("Nova quantidade (deixe em branco para não alterar): ")
                quantidade = int(quantidade) if quantidade else None
                preco = input("Novo preço (deixe em branco para não alterar): ")
                preco = float(preco) if preco else None
                controle.atualizar_produto(codigo, nome, quantidade, preco)
            
            elif opcao == '3':
                codigo = input("Código do produto a remover: ")
                controle.remover_produto(codigo)
            
            elif opcao == '4':
                controle.listar_produtos()
            
            elif opcao == '5':
                codigo = input("Código do produto a buscar: ")
                produto = controle.buscar_produto(codigo)
                if produto:
                    print("\nDetalhes do Produto:")
                    print(f"Nome: {produto['nome']}")
                    print(f"Quantidade: {produto['quantidade']}")
                    print(f"Preço: R$ {produto['preco']:.2f}")
            
            elif opcao == '6':
                print("Saindo do sistema...")
                break
            
            else:
                print("Opção inválida. Tente novamente.")
        
        except ValueError:
            print("Entrada inválida. Verifique os valores digitados.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    menu()