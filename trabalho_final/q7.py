
#Kaline Maciel dos Santos (178295)

# ----------- LISTA INVERTIDA -----------

print('Informe 10 valores:')

lista = []

for i in range(10):
    numero = float(input())
    lista.append(numero)
    
numeros_lista = lista[::-1]
cont = 0

for i in range(10):
    if (numeros_lista[i] < 0):
        cont = +1
        print(f'{numeros_lista[i]:.1f}')
    
if (cont == 0):
    print('Nenhum valor negativo')