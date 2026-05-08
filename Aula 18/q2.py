# 5. Verificação de estoque
# Um mercadinho tem a lista estoque = ["arroz", "feijão",
# "macarrão", "leite", "óleo"]. Peça ao usuário um produto com input()
# e informe se ele está ou não disponível no estoque. Depois, exiba o
# estoque em ordem alfabética usando sorted().

# lista_mercado =["arroz", "feijão", "macarrão", "leite", "óleo"]



# 6. Controle de presença
# Uma turma tem 6 alunos. Use um for com enumerate() para percorrer a
# lista de nomes e perguntar ao ,usuário "presente" ou "ausente" para cada
# um. Ao final, exiba quantos alunos estiveram presentes e quantos faltaram

turma = []
while True:
    aluno = input(f"Digite o nome do aluno N {len(turma)+1}: ")

    if aluno == "" or len(turma) >= 3:
        break

    turma.append(aluno)

    resp = input("Quer continuar? (S/N): ")

    if resp in ["N", "Não", "No"]:
        break

    qtd_ausentes = 0
    qtd_presente = 0

    for aluno in turma:
        print(f"Registro de frequencia do aluno {aluno}")
        frequencia = input("Digite o estado do aluno (presente/ Ausente): ")

        if frequencia == "presente":
            qtd_presente += 1
        


        
# len aluno - qtd presentes
        print(f"presentes: {qtd_presente}")
        print(f"Ausentes: " ({aluno} - qtd_presente))

# 7. Placar de campeonato
# Duas listas paralelas armazenam os times e seus pontos:
# times = ["Corinthians", "Palmeiras", "Santos", "São Paulo"]
# pontos = [58, 65, 42,51]
# Use for com enumerate() para exibir a tabela de classificação. Depois
# encontre e exiba o time com mais pontos (localizando o indice do valor
# máximo com .index(max( ... ))).

