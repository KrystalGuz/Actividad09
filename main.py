from Particula import Particulas

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, Particula:Particulas):
        self.__particulas.append(Particula)

    def agregar_inicio(self, Particula:Particulas):
        self.__particulas.insert(0, Particula)
    
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

p01 = Particulas(1, 434, 453, 323, 123, 45, 255, 132, 34)
p02 = Particulas(2, 100, 22, 12, 345, 15, 65, 89, 98)
p03 = Particulas(3, 432, 342, 345, 32, 34, 12, 57, 48)
p04 = Particulas(4, 233, 54, 55, 156, 65, 90, 23, 44)
administrador = Administrador()

administrador.agregar_final(p01)
administrador.agregar_final(p02)
administrador.agregar_inicio(p03)
administrador.agregar_final(p04)
administrador.mostrar()