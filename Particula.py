from Algoritmos import distancia_euclidiana

class Particulas:
    def __init__(self,Id=0, OrigenX=0, OrigenY=0, DestinoX=0, DestinoY=0, Velocidad=0, Red=0, Green=0, Blue=0):
        self.__Id = Id
        self.__OrigenX = OrigenX
        self.__OrigenY = OrigenY
        self.__DestinoX = DestinoX
        self.__DestinoY = DestinoY
        self.__Velocidad = Velocidad
        self.__Red = Red
        self.__Green = Green
        self.__Blue = Blue
        self.__Distancia = distancia_euclidiana(OrigenX, OrigenY, DestinoX, DestinoY)

    def __str__(self):
        return(
            'ID: ' + str(self.__Id) + '\n' + 
            'Origen en x: ' + str(self.__OrigenX) + '\n' + 
            'Origen en y: ' + str(self.__OrigenY) + '\n' + 
            'Destino en x: ' + str(self.__DestinoX) + '\n' + 
            'Destino en y: ' + str(self.__DestinoY) + '\n' + 
            'Velocidad: ' + str(self.__Velocidad) + '\n' + 
            'Red: ' + str(self.__Red) + '\n' + 
            'Green: ' + str(self.__Green) + '\n' + 
            'Blue: ' + str(self.__Blue) + '\n' +
            'Distancia: ' + str(self.__Distancia) + '\n' 
        )