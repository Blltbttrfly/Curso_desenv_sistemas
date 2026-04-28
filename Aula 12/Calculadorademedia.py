nota = 0
soma_notas = 0
contador_notas = 0
qtd_notas = int(input("Digite quantas notas serão registradas: "))
boletim = ""

for i in range(qtd_notas):
    nota = float(input(f"Insira nota {i+1}: "))
    if nota >= 0 and nota <= 10:
        soma_notas += nota
        contador_notas += 1
        boletim += f"Nota {contador_notas}: {nota} "
    else:
        print("nota inválida")

media = soma_notas/contador_notas

if media >= 6 and media <= 10:
    print("Situação: Aprovado!")
elif media >= 4 and media < 6:
    print("Situação: Recuperação!")
elif media < 4:
    print("Situação: Reprovado!")

print(boletim)

