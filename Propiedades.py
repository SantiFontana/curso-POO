class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre

fontana = Persona("Santiago",20)

nombre = fontana.nombre
print(nombre)

fontana.nombre = "Pepe"

nombre = fontana.nombre
print(nombre)

del fontana.nombre

nombre = fontana.nombre
print(nombre)

