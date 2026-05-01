while True:

    numero1 = float(input("insira o primeiro numero: "))
    numero2 = float(input("insira o segundo numero: "))

    print(f"""
    Escolha uma operação:
        1. (+)
        2. (-)
        3. (*) 
        4. (/) 

    """)

    operacao = input("Informe a operacao desejada: ")

    resultado = 0

    if operacao == "+":
        resultado = numero1 + numero2

    elif operacao == "-":
        resultado = numero1 - numero2

    elif operacao == "*":
        resultado = numero1 * numero2

    elif operacao == "/":
        if numero2 == 0:
            print("ERRO")
        resultado = numero1 / numero2
    else:
        print("Operacao invalida")


    print(f"Resultado = {resultado}")
    
    while True:
        resposta = input("Deseja continuar? (S/N)")

        if resposta == "N":
            print("encerrando o programa")
            break
        elif resposta == "S":
            break
        else:
            print("Digite novamente")
            continue

    if resposta == "N":
        break
    else:
        continue