
class Zona:
    

    def __init__(self, n = None, z = None):
        self._nombre = n
        self._zoo = z
        self._animales = None

     
    def agregarAnimales(self,a):
        if self._animales == None:
            self._animales = []
        self._animales.append(a)

    def cantidadAnimales(self):
        return len(self._animales)

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
        
    
