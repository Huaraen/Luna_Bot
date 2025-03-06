from audio      import Audio
from datahora   import Datahora
from gatilho    import Set_up

audio = Audio()
dh = Datahora()

class Iniciar:
    '''Classe responsável por iniciar o bot e apresentar o usuário.'''
    def iniciar(self, bot_name):
        try:
            setup = Set_up()
            print("\nIniciando . . \n")
            checkin = input("Por Favor, informe nick: ")
            audio.toca_audios("link_start")
            return self.__intro(checkin, bot_name)
        except Exception as erro:
            print(f"Erro: ao iniciar: {erro}")

    def __intro(self, checkin, bot_name):
        try:
            print(f"{bot_name}: olá, {checkin}")
            print(f"{bot_name}: Hoje é dia {dh.data}")
        except Exception as erro:
            print(f"Erro: na introdução: {erro}")
        