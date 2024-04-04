# %%

import time
import datetime
import json
import random

# Função para gerar um produto aleatório
def gerar_produto():
    descricao = f"Produto {random.randint(1, 100)}"
    tamanho = random.randint(1, 100)
    aprovacao = random.choice([True, False])
    data = datetime.datetime.now().isoformat()
    return {"descricao": descricao, "tamanho": tamanho, "aprovacao": aprovacao, "data": data}

# Função para salvar produtos em um arquivo JSON
def salvar_produtos(produtos, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)

# Lista para armazenar os produtos gerados
produtos_gerados = []

# Simulação da esteira de fábrica
while True:
    produto = gerar_produto()
    produtos_gerados.append(produto)
    print(f"Produto gerado: {produto}")
    
    # Salva os produtos a cada 10 produtos gerados
    if len(produtos_gerados) % 10 == 0:
        salvar_produtos(produtos_gerados, 'produtos.json')
        print("Produtos salvos no arquivo JSON.")
    
    # Aguarda 6 segundos para simular a geração de 10 produtos por minuto
    time.sleep(6)
# %%
