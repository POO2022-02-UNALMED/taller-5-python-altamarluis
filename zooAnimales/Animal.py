from typing_extensions import Self

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
        return "Mamiferos: ", cls._m, "\nAves: ", cls._av,  "\nReptiles: ", cls._r, "\nPeces: ", cls._p , "\nAnfibios: ",  cls._an

    def __str__(self):
        if Animal._zona == None:
            return "Mi nombre es ", self._nombre, ", tengo una edad de ", self._edad, ", habito en ", self._habitat, " y mi genero es ", self._genero
        else:
            return "Mi nombre es ", self._nombre, ", tengo una edad de ", self._edad, ", habito en ", self._habitat, " y mi genero es ", self._genero, ", la zona en la que me ubico es ", Animal._zona.getNombre(), ", en el ", Animal._zona.getZoo().getNombre()

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
        cls._zona.agregarAnimales(Self)

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

    