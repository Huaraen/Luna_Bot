from server        import Server
from iniciar       import Iniciar
from switch        import Switch
from config        import Config


class Main:
    def __init__(self):
        self.__bot_name = Config.BOT_NAME

    @property
    def bot_name (self):
        return self.__bot_name
    
    def exe(self):
        switch = Switch()
        iniciar  = Iniciar()
        try:
            iniciar.iniciar(self.bot_name)
            while True:
                switch.check_power()
        except Exception as e:
            print(f"Erro ao executar o programa: {e}")


if __name__ == "__main__":
    try:
        main = Main()
        main.exe()
    except Exception as e:
        print(f"Erro ao iniciar o programa: {e}")