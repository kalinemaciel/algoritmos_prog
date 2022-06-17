
#Kaline Maciel dos Santos (178295)

# ----------- STRINGS -----------

string1 = input('1ª string: ')
string2 = input('2ª string: ')

find    = string1.find(string2)

if string2 in string1:
    print(f'{string2} encontrado na posição {find} de {string1}')
else:
    print(f'{string2} não encontrado em {string1}')