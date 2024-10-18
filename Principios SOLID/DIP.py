# class Diccionario:
#     def verificar_palabra(self,palabra):
#         #Lógica para verificar palabras
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         #usamos el diccionario para corregir el texto
#         pass


from abc import ABC, abstractmethod

class VerificadorOrtográfico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass
    
class Diccionario(VerificadorOrtográfico):
    def verificar_palabra(self, palabra):
    #Lógica para verificar si las palabras estan en el diccionario
        palabras_validas = {"hola", "mundo", "python", "corrector", "texto"}
        return palabra.lower() in palabras_validas

class CorrectorOrtográfico:
    def __init__(self,verificador):
        self.verificador = verificador
        
    def corregir_texto(self,texto):
        # usamos el verificador para corregir texto
        palabras = texto.split()
        texto_corregido = []
        for palabra in palabras:
            if self.verificador.verificar_palabra(palabra):
                texto_corregido.append(palabra)
            else:
                texto_corregido.append(f"*{palabra}*")  # Palabras no encontradas se marcan con '*'
        # Unimos las palabras corregidas en un texto final
        return " ".join(texto_corregido)

corrector = CorrectorOrtográfico(Diccionario())

texto = "Hola mundo programacion en Python"
texto_corregido = corrector.corregir_texto(texto)

print(texto_corregido)