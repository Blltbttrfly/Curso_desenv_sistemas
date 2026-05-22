def q1_cabecalho(titulo):
    #espaco = int((40-len(titulo))/2) 
    print("-"*40)
    print(titulo.center(40))
    print("-"*40)

q1_cabecalho("CADASTRO DE FUNCIONÁRIOS")


def q8_media_notas(n1,n2,n3,n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

def q8_verificar_situacao_aluno(nome, n1,n2,n3,n4):
    media = q8