def imprimir_triangulo_de_numeros_crescentes(n: int):
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end = '   ')
        print('')

print('Triangulo com 1 ')
imprimir_triangulo_de_numeros_crescentes(1)

print('Triangulo com 2 ')
imprimir_triangulo_de_numeros_crescentes(2)

print('Triangulo com 3 ')
imprimir_triangulo_de_numeros_crescentes(3)
