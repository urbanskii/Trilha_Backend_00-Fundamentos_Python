###### Estrutura de Repetição
###### Exercicio 07 da lista python brasil


maximo = float(input('Digito um número: '))

for _ in range(4):
    maximo = max(maximo, float(input('Digito um número: ')))
    print(f'Número máximo encontrado até agora é: {maximo}')

    