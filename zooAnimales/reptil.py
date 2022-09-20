
from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = None
    iguanas, serpientes = 0,0

    def __init__(self, n=None, e=0, h=None, g=None, c = None, l = 0):
        super().__init__(n, e, h, g)
        self._colorEscamas = c
        self._largoCola = l
        if Reptil._listado == None:
            Reptil._listado = []
        Reptil._listado.append(self)
        Animal.totalAnimales("reptil")

    @classmethod
    def crearIguana(cls,n,e,g):
        cls.iguanas += 1
        return Reptil(n,e,"humedal",g,"verde",3)

    @classmethod
    def crearSerpiente(cls,n,e,g):
        cls.serpientes += 1
        return Reptil(n,e,"jungla",g,"blanco", 1)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def movimiento(self):
        return "reptar"

    def getColorEscamas(self):
        return self._colorEscamas

    def getLargoCola(self):
        return self._largoCola

    def getListado(self):
        return Reptil._listado

    def setColorEscamas(self,i):
        self._colorEscamas = i

    def setLargoCola(self, l):
        self._largoCola = l
