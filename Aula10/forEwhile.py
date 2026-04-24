nome_repeticao = input("Informe a palavra que voce quer repetir:")
numero_repeticao = int(input("Informe quantas vezes voce quer repetir a frase 'hello (nome)':"))


for i in range(numero_repeticao): # o i é de iterador
    print(f"hello {nome_repeticao}")




for i in range(5): # o i é de iterador e serve como variavel
    nome_repeticao = input("Informe a palavra que voce quer repetir:")
    
    print(f"Hello {nome_repeticao}")
print(nome_repeticao)

for i in range(10):
    print(i)
