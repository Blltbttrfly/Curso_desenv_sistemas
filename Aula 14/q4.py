maior = 0
menor = 0
while True:
    distancia = float(input("Digite quantos metros foram corridos: "))

    if distancia < 0:
        print("Digite um valor positivo para distância da corrida!")
        continue

    if distancia == 0:
        print("Encerrando cadastro de percursos!")
        break

    if distancia > maior:
        maior = distancia
    if distancia < menor:
        menor = distancia

print(f"O maior percurso foi: {maior}")