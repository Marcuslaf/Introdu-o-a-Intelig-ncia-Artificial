import json
import os

# Nome do arquivo JSON para armazenar os dados do estoque
ARQUIVO_ESTOQUE = "estoque.json"

def carregar_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, 'r') as arquivo:
            return json.load(arquivo)
    return {}

def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)

def adicionar_item(estoque, nome, quantidade):
    if nome in estoque:
        print(f"O item '{nome}' já existe no estoque. Use a opção de atualizar.")
    else:
        estoque[nome] = quantidade
        print(f"Item '{nome}' adicionado ao estoque com quantidade {quantidade}.")

def atualizar_item(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Quantidade do item '{nome}' atualizada para {quantidade}.")
    else:
        print(f"O item '{nome}' não existe no estoque. Use a opção de adicionar.")

def remover_item(estoque, nome):
    if nome in estoque:
        del estoque[nome]
        print(f"Item '{nome}' removido do estoque.")
    else:
        print(f"O item '{nome}' não existe no estoque.")

def exibir_estoque(estoque):
    if estoque:
        print("\nEstoque atual:")
        for item, quantidade in estoque.items():
            print(f"{item}: {quantidade}")
    else:
        print("O estoque está vazio.")

def main():
    estoque = carregar_estoque()

    while True:
        print("\n=== Controle de Estoque ===")
        print("1. Adicionar item")
        print("2. Atualizar quantidade")
        print("3. Remover item")
        print("4. Exibir estoque")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            adicionar_item(estoque, nome, quantidade)
        elif opcao == '2':
            nome = input("Nome do item: ")
            quantidade = int(input("Nova quantidade: "))
            atualizar_item(estoque, nome, quantidade)
        elif opcao == '3':
            nome = input("Nome do item a ser removido: ")
            remover_item(estoque, nome)
        elif opcao == '4':
            exibir_estoque(estoque)
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        salvar_estoque(estoque)

if __name__ == "__main__":
    main()