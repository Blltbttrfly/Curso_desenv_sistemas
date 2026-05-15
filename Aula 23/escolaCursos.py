
alunos = [
    {
        "Nome": "Carlos Henrique Souza",
        "Curso": "Engenharia de Software",
        "Turno": "Noturno",
        "Data de Início": "2024-02-15",
        "Situação": "Ativo"
    },
    {
        "Nome": "Mariana Oliveira Lima",
        "Curso": "Administração",
        "Turno": "Matutino",
        "Data de Início": "2023-08-01",
        "Situação": "Ativo"
    },
    {
        "Nome": "Fernanda Alves Rocha",
        "Curso": "Direito",
        "Turno": "Noturno",
        "Data de Início": "2022-02-10",
        "Situação": "Não Ativo"
    },
    {
        "Nome": "Lucas Martins Pereira",
        "Curso": "Ciência da Computação",
        "Turno": "Integral",
        "Data de Início": "2025-01-20",
        "Situação": "Ativo"
    },
    {
        "Nome": "Juliana Costa Mendes",
        "Curso": "Psicologia",
        "Turno": "Vespertino",
        "Data de Início": "2021-07-05",
        "Situação": "Não Ativo"
    }
]


# dados = {
#     "Nome":
#     "Curso":
#     "Turno":
#     "Data de inicio":
#     "Situação (Ativo/não ativo)":

# }

while True:

    print(f"""

--------------- GERENCIAMENTO CURSOS Escola DELAY ---------------
          
Menu de Opções:
          
          1. Cadastrar aluno
          2. Ver alunos
          3. Ver aluno Específico

          0. Sair
""")
    
    op = input("Digite o número da opção desejada: ")

    if op == "1":
        # Crie um sistema de cadastro onde o usuário preenche as informações do funcionário e na sequência armazena esse funcionário no sistema.
        #Informações do funcionário serão Nome, CPF, Cargo, Salário e Departamento
        #Valide se o cpf tem 11 caracteres
        print("CADASTRO DE ALUNO")

        nome = input("Digite o nome: ")

        curso = input("Digite o curso: ")
        turno = input("Digite o turno (manhã, tarde, noite): ")
        data = input("Digite a data de início: ")
        situacao = input("Digite a situação: ")

        novo_aluno = {
            "Nome": nome,
            "Curso": curso,
            "Turno": turno,
            "Data de início":data,
            "Situação": situacao
        }

        alunos.append(novo_aluno)

    elif op == "2":
        print("ALUNOS CADASTRADOS")
        contador = 1
        for aluno in alunos:
            print(f"{contador}. {aluno["Nome"]} - {aluno["Curso"]}")
            contador += 1


    elif op == "3":
        
        print("ALUNOS CADASTRADOS")
        contador = 1
        for aluno in alunos:
            print(f"{contador}. {aluno["Nome"]} - {aluno["CPF"]}")
            contador += 1

        numero = int(input("Digite o número do aluno desejado para ver mais informações: (0=Cancelar)"))

        if numero == 0:
            print("Cancelando operação...")
        else:
            aluno_escolhido = alunos[numero-1]

            print(f"""
FICHA DE ALUNOS:
                  
    Nome: {aluno_escolhido["Nome"]}
    CPF: {funcionario_escolhido["CPF"]}
    Cargo: {funcionario_escolhido["Cargo"]}
    Salário: R$ {funcionario_escolhido["Salário"]:,.2f}
    Departamento: {funcionario_escolhido["Departamento"]}

""")
    elif op == "0":
        print("ENCERRANDO PROGRAMA...")
        break
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA!")



    input("DIGITE ENTER PARA CONTINUAR")