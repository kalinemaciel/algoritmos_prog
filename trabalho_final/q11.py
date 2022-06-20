
#Kaline Maciel dos Santos (178295)

# ----------- SUBSTITUIÇÃO -----------

def substix2(num):
    for i in range (len(num)):
        if (num[i] % 2 != 0):
            num[i] += num[i]
        return num

print('Digite 0 para encerrar!')
num = []

while True:
    valor = int(input('Informe um valor: '))
    if (valor != 0):
        num.append(valor)
    else:
        break
    
n_num = substix2(num)
for i in range (len(n_num)):
    print(n_num[i])