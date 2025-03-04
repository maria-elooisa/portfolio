estoque = []

# Início do Usuário
print("BEM-VINDO AO CADASTRO DE SUAS COMPRAS")
print("")
run = int(input('Digite 1 para cadastrar produtos ou 0 para sair: '))

while run == 1:
    produto_nome = input('Nome do Produto: ')
    produto_quantidade = int(input('Quantidade: '))
    produto_preco = float(input('Preço: '))

    # Criando a tupla com os dados do produto
    produto = (produto_nome, produto_quantidade, produto_preco)
    
    # Adicionando ao estoque
    estoque.append(produto)
    print(estoque)

    print("Produto Inserido!")
    print("")
    run = int(input('Digite 1 para cadastrar novos produtos ou 0 para sair: '))

# Exibindo o estoque
print("\n...................... ESTOQUE .....................")
print("Nome do Produto - Quantidade - Preço - Valor Total")

for nome, quantidade, preco in estoque:
    valor_total = quantidade * preco
    print(f"{nome} ----- {quantidade} ----- R${preco:.2f} ----- R${valor_total:.2f}")
