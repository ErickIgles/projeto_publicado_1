"""
Calculadora - básica de quatro operações
"""
# Amostra de cabeçalho do programa. 
print(f"{'CALCULADOR - BÁSICA':-^40}")
print('''[1] ADIÇÃO
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO''')
print(f"{'-':-^40}")
op = int(input('Informe a opção')) # Escolha de opção relacionada ao cabeçalho. 

print(f"{'-':-^40}")

# Corpo do programa. 
if op == 1:
    print('ADIÇÃO')
    num1 = float(input('Digite o 1 número:'))
    num2 = float(input('Digite o 2 número:'))
    soma = num1 + num2
    print(f'{num1} + {num2} = {soma}')
elif op == 2:
    print('SUBTRAÇÃO')
    num1 = float(input('Digite o 1 número:'))
    num2 = float(input('Digite o 2 número:'))
    subtracao = num1 - num2
    print(f'{num1} - {num2} = {subtracao}')
elif op == 3:
    print('MULTIPLICAÇÃO')
    num1 = float(input('Digite o 1 número:'))
    num2 = float(input('Digite o 2 número:'))
    multiplicacao = num1 * num2 
    print(f'{num1} x {num2} = {multiplicacao}')
elif op == 4:
    print('DIVISÃO')
    num1 = float(input('Digite o 1 número:'))
    num2 = float(input('Digite o 2 número:'))
    if num2 == 0:
        print('Não é possível dividir por zero.')
    else: 
        divisao = num1 / num2
        print(f'{num1} / {num2} = {divisao}')
print(f"{'FIM DO PROGRAMA':-^40}") # FInalização do programa. 
