soma = 0
contador_par = 0
contador_impar = 0

for i in range(0, 10):
    num = int(input(f"digite o número {i+1}: "))
    soma += num

    if num < 0:
        print("Numro invalido!")
    elif num % 2 == 0:
        contador_par += 1
    else:
        contador_impar = 1
        
print(f"A soma dos numeros é:{soma}")

    
