codigoNumeroValor = input().split()
a = int(codigoNumeroValor[0])
b = int(codigoNumeroValor[1])
c = float(codigoNumeroValor[2])

codigoNumeroValor2 = input().split()
d = int(codigoNumeroValor2[0])
e = int(codigoNumeroValor2[1])
f = float(codigoNumeroValor2[2])

valorTotal = (b * c) + (e * f)

print(f'VALOR A PAGAR: {valorTotal:.2f}')

