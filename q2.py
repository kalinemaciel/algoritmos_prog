
#Kaline Maciel dos Santos (178295)

# ----------- EMPRÉSTIMO -----------

valor   = float(input('Valor do Imóvel: '))
salario = float(input('Salário: '))
anos    = int(input('Anos a pagar: '))

parcela = valor / (anos * 12)
porcentagem = 0.3 * salario

if parcela < porcentagem:
    print('Empréstimo aprovado.')
    print(f'Valor da prestação: R$ {parcela:.2f}')
else:
    print('Infelizmente você não pode obter o empréstimo.')