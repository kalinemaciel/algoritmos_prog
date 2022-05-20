def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return False, False
    else:
        return (-b + delta ** 0.5)/(2*a), (-b - delta ** 0.5)/(2*a)
    
a, b, c = map(float, input().split())
x1, x2 = bhaskara(a, b, c)
print(f'x1 = {x1}; x2 = {x2}')