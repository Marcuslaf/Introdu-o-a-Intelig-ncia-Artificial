import json

def criar_estoque():
    return {}

def adicionar_produto(estoque, produto, quantidade, preco):
    estoque[produto] = {'quantidade': quantidade, 'preco': preco}

def remover_produto(estoque, produto):
    estoque.pop(produto, None)

def atualizar_produto(estoque, produto, quantidade=None, preco=None):
    if produto in estoque:
        if quantidade is not None:
            estoque[produto]['quantidade'] = quantidade
        if preco is not None:
            estoque[produto]['preco'] = preco

def consultar_estoque(estoque):
    return estoque

def salvar_estoque(estoque, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(estoque, f)

def carregar_estoque(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return criar_estoque()