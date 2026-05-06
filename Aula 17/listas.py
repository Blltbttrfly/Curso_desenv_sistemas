# frutas = ["maçã", "Pera", "uva", "abacate", "abacaxi"] 
#CRUD
#Create - Inserir
#Read - Ler/Acessar
#Update - Alterar
#Delete - Remover

# print(len(frutas))

# print(frutas[-1])

# print(frutas[3])

# print("--------Lista de animais-------")

animais = ["Veado", "baleia", "homem", "cágado", "cabra"]

animais.append("Dragão") 

animais += ["Enguia", "Peixe", "Cachorro"]

# Remova um animal da lista

# animais.pop()
# animais.remove("Cavalo")|

# Substituir valor
animais[2] = "Galinha"

print(animais)

print("----- LISTA DE PESSOAS ------")
pessoa = ["Michael", 35, 1.75, True]

print(f"""

DADOS PESSOAIS:
Nome: {pessoa[0]}
Idade: {pessoa[1]}
Altura: {pessoa[2]}
Conta paga: {pessoa[3]}

""")

print("----- LISTA DE NUMEROS ------")
numeros = [10, 50, 30, 25, 13]

soma = 0
maior_numero = max(numeros)
menor_numero = min(numeros)
sum(numeros)/len(numeros)

for num in numeros:
    print(num)