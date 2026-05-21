# Calculadora de 10%. Crie uma função que recebe o valorde uma conta, use
# o valor dessa conta para calcular a gorjeta(10%) e o valor final da conta
# (total + gorjeta) e imprima na tela uma nota fiscal do que o usuário terá
# que pagar.

# def calculadora_gorjeta_padrao(valor_conta):
#     gorjeta = valor_conta * 0.1
#     valor_final = valor_conta + gorjeta

#     print(f"""
# ======== NOTA FISCAL ========
# Valor da conta: R$ {valor_conta:,.2f}
# Gorjeta (10%): R$ {gorjeta:,.2f}

# TOTAL A PAGAR: R$ {valor_final:,.2f}

# """)
    
# calculadora_gorjeta_padrao(100)

# Calculadora de gorjeta. Crie uma função que recebe as informações valor da conta e porcentagem da gorjeta, a função deverá retornar o valor total a ser pago pelo cliente, imprima na tela.

# def calcular_gorjeta_personalizada(valor_conta=0, 
#                                    pct_gorj=0.1):
    
#     gorjeta = valor_conta * pct_gorj

#     valor_total = valor_conta + gorjeta

#     return valor_total 


# total_conta = calcular_gorjeta_personalizada(600, 0.2)

# print(f"total a pagar: {total_conta} ")

# if total_conta >= 500:
#     total_conta -= 50
#     print(f"Valor final da conta: {total_conta}")


# Crie uma função de calculadora. Essa função deve receber as informações num1, num2 e operação, essa função deverá retomar o resultado da operação escolhida. Imprima o resultado de 5 operações com essa ferramenta. P.S: Lembre de verificar divisões por 0 e forneça o resultado adequado.

def calcular(num1, num2, operacao): #case e match
    if operacao == "+":
        resultado = num1 + num2 
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:
            resultado = "ERRO: DIVISAO POR ZERO"
        else: 
            resultado = num1 / num2
        
        return resultado
    
print(f"""
RESULTADO 1:

""")