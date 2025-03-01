from commands      import Server
from gatilho       import Audio, Datahora

audio = Audio()
dh = Datahora()
server   = Server()

class Power_on:
    '''se sistema se encontra ligado, identifica a voz'''
    def check_power(self, Switch):
        voz = Switch.executavel.power(Switch.power)
        cmd_voz = ['sleep', 'dormir']
        for cmd_voz_check in cmd_voz:
            if voz == cmd_voz_check:return self.desligar(Switch)
        if voz == "fechar console": Switch.fechar_console()
        elif voz == "abrir console": Switch.abrir_console()

    def ligar(self, Switch):
        server.notification ("Programa já em andamento")

    def desligar(self, Switch):
        Switch.estado_atual = Power_off()
        Switch.power = False
        server.notification ("Turning Off")
        audio.toca_randomic_audio("go_to_sleep_", 4)

class Power_off:
    '''se sistema se encontra desligado, identifica a voz'''
    def check_power(self, Switch):
        command = Switch.executavel.power(Switch.power)
        if command == "fechar console": Switch.fechar_console()
        elif command == "abrir console": Switch.abrir_console()
        elif command == True: self.ligar(Switch)

    def ligar(self, Switch):
        Switch.estado_atual = Power_on()
        Switch.power = True
        audio.toca_randomic_audio("turn_on_", 5)
        server.notification("Oláa!!", Switch.name_bot.title())

    def desligar(self, Switch):
        server.notification ("Programa já se encontra desligado")
