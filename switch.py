from microfone_off import Console
from microfone import Mic
from power import Power_on, Power_off
from server import Server
from config import Config

server = Server()

class Switch:
    """Classe responsável por ligar e desligar o sistema."""
    def __init__(self):
        self.bot_name = Config.BOT_NAME
        self.console = Console()
        self.mic = Mic()
        self.executavel = self.console
        self.estado_atual = Power_off()
        self.power = False

    def check_power(self):
        try:
            self.estado_atual.check_power(self)
        except Exception as e:
            print(f"Erro ao verificar o estado de energia: {e}")

    def ligar(self):
        try:
            self.estado_atual.ligar(self)
        except Exception as e:
            print (f"Erro ao ligar: {e}")

    def desligar(self):
        try:
            self.estado_atual.desligar(self)
        except Exception as e:
            print (f"Erro ao desligar:{e}")

    def abrir_console(self):
        try:
            self.executavel = self.console
            server.notification("Iniciando comando pelo teclado. .")
        except Exception as e:
            print (f"Erro ao abrir console: {e}")

    def fechar_console(self):
        try:
            self.executavel = self.mic
            server.notification("Iniciando comando por voz. .")
        except Exception as e:
            print (f"Erro ao fechar console: {e}")














