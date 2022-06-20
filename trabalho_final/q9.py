
#Kaline Maciel dos Santos (178295)

# ----------- PARES E IMPARES -----------

print('Informe 8 números inteiros:')

par = []
impar = []

for n in range(8):
    numeros = int(input())
    
    if (numeros % 2 == 0):
        par.append(numeros)
        
    else:
        impar.append(numeros)
        
if (len(par) != 0):
    print(f'{len(par)} pares:')
    for lista in par:
        print(lista)

if (len(impar) != 0):
    print(f'{len(impar)} ímpares:')
    for lista in impar:
        print(lista)