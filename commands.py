import webbrowser    as browser
import playsound     as ps
from os              import remove, system as os_system
from random          import randrange
from time            import sleep
from datetime        import datetime
from gtts            import gTTS


class Utility:
    def separar_numeros_da_frase (self, trigger):
        '''recebe texto, mantem e retorna somente numeros em inteiro'''
        apenas_digitos = ("")
        for caractere in trigger:
            if caractere.isdigit():
                apenas_digitos += caractere
        apenas_digitos = int(apenas_digitos)
        return apenas_digitos
            
            
class Datahora:
    '''retorna hora e/ou data atual''' 
    def _data_agora(self):
        '''retorna dia/mês'''
        return datetime.now().strftime("%d/%m")    
    def _hora_agora(self):
        '''retorna Horas:Minutos'''
        return datetime.now().strftime("%H:%M")
        # ("%H:%M:%S") Para segundos também.
    def _data_hora(self):
        '''retorna dia/mes/ano Horas:Minutos'''
        return datetime.now().strftime("%d/%m/%Y %H:%M")

    @property
    def dia(self):
        '''imprime, cria e reproduz audio com a data atual'''
        data = ("hoje é dia {}".format (self._data_agora()))
        print (data)
        Audio().cria_audio (data, "data_atual")
    
    @property
    def hora(self):
        '''imprime, cria e reproduz audio com as horas'''
        horas = ("agora são, {}".format (self._hora_agora()))
        print (horas)
        Audio().cria_audio (horas, "hora_atual")

    @property
    def data (self):
        '''retorna data atual em string'''
        return self._data_agora()


class Audio:
    def __init__(self):
        self.__path = "Audios/"
        self.__path_voices = "Audios/bot_sound/"

    def toca_audios (self, nome, fonte="audios"):
        '''reproduz audio.mp3, fonte "audios", "bot" ou informar caminho dentro da pasta Luna_bot terminando com /'''
        if fonte == "audios":
            path = self.__path
        elif fonte == "bot":
            path = self.__path_voices        
        else: path = fonte
        ps.playsound(f'{path}{nome}.mp3')

    def toca_randomic_audio(self, nome_audio, stop=2, start=1):
        random = str(randrange(start,stop+1))
        self.toca_audios(nome_audio+random, fonte="bot")
        return random
 
    def cria_audio(self, texto, nome_audio):
        '''Cria audio com base em texto'''
        tts = gTTS(texto, lang="pt-br")
        tts.save('{}{}.mp3'.format (self.__path, nome_audio))
        self.toca_audios(nome_audio)
        sleep (1)
        remove('{}{}.mp3'.format (self.__path, nome_audio))

    def playlist (self, album):
            '''toca musica'''
            if album == "bad apple":
                browser.open("https://open.spotify.com/track/3urItfkvXw8tPjwNs2lXdd?si=06f4bc2e97174db7")
            elif album == "anime":
                browser.open("https://open.spotify.com/playlist/3lsfveO1cBycWxcjbQ54Gw?si=d7fcc215816747ac")


class Server:
    def notification(self, texto, cardinal = "Cardinal"):
        '''imprime a mensagem do sistema'''
        print("{}: {}".format(cardinal, texto))

    def mute(self, trigger):
        '''Mute'''
        tempo = Utility().separar_numeros_da_frase(trigger)
        if tempo != int: tempo = 30
        mute_alert = [5, 15, 35, 55, 75, 95]
        Audio().toca_audios("yeah_no_problem", "bot")
        for sec in range (0,tempo):
            sleep (1)
            if sec in mute_alert:               
                self.notification ("Muted for {} Seconds" .format(tempo - sec))
        self.notification ("Unmuter!")
        Audio().toca_randomic_audio("turn_on_", 5)
    
    def comando_invalido (self, trigger):
        '''alerta na tela e audio de comando invalido'''
        Audio().toca_audios("what")
        self.notification('Comando  ==> {} <== Não Existente'.format(trigger))


class Browser:
    def abrir_aba_navegador (self, http):
        '''abre browser selecionado'''
        if http == "whatsapp":
            browser.open ("https://web.whatsapp.com/")
            print ("Abrindo Whats App")
        elif http == "google" or http == "navegador":
            browser.open ("https://www.google.com.br/")
            print ("Abrindo Google")
        elif http == "youtube":
            browser.open ("https://www.youtube.com/")
            print ("Abrindo Youtube")
        elif http == "alura" or http == "curso" or http == "allura":
            browser.open ("https://cursos.alura.com.br/category/data-science")
            print ("Abrindo Site de cursos da Alura")
        elif http == "discord":
            browser.open ("https://discord.com/channels/490586921664512001/708076678924206170")
            print ("Abrindo Discord")

    def procurar_youtube (self, search):
        '''procura no youtube'''
        search = search.replace(" ", "+")
        browser.open ("https://www.youtube.com/results?search_query={}".format(search))
        print ("Abrindo Youtube")

class Watch:
    def assistir(self, o_que_quer_assistir):
        if   o_que_quer_assistir == "anime":
            browser.open ("https://animesonline.cc/episodio/")
        elif o_que_quer_assistir == "série":
            browser.open ("https://pobreflix.top/")

class App:
    def __init__(self, path_atalhos):
        self.__path = path_atalhos

    def abrir_aplicativo (self, app):
        '''Abre aplicativo pelo atalho.lnk dentro da pasta Atalhos'''
        os_system ("start /d {} {}.lnk".format(self.__path, app))
    
    def abrir_programa(self, app):
        '''Abre programa direto'''
        os_system ("start {}".format(app))

    def fechar_aplicativo (self, app):
        '''Fecha aplicativo.exe'''
        try:        
            os_system('taskkill /f /im {}.exe'.format(app))
        except:
            Server().notification ("{}: Aplicativo não encontrado na barra de tarefas")
            Audio().cria_audio("Arquivo não encontrado", 'fechar_aplicativo')
        '''
        /f : Specifies that process(es) be forcefully terminated.
        /im (ImageName ): Specifies the image name of the process to be terminated.
        For more info regarding TaskKill --> 
        https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb491009(v=technet.10)?redirectedfrom=MSDN
        dir : 
        cd : change directory (cd User, .. "volta", / "à raiz" )
        ipconfig
        sfc /scannow : varredura
        Systeminfo
        tasklist
        Netstat : análise de conexões TCI/IP ativas na sua máquina
        '''

    


if __name__ == "__main__":
    Server().notification("Arquivo de propriedade extensão")
    for time in range (0,3):
        Server().notification(("Programa se desligando em {}".format(3-time)))
        sleep(1)
    exit()
