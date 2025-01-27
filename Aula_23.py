class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.circuferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor
    
    def trocaCor(self, cor):
        self.cor = cor

circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()
circulo_segundo.trocaCor('Amarelo')
print(type(circulo_primeiro))
print(circulo_primeiro is circulo_segundo)
print(id(circulo_primeiro), circulo_primeiro.mostra_cor())
print(id(circulo_segundo), circulo_segundo.mostra_cor())

print(circulo_primeiro.cor, circulo_segundo.cor)

