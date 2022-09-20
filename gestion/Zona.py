
class Zona:
    _animales = None

    def __init__(self, n = None, z = None):
        self._nombre = n
        self._zoo = z

    def agregarAnimales(self,a):
        if Zona._animales == None:
            Zona._animales = []
        Zona._animales.append(a)

    def cantidadAnimales(self):
        return len(Zona._animales)

    def getZoo(self):
        return self._zoo

    def getNombre(self):
        return self._nombre

    def getAnimales(self):
        return Zona._animales

    def setNombre(self, n):
        self._nombre = n

    def setZoo(self,z):
        self._zoo = z
        
    