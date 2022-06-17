
#Kaline Maciel dos Santos (178295)

# ----------- TABUADA -----------

n      = int(input('Tabuada de: '))
inicio = int(input('De: '))
fim    = int(input('Até: '))

for i in range(inicio, fim+1):
    print(f'{n} x {i} = {n*i} ')