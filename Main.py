from microfone_off import Console
from microfone     import Mic
from commands      import Server
from gatilho       import Audio, Datahora
audio = Audio()
dh = Datahora()


class Main:
    def __init__(self):
        self.__princess = "luna"

    def name_bot (self):
        return self.__princess
    def exe(self):
        iniciar.iniciar(self.name_bot)
        while True:
            switch.check_power()
main = Main()

class Iniciar:
    def iniciar (self, bot):
        from gatilho import Set_up
        setup = Set_up()
        print ("\nIniciando . . \n")
        checkin = input ("Por Favor, informe nick: ")
        login = checkin.lower()
        audio.toca_audios("link_start")
        return self.__intro (checkin, bot)

    def __intro (self, checkin, bot):
        print ("{}: olá,  {}" .format (bot, checkin))
        print ("{}: Hoje é dia {}" .format (bot, dh.data))


class Switch:
    console  = Console(main.name_bot)
    mic      = Mic(main.name_bot)

    def __init__(self):
        self.executavel   = self.console
        self.estado_atual = Power_off()
        self.power        = False
        
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
        self.executavel =  self.mic
        server.notification("Iniciando comando por voz. .")


class Power_on:    
    def check_power(self, Switch):
        voz = Switch.executavel.power(Switch.power)
        if voz == "sleep":
            return self.desligar(Switch)
        elif voz == "fechar console": Switch.fechar_console()
        elif voz == "abrir console": Switch.abrir_console()
    def ligar(self, Switch):
        server.notification ("Programa já em andamento")
    def desligar(self, Switch):
        Switch.estado_atual = Power_off()
        Switch.power = False
        audio.toca_randomic_audio("go_to_sleep_", 4)

class Power_off:
    def check_power(self, Switch):
        command = Switch.executavel.power(Switch.power)
        if command == "fechar console": Switch.fechar_console()
        elif command == "abrir console": Switch.abrir_console()
        elif command == True:
            self.ligar(Switch)
    def ligar(self, Switch):
        Switch.estado_atual = Power_on()
        Switch.power = True
        audio.toca_randomic_audio("turn_on_", 5)
        server.notification("Oláa!!", main.name_bot.title())
    def desligar(self, Switch):
        server.notification ("Programa já se encontra desligado")


if __name__ == "__main__":
    iniciar  = Iniciar()
    switch   = Switch()
    server   = Server()
    main.exe()