valor_final = 0

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}:") #numerar os nomes e precos
    preco = float(input(f"Digite o preço do produto {i+1}:"))
    qntd = int(input(f"Digite a quantidade do produto {i+1}:"))
    valor_compra = preco * qntd

valor_final += valor_compra

print("Aqui está seu recibo")
print(f"""
    Produto {nome}, preço {preco}, comprado em {qntd}
    total: {valor_final}
""")
    