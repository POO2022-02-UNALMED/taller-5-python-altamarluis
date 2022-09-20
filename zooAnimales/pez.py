
from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = None
    salmones, bacalaos = 0,0

    def __init__(self, n=None, e=0, h=None, g=None, c = None, l = 0):
        super().__init__(n, e, h, g)
        self._colorEscamas = c
        self._cantidadAletas = l
        if Pez._listado == None:
            Pez._listado = []
        Pez._listado.append(self)
        Animal.totalAnimales("pez")

    @classmethod
    def crearSalmon(cls,n,e,g):
        cls.salmones += 1
        return Pez(n,e,"oceano",g,"rojo",6)

    @classmethod
    def crearBacalao(cls,n,e,g):
        cls.bacalaos += 1
        return Pez(n,e,"oceano",g,"gris", 6)

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    def movimiento(self):
        return "nadar"

    def getColorEscamas(self):
        return self._colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def getListado(self):
        return Pez._listado

    def setColorEscamas(self,i):
        self._colorEscamas = i

    def setCantidadAletas(self, l):
        self._cantidadAletas = l
