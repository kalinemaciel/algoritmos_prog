
#Kaline Maciel dos Santos (178295)

# ----------- AMPLITUDE TÉRMICA -----------

temperatura = []

for n in range(12):
    valor = float(input())
    temperatura.append(valor)

maior = max(temperatura)
menor = min(temperatura)
amplitude = maior - menor

print(f'{amplitude:.1f}')
