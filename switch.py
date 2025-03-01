from microfone_off import Console
from microfone import Mic
from power import Power_on, Power_off
from commands import Server

server = Server()
class Switch:
    """Classe responsável por ligar e desligar o sistema."""
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.console = Console(bot_name)
        self.mic = Mic(bot_name)
        self.executavel = self.console
        self.estado_atual = Power_on()
        self.power = True

    def check_power(self):
        self.estado_atual.check_power(self)

    def ligar(self):
        self.estado_atual.ligar(self)

    def desligar(self):
        self.estado_atual.desligar(self)

    def abrir_console(self):
        self.executavel = self.console
        server.notification("Iniciando comando pelo teclado. .")

    def fechar_console(self):
        self.executavel = self.mic
        server.notification("Iniciando comando por voz. .")
