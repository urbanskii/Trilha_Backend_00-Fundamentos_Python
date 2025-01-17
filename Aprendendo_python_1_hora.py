type(1)
print(type(1))
print(43%6)

print(43/6)

print(43//6)

print(type(7.16))

pi = 3.1415
raio = 1
print(pi * (raio ** 2))


print("Olá Mundo")

print(type('Renzo'), type("Renzo"), type("""Renzo"""), type('''Renzo'''))

nome = 'Renzo \n Nuccitelli'
print(nome)


nome = '''Renzo
    Nuccitelli'''

print(nome)


print(type(True), type(False))

print(not(True))

print(not(False))

print(True and False)
print(True and True)
print(False and False)

print(True or False)
print(True or True)
print(False or False)

print(5 < 6)

print(5 <= 6)

print(5 == 6)

print(5 > 6)
print(5 != 6)
print( 5 and 6)



### Desvios logicos:

idade = 17

if idade < 18:
    print(f'menor de idade: {idade}')
    print('Acabou o if')
elif idade >= 65:
    print(f'pessoa idosa: {idade}')
else:
    print(f'maior de idade: (idade)')
    


## Funções

def classificar(idade, nome):
    
    if idade < 18:
        return f'{nome} é menor de idade: {idade}'
    elif idade >= 65:
        return f' {nome} é um idoso(a): {idade}'
    else:
        return f' {nome} é maior de idade: {idade}'

print(classificar(17, "João"))
print(classificar(21, "Carla"))
print(classificar(68, "Pedro"))


## Sequencias

lista = [1, 4.5, True, []]
print(type(lista), lista)

## Acesso aos elementos

print(lista[0])
print(lista[1])

print(len(lista))

## Fatiamento

print(lista[0:3])


print(lista[:4])
print(lista[-2])
print(lista)
