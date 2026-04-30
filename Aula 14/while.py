qtd_funcionarios = 0

while True:
    nome_func = input("Digite o nome do funcionario: ")

    if nome_func.capitalize() in ["sair","Sair", "pronto"]:
        print("SAINDO DO CADASTRO DE FUNCIONARIOS")
        break
    
    qtd_funcionarios += 1

print(f"Funcionarios cadastrados {qtd_funcionarios}")