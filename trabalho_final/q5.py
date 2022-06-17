
#Kaline Maciel dos Santos (178295)

# ----------- FUNÇÕES -----------

def operacao(op):
    if (op == '+'):
        descricao = 'soma'
    elif (op == '-'):
        descricao = 'subtração'
    elif (op == '*'):
        descricao = 'multiplicação'
    elif (op == '/'):
        descricao = 'divisão'
    return descricao

def calculadora(valor1, valor2, op):
    if (op == '+'):
        calcula = valor1 + valor2
    elif (op == '-'):
        calcula = valor1 - valor2
    elif (op == '*'):
        calcula = valor1 * valor2
    elif (op == '/'):
        calcula = valor1 / valor2
    return calcula

# ----------- OPERAÇÕES -----------

valor1    = int(input('Digite o primeiro valor: '))
valor2    = int(input('Digite o segundo valor: '))

op        = input('Qual operação? ')

descricao = operacao(op)
resultado = calculadora(valor1, valor2, op)

print(f'Resultado da operação de {descricao} entre {valor1} e {valor2} é {resultado}.')