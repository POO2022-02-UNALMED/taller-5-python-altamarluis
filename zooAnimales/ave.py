
from zooAnimales.animal import Animal


class Ave(Animal):
    _listado = None
    halcones, aguilas = 0,0

    def __init__(self, n=None, e=0, h=None, g=None, c = None):
        super().__init__(n, e, h, g)
        self._colorPlumas = c
        if Ave._listado == None:
            Ave._listado = []
        Ave._listado.append(self)
        Animal.totalAnimales("ave")

    @classmethod
    def crearHalcon(cls,n,e,g):
        cls.halcones += 1
        return Ave(n,e,"montanas",g,"cafe glorioso")

    @classmethod
    def crearAguila(cls,n,e,g):
        cls.aguilas += 1
        return Ave(n,e,"montanas",g,"blanco y amarillo")

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def movimiento(self):
        return "volar"

    def getColorPlumas(self):
        return self._colorPlumas

    def getListado(self):
        return Ave._listado

    def setColorPlumas(self,i):
        self._colorPlumas = i


