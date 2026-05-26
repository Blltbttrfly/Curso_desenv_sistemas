# def nome_funcao (parâmetros):
#     #bloco de codigo

# def veificar_idade(idade):
#     # verificar se e maior que 18
#     # verificar se é numerico
#     return

#se for possivel nao use variaves globais
cadastrarFuncionario = []
funcionarios = []
def ver_funcionarios():
    print
while True:


    print(f"""
BEM VINDO AO SISTEMA RH XYZ

Menu:

        1. adastrar Funcionário
        2. Ver Funcionários
        3. Alterar Funcionário
        4. Remover Funcionário

        0. Sair
          """)
    
    op = input("Digite a opção desejada:")

    if op == "1":
        cadastrar_Funcionario()
    elif op == "2":
        ver_funcionarios()
    elif op == "3":
        pass
    elif op == "4":
        # Mostrar a lista de funcionarios na tela 
        # pedir para o usuario digitar o numero do funcionario
        # validar se o numero que o usuario digitou é possivel
        # remover funcionario escolhido
         pass
    elif op == "0":
        print("SAINDO DO PROGRAMA ... ")
        break
    else: 
        print("Digite a opção novamente.")
    input("Tecle enter para continuar.")

# Criar uma funcao chamada ver_funcionarios() que exibe os funcionarios em uma lista numerada no formato {numero}. {nome} - {cpf}
    