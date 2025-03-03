from gatilho import Audio, Datahora, Set_up

audio = Audio()
dh = Datahora()

class Iniciar:
    '''Classe responsável por iniciar o bot e apresentar o usuário.'''
    def iniciar(self, bot):
        try:
            setup = Set_up()
            print("\nIniciando . . \n")
            checkin = input("Por Favor, informe nick: ")
            audio.toca_audios("link_start")
            return self.__intro(checkin, bot)
        except Exception as erro:
            print(f"Erro: ao iniciar: {erro}")

    def __intro(self, checkin, bot):
        try:
            print(f"{bot}: olá, {checkin}")
            print(f"{bot}: Hoje é dia {dh.data}")
        except Exception as erro:
            print(f"Erro: na introdução: {erro}")
        