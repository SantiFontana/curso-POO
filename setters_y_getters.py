class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre


fontana = Persona("Santiago",20)

nombre = fontana.get_nombre()
print(nombre)

fontana.set_nombre("Pepito")

nombre = fontana.get_nombre()
print(nombre)