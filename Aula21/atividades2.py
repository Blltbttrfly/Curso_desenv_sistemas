# Crie uma agenda telefonica onde o telefone da pessoa deve ser acessado pelo seu nome. Você deve usar um dicionário onde a chave será o nome e o valor será o telefone. Peça para que a pessoa escreva um nome e mostre na tela o telefone da pessoa escolhida. Faça pelo menos 10 contatos.

agenda = {
    "Noelle": 1001,
    "Kris": 1002,
    "Berdly": 1003,
    "ralsei": 1004
}

nome = input("Digite o contato que deseja telefonar: ")

if nome in agenda:
    print(f"Telefone: {agenda[nome]}")
else:
    print("Nome não encontrado!")

# 1 - Peça para o usuário o nome e telefone de 5 novas pessoas e adicione na agenda.
while True: 
    adicionar = input("deseja adicionar um novo contato?: ")
    
    if adicionar.upper() == "SIM":
        
        novo_contato = input("Informe o nome do contato: ")
        
        numero_contato = int(input("Digite o telefone do contato: "))
        
        agenda.update({novo_contato:numero_contato})
    else:
        break

print(agenda)


# 2 - Utilize um loop while para permitir que a pessoa consulte os números da agenda. O usuário deverá escrever o nome de um dos contatos e o programa deve exibir o número na tela (caso exista, senão exibir mensagem de erro) e depois pedir o nome do próximo. Continue até que a pessoa escreva o nome "Sair".



# 3 - No começo de cada repetição, exiba a lista de contatos na tela.
