saque = int(input('Digite o valor para saque: '))

notas_de_100 = notas_de_50 = notas_de_10 = notas_de_1 = 0

notas_de_100, saque = divmod(saque, 100)

notas_de_50, saque = divmod(saque, 50)

notas_de_10, saque = divmod(saque, 10)

notas_de_5, notas_de_1 = divmod(saque, 5)

if notas_de_100 > 0:
    print(f'{notas_de_100} nota(s) de 100')
if notas_de_50 > 0:
    print(f'{notas_de_50} notas(s) de 50')
if notas_de_10 > 0:
    print(f'{notas_de_10} notas(s) de 10')
if notas_de_5 > 0:
    print(f'{notas_de_5} nota(s) de 5')
if notas_de_1 > 0:
    print(f'{notas_de_1} notas(s) de 1')