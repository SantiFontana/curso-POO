from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre  = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
    
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f"Estoy trabajando en el rubro de: {self.actividad}")


fontana = Estudiante("Santiago",20,"Masculino","programación")

pedro = Trabajador("Pedro",25,"Masculino","programación")


fontana.presentarse()
fontana.hacer_actividad()
pedro.presentarse()
pedro.hacer_actividad()
