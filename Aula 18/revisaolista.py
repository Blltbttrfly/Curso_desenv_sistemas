perfil = [ "Shin", 30, False, ["Hiyori", "sara", "kanna"], "death game"]

print(perfil[-2]) 

perfil.append("Soushin")

perfil[1] = "naosara"

print(perfil.pop(2))

print(perfil)

#programa que recebe nome de 5 alnos e exibe em ordem alfabetica

nome = []
nomes = ""
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nomes.append(nome)
