qtd_notas_validas = 0 

while qtd_notas_validas < 4:

    nota = float(input("Digite uma nota entre 0 e 10:"))

    if nota < 0 or nota < 10:
        print("Nota inválida...")
        print("Digite novamente...")
    else: 
        qtd_notas_validas += 1
        soma_notas += nota

media = soma_notas/qtd_notas_validas

print("")