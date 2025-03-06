from server        import Server
from iniciar       import Iniciar
from switch        import Switch


class Main:
    def __init__(self):
        self.__bot_name = "cacau"
        self.switch = Switch(self.bot_name)


    @property
    def bot_name (self):
        return self.__bot_name
    
    def exe(self):
        try:
            iniciar.iniciar(self.bot_name)
            while True:
                self.switch.check_power()
        except Exception as e:
            print(f"Erro ao executar o programa: {e}")


if __name__ == "__main__":
    try:
        main = Main()
        iniciar  = Iniciar()
        server   = Server()
        main.exe()
    except Exception as e:
        print(f"Erro ao iniciar o programa: {e}")