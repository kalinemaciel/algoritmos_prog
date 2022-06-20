
#Kaline Maciel dos Santos (178295)

# ----------- DIVISÃO -----------

lista = []
n     = int(input('Informe um número inteiro:'))

for i in range(n):
    valor = float(input('Informe um valor: '))
    lista.append(valor)
    
minimo = min(lista)

for i in range(len(lista)):
    if (minimo != 0):
        divisao = lista[i] / minimo
        print(f'{divisao:.1f}')
    else:
        print(f'{lista[i]:.1f}')
