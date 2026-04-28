soma = 0 
contador = 0 

for i in range(0,1001):
    if i % 2 == 0: #soma de todos os numeors pares de 1 a 1000
        soma += i 
        contador += 1
        print(i)

print(f"{soma}")

