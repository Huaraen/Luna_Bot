from commands      import Server
from iniciar       import Iniciar
from switch        import Switch


class Main:
    def __init__(self):
        self.__bot_name = "luna"
        self.switch = Switch(bot_name)

    @property
    def bot_name (self):
        return self.__bot_name
    
    def exe(self):
        iniciar.iniciar(self.bot_name)
        while True:
            self.switch.check_power()


if __name__ == "__main__":
    try:
        iniciar  = Iniciar()
        switch   = Switch()
        server   = Server()
        main = Main()
        main.exe()
    except Exception as e:
        print(f"Erro ao iniciar o programa: {e}")