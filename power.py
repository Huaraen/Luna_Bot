from server        import Server
from gatilho       import Audio, Datahora

audio = Audio()
dh = Datahora()
server   = Server()

class Power_on:
    '''se sistema se encontra ligado, identifica a voz'''
    def check_power(self, Switch):
        try:
            voz = Switch.executavel.power(Switch.power)
            cmd_voz = ['sleep', 'dormir']
            for cmd_voz_check in cmd_voz:
                if voz == cmd_voz_check:return self.desligar(Switch)
            if voz == "fechar console": Switch.fechar_console()
            elif voz == "abrir console": Switch.abrir_console()
        except Exception as e:
            print(f"Erro ao verificar power (ligado): {e}")

    def ligar(self, Switch):
        try:
            server.notification ("Programa já em andamento")
        except Exception as e:
            print(f"Erro ao ligar (ligado): {e}")

    def desligar(self, Switch):
        try:
            Switch.estado_atual = Power_off()
            Switch.power = False
            server.notification ("Turning Off")
            audio.toca_randomic_audio("go_to_sleep_", 4)
        except Exception as e:
            print(f"Erro ao desligar (ligado): {e}")

class Power_off:
    '''se sistema se encontra desligado, identifica a voz'''
    def check_power(self, Switch):
        try:
            command = Switch.executavel.power(Switch.power)
            if command == "fechar console": Switch.fechar_console()
            elif command == "abrir console": Switch.abrir_console()
            elif command == True: self.ligar(Switch)
        except Exception as e:
            print(f"Erro ao verificar power (desligado): {e}")

    def ligar(self, Switch):
        try:
            Switch.estado_atual = Power_on()
            Switch.power = True
            audio.toca_randomic_audio("turn_on_", 5)
            server.notification("Oláa!!", Switch.bot_name.title())
        except Exception as e:
            print(f"Erro ao ligar (desligado): {e}")    

    def desligar(self, Switch):
        try:
            server.notification ("Programa já se encontra desligado")
        except Exception as e:
            print(f"Erro ao desligar (desligado): {e}")




