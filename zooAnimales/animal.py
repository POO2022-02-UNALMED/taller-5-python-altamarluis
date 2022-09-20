


class Animal:
    _totalAnimales = 0
    _zona = None
    _m, _av, _r, _p, _an = 0,0,0,0,0

    def __init__(self, n = None, e = 0, h = None, g = None):
        self._nombre = n
        self._edad = e
        self._habitat = h
        self._genero = g

    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos : " + str(cls._m) + "\nAves : " + str(cls._av) +  "\nReptiles : " + str(cls._r) + "\nPeces : " + str(cls._p)  + "\nAnfibios : " +  str(cls._an)

    def toString(self):
        if Animal._zona == None:
            return "Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(self._edad) + ", habito en " + str(self._habitat) + " y mi genero es " + str(self._genero)
        else:
            return "Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(self._edad) + ", habito en " + str(self._habitat) + " y mi genero es " + str(self._genero) + ", la zona en la que me ubico es " + str(Animal._zona.getNombre()) + ", en el " + str(Animal._zona.getZoo().getNombre())

    def movimiento(self):
        return 'desplazarse'

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def getZona(self):
        return Animal._zona

    def getTotalAnimales(self):
        return Animal._totalAnimales

    def setNombre(self,n):
        self._nombre = n

    def setEdad(self, e):
        self._edad = e

    def setHabitat(self, h):
        self._habitat = h

    def setGenero(self, g):
        self._genero = g
    
    @classmethod
    def setZona(cls,z):
        cls._zona = z
        cls._zona.agregarAnimales(cls)

    @classmethod
    def totalAnimales(cls,t):
        cls._totalAnimales += 1
        if t == "mamifero":
            cls._m += 1
        elif t == "ave":
            cls._av += 1   
        elif t == "reptil":
            cls._r += 1
        elif t == "pez":
            cls._p += 1
        elif t == "anfibio":
            cls._an += 1

    
