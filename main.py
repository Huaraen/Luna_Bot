from iniciar    import Iniciar
from switch     import Switch
from gatilho    import Audio, Datahora

audio = Audio()
dh = Datahora()

class Main:
    '''Classe principal que inicializa o bot e executa o loop principal.'''
    def __init__(self):
        self.__bot_name = "luna"
        self.switch = Switch(self.__bot_name)

    @property
    def name_bot (self):
        return self.__bot_name
    
    def exe(self):
        iniciar.iniciar(self.name_bot)
        while True:
            self.switch.check_power()
            
if __name__ == "__main__":
    iniciar  = Iniciar()
    main = Main()
    main.exe()























    