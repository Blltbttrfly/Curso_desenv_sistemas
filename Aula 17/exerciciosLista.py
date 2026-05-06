# Crie um programa que pede o nome de 10
# pessoas. Adicione cada nome em uma lista
# e ao final imprima a lista
# verticalmente. Ex:
#Maria
#João
#Zeca
#Mane1

lista_nomes = []

for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    lista_nomes.append(nome)

numero = 1
for n in lista_nomes:
    print(f"{numero}. {n}")
    numero += 1

print(lista_nomes)

# Crie um programa que recebe o valor de 5 prdutos. Ao final imprima o total da compra
# Crie um programa que recebe 8 notas e imprima na tela a média dessas notas. Ao final tambem exiba o boletim do aluno seguindo o formato 
# NOta 1 -7
