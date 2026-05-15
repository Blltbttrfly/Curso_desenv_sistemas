# Crie um Sistema de Gerenciamento de RH.
# Criar um sistema que permita a um usuário
# cadastrar novos funcionários, ver uma lista de
# funcionários e ver as informações de um
# funcionário específico.

funcionarios = [
    {
        "Nome": "Carlos Henrique Souza",
        "CPF": "123.456.789-01",
        "Cargo": "Analista Financeiro",
        "Salário": 4500.00,
        "Idade": 32
    },
    {
        "Nome": "Mariana Oliveira Lima",
        "CPF": "234.567.890-12",
        "Cargo": "Desenvolvedora Backend",
        "Salário": 7800.00,
        "Idade": 28
    },
    {
        "Nome": "Fernanda Alves Rocha",
        "CPF": "345.678.901-23",
        "Cargo": "Gerente de Projetos",
        "Salário": 9200.00,
        "Idade": 41
    },
    {
        "Nome": "Lucas Martins Pereira",
        "CPF": "456.789.012-34",
        "Cargo": "Designer UX/UI",
        "Salário": 5600.00,
        "Idade": 26
    },
    {
        "Nome": "Juliana Costa Mendes",
        "CPF": "567.890.123-45",
        "Cargo": "Assistente Administrativo",
        "Salário": 3200.00,
        "Idade": 24
    }
]
contador = 0

while True:
    print("""
        |      MENU        |
        | 1 - Cadastrar    |
        |  funcionário     |
        | 2 - Ver          |
        |  funcionários    |
        | 3 - Ver detalhes |
        |  de funcionário  |
        | 0 - Sair         |
          
          """)
    acao = input("Selecione o número da ação desejada: ")


    if acao == "1":
        print("-----CADASTRO DE FUNCIONARIOS-----")
        
        nome_novo = input("Nome do funcionário: ")
            
        while True:    
            cpf_novo = input("CPF do funcionário (11 caracteres): ")

            # try:
            #     cpf_novo = int(cpf_novo)

            # except:
            #     print("Caracteres não numéricos detectados!")

            if len(cpf_novo) != 11 or not cpf_novo.isdigit():
                print("CPF INVALIDO.")
            else:
                break

        cargo_novo = input("Cargo do funcionário: ")
        salario_novo = float(input("Salário do funcionário: "))
        idade_novo = int(input("Idade do funcionário: "))

        funcionario_novo = {
             "Nome": nome_novo,
             "CPF": cpf_novo,
             "Cargo": cargo_novo,
             "Salário": salario_novo,
             "Idade": idade_novo

        }

        funcionarios.append(funcionario_novo)

    elif acao == "2":
        print("-----VISUALIZAR FUNCIONARIOS-----")
        contador = 1
        for funcionario in (funcionarios):
            print(f"{contador}. {funcionario["Nome"]} - {funcionario["CPF"]}")
            contador += 1


    elif acao == "3":
        print("-----ESCOLHA UM FUNCIONÁRIO-----")
        numero = int(input("Digite o número do funcionário desejado para ver mais informações: (0=Cancelar)"))

        if numero == 0:
            print("Cancelando operação...")
        else:
            funcionario_escolhido = funcionarios[numero-1]

        print(f"""
            FICHA DE FUNCIONÁRIO:
                  
    Nome: {funcionario_escolhido["Nome"]}
    CPF: {funcionario_escolhido["CPF"]}
    Cargo: {funcionario_escolhido["Cargo"]}
    Salário: R$ {funcionario_escolhido["Salário"]:,.2f}
    Departamento: {funcionario_escolhido["Departamento"]}

""")




    elif acao == "0":
        print("-----ENCERRANDO PROGRAMA-----")
        break
    else:
        print("Digite enter")

    input("Digite enter para continuar.")







