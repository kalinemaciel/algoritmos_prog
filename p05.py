def testatriangulo(a, b, c):
    if a<0 or b<0 or c<0:
        return 0
    greater = 0
    smaller = 0
    temp = 0
    if a>b:
        greater = a
        smaller = b
        temp = c
    else:
        greater = b
        smaller = a
        temp = c

    if c>greater:
        temp = greater
        greater = c

    if greater<temp+smaller:
        if a == b and b == c:
            return 1
        if a == b or a == c or b == c:
            return 2

        return 3
    else:
        return 0

a = float(input())
b = float(input())
c = float(input())

tabela = ['Não é possível formar um triângulo',
          'Triângulo Equilátero',
          'Triângulo Isóceles',
          'Triângulo Escaleno']

print(tabela[testatriangulo(a, b, c)])