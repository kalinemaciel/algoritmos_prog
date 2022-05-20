nomeVendedor = input()
salarioFixo = float(input())
totalDeVendas = float(input())

comissao = salarioFixo + (totalDeVendas*0.15)


print(f'TOTAL = R${comissao:.2f}')
