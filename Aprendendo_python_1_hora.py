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

print(lista[:])


numeros = list(range(1, 11) )
print(numeros, numeros[1: 7: 2])

numeros2 = list(range(1, 32, 2))
print(numeros2)

## Adição e Remoção

print(dir (numeros))

###

"""
['__add__', 
 '__class__', 
 '__class_getitem__', 
 '__contains__', 
 '__delattr__', 
 '__delitem__', 
 '__dir__',  
 '__doc__',
 '__eq__', 
 '__format__', 
 '__ge__', 
 '__getattribute__', 
 '__getitem__', 
 '__gt__', 
 '__hash__', 
 '__iadd__', 
 '__imul__', 
 '__init__', 
 '__init_subclass__', 
 '__iter__', 
 '__le__', 
 '__len__', 
 '__lt__', 
 '__mul__', 
 '__ne__', 
 '__new__', 
 '__reduce__', 
 '__reduce_ex__', 
 '__repr__', 
 '__reversed__', 
 '__rmul__', 
 '__setattr__', 
 '__setitem__', 
 '__sizeof__', 
 '__str__', 
 '__subclasshook__', 
 'append', 
 'clear', 
 'copy', 
 'count', 
 'extend', 
 'index', 
 'insert', 
 'pop', 
 'remove', 
 'reverse', 
 'sort']
"""

###

##print(help(numeros.pop))
print(numeros.pop())
print(numeros)
print(numeros.append(10))
print(numeros)

### Laços de Repetição

idades = [17, 38, 70]
print(classificar(idades[0], 'Renzo'))

for idade in idades:
    print(classificar(idade, 'Pessoa'))

## Dicionario

linguas = {'pt': 'Portugues', 'en': 'Inglês'}
print(linguas['pt'], linguas['en'])


linguas['es'] = 'Espanhol'

print(linguas)

for chave in linguas.keys():
    print(chave)

for chave in linguas.values():
    print(chave)

for chave, valor in linguas.items():
    print(chave, valor)
