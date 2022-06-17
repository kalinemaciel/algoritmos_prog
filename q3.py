
#Kaline Maciel dos Santos (178295)

# ----------- STRINGS -----------

frase = input('1ª string: ')
palavra = input('2ª string: ')

if frase.count(palavra) != 0:
    print(f'{palavra} encontrado {} na posição de {frase}')
else:
    print(f'{palavra} não encontrado em {frase}')
