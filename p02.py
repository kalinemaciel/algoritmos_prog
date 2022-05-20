def ler_nota():
    nota = -1
    while nota not in range(0,11):
        nota = int(input())
        if nota not in range(0,11):
            print("Nota inválida")
        else:
            return nota

def mediasemestral(nota1, nota2, nota3):
    media = ((nota1*3.0)+(nota2*4.0)+(nota3*3.0))/10
    return media

def resultado(media):
    print(f'{media:.1f}')
    if media < 3.0:
        print("Aluno reprovado")
    elif media > 7.0:
        print("Aluno aprovado")
    else:
        print("Aluno em exame")
        falta = 7.0-media
        print(f'Falta {falta:.1f} para ser aprovado')


nota1 = ler_nota()
nota2 = ler_nota()
nota3 = ler_nota()

media = mediasemestral(nota1, nota2, nota3)
resultado(media)