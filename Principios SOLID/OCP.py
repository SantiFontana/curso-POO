class Notificador:
    def __init__(self,usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")
        
class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviando Whatsapp a {self.usuario.whatsapp}")
        
class NotificadorTwitter(Notificador):
    def Notificar(self):
        print(f"Enviando tweet a {self.usuario.twitter}")