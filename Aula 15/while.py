idade = 0
while idade < 18:
    idade = int(input("digite sua idade: "))

    if idade < 18:
        print("voce é menor de idade, digite sua idade novamente.")

    else:
        break

print("Voce saiu do loop pois é maior de idade.")

