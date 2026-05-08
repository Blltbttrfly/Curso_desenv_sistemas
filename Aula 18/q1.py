# 1. Lista de compras
# Crie uma lista com 5 itens de supermercado. Exiba o
# primeiro item, o último e o total de itens da lista
# usando len().
# nomes = []

# for i in range(5):
#     nome = input(f"Digite o {i+1} nome: ")
#     nomes.append(nome)

# print(nomes[0])
# print(nomes[-1])

# print(len(nomes))


# 2. Fila de atendimento
# Uma clínica tem uma fila com os nomes: ["Carlos",
# "Beatriz", "Fábio", "Juliana", "Rafael"]. Adicione
# "Tatiane" ao final da fila e remova "Fábio" porque ele
# desistiu. Exiba a fila atualizada e o total de pessoas.

fila_atendimento = ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]

fila_atendimento.append("Tatiane")
fila_atendimento.pop(2)

numero = 1
for p in fila_atendimento:
    print(f"{numero}. {p}")
    1
    numero += 1
print(f"Total: {len(fila_atendimento)}")