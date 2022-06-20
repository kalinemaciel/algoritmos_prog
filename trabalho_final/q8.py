
#Kaline Maciel dos Santos (178295)

# ----------- ESFERA -----------

import math

raio = float(input('Informe o raio da esfera: '))

def volume_esfera(raio):
    volume = (4 * math.pi * (raio ** 3)) / 3
    return volume

print(f'Volume: {volume_esfera(raio):.2f}')