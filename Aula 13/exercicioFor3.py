#receba 5 numeros e printe o maior deles
maior = None
menor = 0
for i in range(5):
    num = float(input("Digite um numero: "))

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f"O maior número: {maior}")