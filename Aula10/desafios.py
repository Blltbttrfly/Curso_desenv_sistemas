numero1 = int(input("insira o primeiro numero"))
numero2 = int(input("insira o segundo numero"))
numero3 = int(input("insira o terceio numero"))

if numero1 <= numero2 and numero2 <= numero3:
    if numero2 <= numero3:
        print(numero1, numero2, numero3)
    else:
        print(numero1, numero3, numero2)
