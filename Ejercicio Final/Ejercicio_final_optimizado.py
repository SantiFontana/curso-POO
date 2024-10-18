from textblob import TextBlob

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos
    
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")

# Definir los rangos de polaridad
rangos = [
    ((-1.0, -0.6), Sentimiento("muy negativo", "31")),
    ((-0.6, -0.3), Sentimiento("negativo", "31")),
    ((-0.3, -0.1), Sentimiento("algo negativo", "31")),
    ((-0.1, 0.1), Sentimiento("neutral", "33")),
    ((0.1, 0.4), Sentimiento("algo positivo", "32")),
    ((0.4, 0.9), Sentimiento("positivo", "32")),
    ((0.9, 1.0), Sentimiento("muy positivo", "32")),
]

analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input("\x1b[1;32m" + "\nDecime algo" + "\x1b[0;37m")
    
    blob = TextBlob(user_prompt)
    polaridad = blob.sentiment.polarity  
    
    sentimiento = analizador.analizar_sentimiento(polaridad)
    
    print(sentimiento)
    
