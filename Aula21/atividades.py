
nome = input("Digite o nome do animal: ") 
especie = input("Digite qual o animal: ")
idade = int(input("Digite a idade do animal: "))
peso = float(input("Digite o peso so animal: "))


animal = {
    "Nome": nome,
    "Espécie": especie,
    "Idade": idade,
    "Peso": peso,
    }

print(f"""
----Ficha do animal----
    Nome: {animal['Nome']}
    Espécie: {animal['Espécie']}
    Idade: {animal['Idade']}
    Peso: {animal['Peso']}
      """)



