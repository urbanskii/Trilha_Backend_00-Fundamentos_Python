soma = float(input('Digito um número: '))

for n in range(2, 6):
    soma += float(input('Digito um número: '))
    media = soma / n
    print(f'A soma dos números é {soma}, e a média é {media}')
    