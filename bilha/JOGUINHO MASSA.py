import random
numeros = random.randint(0,51)

print('BEM-VINDO AO JOGO DE ADIVINHAÇÃO DO SÉCULO!')
print('PARA JOGAR, DIGITE UM NÚMERO. CUIDADO, VOCÊ SÓ TEM 10 TENTATIVAS.')
count = 0
while (count < 9):
  x = int(input())
  count += 1 
  if x > numeros:
    print("O número digitado é maior que o número sorteado")

  elif x < numeros:
    print("O número digitado é menor que o número sorteado")

  if count > 10:
    break

  if x == numeros:
    print('Parabéns, você acertou!')
    break

else: 
  x != numeros
  print('Não foi dessa vez, tente novamente!')


