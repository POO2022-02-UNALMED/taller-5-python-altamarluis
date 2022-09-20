
from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = None
    ranas, salamandras = 0,0

    def __init__(self, n=None, e=0, h=None, g=None, c = None, v = False):
        super().__init__(n, e, h, g)
        self._colorPiel = c
        self._venenoso = v
        if Anfibio._listado == None:
            Anfibio._listado = []
        Anfibio._listado.append(self)
        Animal.totalAnimales("anfibio")

    @classmethod
    def crearRana(cls,n,e,g):
        cls.ranas += 1
        return Anfibio(n,e,"selva",g,"rojo",True)

    @classmethod
    def crearSalamandra(cls,n,e,g):
        cls.salamandras += 1
        return Anfibio(n,e,"selva",g,"negro y amarillo", False)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento(self):
        return "saltar"

    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso

    def getListado(self):
        return Anfibio._listado

    def setColorPiel(self,i):
        self._colorPiel = i

    def setVenenoso(self, l):
        self._venenoso = l
