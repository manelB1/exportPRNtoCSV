import csv

# Inicialize listas vazias para armazenar os dados
produtos = []
marcas = []
precos = []
composicoes = []
finalidades = []

# Abra o arquivo .prn para leitura
with open('dados.PRN', 'r') as file:
    # Inicialize uma variável para rastrear os detalhes do produto atual
    produto_atual = {}

    # Leia cada linha do arquivo
    for line in file:
        # Se a linha estiver em branco, isso indica o final de um registro de produto
        if line.strip() == "":
            # Adicione os detalhes do produto atual às listas correspondentes
            produtos.append(produto_atual.get('Produto', ''))
            marcas.append(produto_atual.get('Marca', ''))
            precos.append(produto_atual.get('Preco', ''))
            composicoes.append(produto_atual.get('Composicao', ''))
            finalidades.append(produto_atual.get('Finalidade', ''))

            # Limpe o dicionário do produto atual para o próximo produto
            produto_atual = {}
        else:
            # Separe a linha em chave e valor com base no caractere ':'
            chave, valor = line.strip().split(": ", 1)
            produto_atual[chave] = valor

# Crie um dicionário com as colunas e seus dados
data = {
    'Produto': produtos,
    'Marca': marcas,
    'Preco': precos,
    'Composicao': composicoes,
    'Finalidade': finalidades
}

# Exporte os dados para um arquivo CSV
with open('dados.csv', 'w', newline='') as csv_file:
    fieldnames = ['Produto', 'Marca', 'Preco', 'Composicao', 'Finalidade']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for row in zip(produtos, marcas, precos, composicoes, finalidades):
        writer.writerow({field: value for field, value in zip(fieldnames, row)})

print("Os dados foram exportados para dados.csv")
