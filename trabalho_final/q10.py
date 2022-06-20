
#Kaline Maciel dos Santos (178295)

# ----------- MÉDIA DOS NÚMEROS -----------

num  = []
soma = 0

print('Digite 0 para encerrar!')

while True:
    valor = float(input('Informe um valor: '))
    if (valor != 0):
        num.append(valor)
    else:
        break
    
for i in range(len(num)):
    soma += num[i]
    
media = soma / len(num)
print(f'Média: {media:.2f}')

print('Maiores que a média:')
for i in range(len(num)):
    if (num[i] > media):
        print(num[i])
