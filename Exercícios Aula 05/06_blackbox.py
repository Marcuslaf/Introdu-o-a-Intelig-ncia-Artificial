import json
import os

# Função para carregar o estoque do arquivo JSON
def carregar_estoque():
    if os.path.exists('estoque.json'):
        with open('estoque.json', 'r') as file:
            return json.load(file)
    return {}

# Função para salvar o estoque no arquivo JSON
def salvar_estoque(estoque):
    with open('estoque.json', 'w') as file:
        json.dump(estoque, file, indent=4)

# Função para adicionar um item ao estoque
def adicionar_item(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    salvar_estoque(estoque)
    print(f'Item "{nome}" adicionado com sucesso!')

# Função para visualizar o estoque
def visualizar_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("Estoque atual:")
        for nome, quantidade in estoque.items():
            print(f'- {nome}: {quantidade}')

# Função para atualizar a quantidade de um item
def atualizar_item(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        salvar_estoque(estoque)
        print(f'Item "{nome}" atualizado para {quantidade}.')
    else:
        print(f'Item "{nome}" não encontrado no estoque.')

# Função principal
def main():
    estoque = carregar_estoque()

    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Visualizar estoque")
        print("3. Atualizar item")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            adicionar_item(estoque, nome, quantidade)
        elif opcao == '2':
            visualizar_estoque(estoque)
        elif opcao == '3':
            nome = input("Nome do item: ")
            quantidade = int(input("Nova quantidade: "))
            atualizar_item(estoque, nome, quantidade)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()