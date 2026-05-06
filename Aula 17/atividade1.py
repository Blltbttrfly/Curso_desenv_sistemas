# # Crie um programa que recebe uma palavra. Imprima a última letra
# dessa palavra.
nome = input("Digite uma palavra: ")

print(nome[-1])

# # Crie um programa que recebe uma palavra. Informe se a palavra  começa com vogal ou consoante.

palavra = input("Digite uma palavra: ")

if palavra[0].lower() in "aeiou":
    print("Começa com vogal!")
else: 
    print("começa com consoante!")


# # Crie um programa que recebe uma palavra. Imprima todos os caracteres dessa palavra, linha por linha

palavra2 = input("digite uma palavra: ")

for i in range(len(palavra2)):
    print(palavra2[i])

palavra = "Jujuba"

texto_final = ""

for i in range(len(palavra)):
    if i == len(palavra)-1:
        texto_final += palavra[i]
    else:
        texto_final += palavra[i]

print(texto_final)


texto = "Senhor dos Aneis"
qtd_vogais = 0

for letra in texto:
    if letra in "aeiou":
        print(letra)
        qtd_vogais += 1

print(qtd_vogais)














