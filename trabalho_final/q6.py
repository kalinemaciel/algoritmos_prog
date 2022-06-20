
#Kaline Maciel dos Santos (178295)

# ----------- CIDADES -----------

cidade = []
caracteres = []

while True:
    nome = str(input('Informe uma cidade: '))
    
    if (nome.upper() != 'FIM'):
        cidade.append(nome)
        caracteres.append(len(nome))
        
    else:
        break
    
nome = caracteres.index(max(caracteres))
print(f'A cidade com nome mais extenso é {cidade[nome]}, com {max(caracteres)} caracteres.')