import speech_recognition as sr
from audio      import Audio
from server     import Server
from gatilho    import Verifica_voz
from random     import randrange
from config     import Config

verify_voice = Verifica_voz()
server = Server()
audio = Audio()

class Mic:
    def __init__(self):
        self.__name_bot = Config.BOT_NAME

    @property
    def name_bot(self):
        return self.__name_bot

    def power (self, is_power):
        if is_power: return Power_on().mic_on(self, is_power)
        else: return Power_off().mic_on(self, is_power)

class Power_on:
    '''se sistema se encontra ligado, identifica a voz
    e executa função.'''
    def __init__(self):
        self.__trig_turn_off = ["turn off", "vai pra casa", "dormir", "boa noite"]
    
    def mic_on(self, Miic, is_power):
        print ("\n｡◕ ‿ ◕ ｡")
        voice = Mic_turn_on().reconhecimento_mic(Miic, is_power)
        if Miic.name_bot == voice: verify_voice.voz_bot ()
        elif Miic.name_bot in voice:
            if "console" in voice: return "abrir console"
            for command_voice in self.__trig_turn_off:
                if command_voice in voice: return "sleep"
            voice = voice.replace((Miic.name_bot+" "), "")
            return verify_voice.realiza_comandos(voice)
        else:
            return verify_voice.just_voice (voice)

class Power_off:
    '''se sistema se encontra desligado, identifica a voz
    e se tiver o comando de ligar, liga o sistema.'''
    def __init__(self):
        self.__trig_turn_on = ["turn on", " ligar", "acord", "bom dia", "boa tarde", "boa noite", "despert"]

    def mic_on(self, Miic, is_power):
        voice = Mic_turn_on().reconhecimento_mic(Miic, is_power)
        if voice == False: return False
        elif Miic.name_bot in voice:
            if "console" in voice: return "abrir console"
            for command_voice in self.__trig_turn_on:
                if command_voice in voice: return True
            return self.__sleeping()
        else: return self.__sleeping()

    def __sleeping(self, Miic):
        server.notification(texto="Sleeping...", cardinal=(Miic.name_bot.title())) 
        roll20 = randrange(1, 20)
        if roll20 >= 18: audio.toca_audios("go_to_sleep_2", "bot")
        return False

class Mic_turn_on:
    def __init__ (self):
        self.reconhecimento = sr.Recognizer()


    def reconhecimento_mic(self, Miic, power):
        with sr.Microphone() as mic:
            reconhecimento_do_mic = self.reconhecimento.listen(mic)
            try:
                voice = self.reconhecimento.recognize_google(reconhecimento_do_mic,language= "pt-BR")
                voice = voice.lower()
                print (">>: {}".format(voice))
                return voice
            except sr.UnknownValueError:
                if power: return self.__power_on_unknownvalue_exception(Miic)
                else: return self.__power_off_unknownvalue_exception(Miic)     
            except sr.RequestError as e:
                if power: return self.__power_on_requesterror_exception(Miic, e)
                else: return self.__power_off_requesterror_exception(Miic, e)

    def __power_on_unknownvalue_exception(self, Miic):
        server.notification ("não consegui entender o que você disse", Miic.name_bot.title())
        roll20 = randrange(1,20)
        if roll20 > 13: audio.toca_randomic_audio("beep_", 9)
        return "unknown command" 
    def __power_off_unknownvalue_exception(self, Miic):        
        server.notification (":  Não estou em casa, deixe seu recado e eu vejo quando voltar", (Miic.name_bot.title()))
        return False

    def __power_on_requesterror_exception(self, Miic, e):
        print (Miic.name_bot.title(), ":  Error, Error. . .; {0}".format(e))
        audio.toca_audios("Hello_Monkeys")
        return "unknown command"
    def __power_off_requesterror_exception(self, Miic, e):    
        '''Não foi possivel requisitar resultados de Google Speech Recognition service'''
        server.notification (":  Error, Error. . . {0}".format(e)), (Miic.name_bot.title())
        return False


if "__main__" == __name__:
    while True:
        x = Mic_turn_on().reconhecimento_mic(power = True)
        if x == "sleep": break
        elif x == "unknown command": continue
        elif x == "abrir console": print ("abrir console")
        elif x == "fechar console": print ("fechar console")
        else: print (f"Comando: {x}")
        