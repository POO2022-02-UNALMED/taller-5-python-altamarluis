from typing_extensions import Self
from zooAnimales.Animal import Animal

class Mamifero(Animal):
    _listado = None
    caballos, leones = 0,0

    def __init__(self, n=None, e=0, h=None, g=None, p = False, pa = 0):
        super().__init__(n, e, h, g)
        self._pelaje = p
        self._patas = pa
        if Mamifero._listado == None:
            Mamifero._listado = []
        Mamifero._listado.append(Self)
        Animal.totalAnimales("mamifero")

    @classmethod
    def crearCaballo(cls,n,e,g):
        cls.caballos += 1
        return Mamifero.__init__(n,e,"pradera",g,True,4)

    @classmethod
    def crearLeon(cls,n,e,g):
        cls.leones += 1
        return Mamifero.__init__(n,e,"selva",g,True,4)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    def isPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas

    def getListado(self):
        return Mamifero._listado

    def setPelaje(self,i):
        self._pelaje = i

    def setPatas(self, l):
        self._patas = l