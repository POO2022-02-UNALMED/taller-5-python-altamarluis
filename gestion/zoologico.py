
class Zoologico:
    _zonas = None

    def __init__(self, n = None, u = None):
        self._nombre = n
        self._ubicacion = u
        
    def agregarZonas(self,z):
        if Zoologico._zonas == None:
            Zoologico._zonas = []
        Zoologico._zonas.append(z)

    def cantidadTotalAnimales(self):
        s = 0
        if Zoologico._zonas != None:
            for z in Zoologico._zonas:
                s += z.cantidadAnimales()
        return s
    
    def getNombre(self):
        return self._nombre

    def getUbicacion(self):
        return self._ubicacion

    def getZona(self):
        return Zoologico._zonas

    def setUbicacion(self, u):
        self._ubicacion = u
