import json
import os

def carregar_estoque(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    return {}

def salvar_estoque(arquivo, estoque):
    with open(arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)

def adicionar_item(estoque):
    codigo = input("Digite o código do produto: ")
    if codigo in estoque:
        print("Código já existente no estoque!")
        return

    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))

    estoque[codigo] = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    print("Item adicionado com sucesso!")

def atualizar_item(estoque):
    codigo = input("Digite o código do produto a ser atualizado: ")
    if codigo not in estoque:
        print("Código não encontrado no estoque!")
        return

    print(f"Produto atual: {estoque[codigo]}")
    nome = input("Digite o novo nome do produto (ou pressione Enter para manter o atual): ")
    quantidade = input("Digite a nova quantidade (ou pressione Enter para manter a atual): ")
    preco = input("Digite o novo preço (ou pressione Enter para manter o atual): ")

    if nome:
        estoque[codigo]["nome"] = nome
    if quantidade:
        estoque[codigo]["quantidade"] = int(quantidade)
    if preco:
        estoque[codigo]["preco"] = float(preco)

    print("Item atualizado com sucesso!")

def remover_item(estoque):
    codigo = input("Digite o código do produto a ser removido: ")
    if codigo in estoque:
        del estoque[codigo]
        print("Item removido com sucesso!")
    else:
        print("Código não encontrado no estoque!")

def visualizar_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    for codigo, detalhes in estoque.items():
        print(f"Código: {codigo}, Nome: {detalhes['nome']}, Quantidade: {detalhes['quantidade']}, Preço: R${detalhes['preco']:.2f}")

def menu():
    print("\nControle de Estoque")
    print("1. Adicionar item")
    print("2. Atualizar item")
    print("3. Remover item")
    print("4. Visualizar estoque")
    print("5. Sair")

def main():
    arquivo_json = "estoque.json"
    estoque = carregar_estoque(arquivo_json)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_item(estoque)
        elif opcao == "2":
            atualizar_item(estoque)
        elif opcao == "3":
            remover_item(estoque)
        elif opcao == "4":
            visualizar_estoque(estoque)
        elif opcao == "5":
            salvar_estoque(arquivo_json, estoque)
            print("Estoque salvo. Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
