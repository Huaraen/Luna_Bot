from iniciar       import Iniciar
from switch        import Switch

class Main:
    '''Classe principal que inicializa o bot e executa o loop principal.'''
    def __init__(self):
        self.__name_bot = "luna"
        self.switch = Switch(self.name_bot)

    @property
    def name_bot(self):
        return self.__name_bot
    
    def exe(self):
        try:
            iniciar.iniciar(self.name_bot)
            while True:
                self.switch.check_power()
        except Exception as e:
            print (f'Ocorreu um erro: {e}')

if __name__ == "__main__":
    try:
        iniciar = Iniciar()
        main = Main()
        main.exe()
    except Exception as e:
        print (f'Ocorreu um erro ao iniciar: {e}')
