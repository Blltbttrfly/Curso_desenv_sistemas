import random
#numeros_ganhadores = 0

#for i in range(6):
 #   numeros_ganhadores = random.randint(1,60)
  # num_inseridos = int(input(f"Digite o número {i+1}"))

bilhete = "" 
for i in range(6):
    num = random.randint(1,60)

    if i == 5:
        bilhete += f"{num}"
    else:
        bilhete += f"{num} - "

print(bilhete)

