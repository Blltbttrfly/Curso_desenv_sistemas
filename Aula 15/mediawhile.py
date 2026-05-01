soma_notas = 0
qtd_notas_validas = 0
soma_notas = 0
# Algoritmo de coletar notas
while True:

    nota = float(input("Digite uma nota entre 0 e 10:"))

    if nota < 0 or nota > 10:
        print("Nota Inválida ... Digite Novamente ... ")
    continue
    qtd_notas_validas += 1
    soma_notas += nota