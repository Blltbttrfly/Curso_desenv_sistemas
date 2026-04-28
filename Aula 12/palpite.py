import random 
numero_secreto = random.randint(0,10) 
tentativas = 3

for i in range(3):
    print(f"Voce tem {tentativas} tentativas!")
    palpite = int(input("DIgite seu palpite de 0 a 10: "))
    tentativas -= 1

    if palpite == numero_secreto:
        print("Acertou!")
        break
    else:  # o elif poderia caber aqui tbm
        if tentativas == 0:
            print("Voce não tem mais tentativas")
        else:
            print("Errou!")
