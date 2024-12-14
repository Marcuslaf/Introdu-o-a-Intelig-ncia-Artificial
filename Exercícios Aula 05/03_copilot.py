import json

# Carregar dados de estoque de um arquivo JSON
def carregar_estoque(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Salvar dados de estoque em um arquivo JSON
def salvar_estoque(nome_arquivo, estoque):
    with open(nome_arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)

# Adicionar um novo item ao estoque
def adicionar_item(estoque, nome, quantidade):
    if nome in estoque:
        print(f"O item {nome} já existe no estoque.")
    else:
        estoque[nome] = quantidade
        print(f"Item {nome} adicionado com sucesso.")

# Atualizar a quantidade de um item existente no estoque
def atualizar_item(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
        print(f"Item {nome} atualizado com sucesso.")
    else:
        print(f"O item {nome} não existe no estoque.")

# Exibir o estoque atual
def exibir_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
    else:
        for nome, quantidade in estoque.items():
            print(f"{nome}: {quantidade}")

def main():
    nome_arquivo = 'estoque.json'
    estoque = carregar_estoque(nome_arquivo)

    while True:
        print("\nControle de Estoque")
        print("1. Adicionar Item")
        print("2. Atualizar Item")
        print("3. Exibir Estoque")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            adicionar_item(estoque, nome, quantidade)
            salvar_estoque(nome_arquivo, estoque)
        elif escolha == '2':
            nome = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            atualizar_item(estoque, nome, quantidade)
            salvar_estoque(nome_arquivo, estoque)
        elif escolha == '3':
            exibir_estoque(estoque)
        elif escolha == '4':
            salvar_estoque(nome_arquivo, estoque)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()