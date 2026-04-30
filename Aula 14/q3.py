
soma = 0
while True:
    numero = int(input("Digite um número: "))

    if numero == -1:
        break
    soma += numero


print(f"A soma dos numeros foi: {soma}")