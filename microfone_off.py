from server     import Server
from audio      import Audio
from gatilho    import Verifica_voz
from random     import randrange
from config     import Config   

verify_voice = Verifica_voz()
server = Server()
audio = Audio()

class Console():
    def __init__(self):
        self.__bot_name = Config.BOT_NAME

    @property
    def bot_name(self):
        return self.__bot_name

    def power (self, is_power):
        if is_power: return Power_on().mic_on()
        else: return Power_off().mic_on()

class Power_on():
    '''se sistema se encontra ligado, identifica a voz
    e executa função.'''
    def __init__(self):
        self.bot_name = Config.BOT_NAME
        self.__trig_turn_off = ["turn off", "vai pra casa", "dormir", "boa noite"]
    
    def mic_on(self):
        voice = input("... ")
        if self.bot_name == voice: 
            return verify_voice.voz_bot ()
        elif self.bot_name in voice:
            for command_voice in self.__trig_turn_off:
                if command_voice in voice:
                    return "sleep"
            if "console" in voice: return "fechar console"
            voice = voice.replace((self.bot_name+" "), "")
            return verify_voice.realiza_comandos(voice)
        else:
            return verify_voice.just_voice (voice)

class Power_off():
    '''se sistema se encontra desligado, identifica a voz
    e se tiver o comando de ligar, liga o sistema.'''
    def __init__(self):
        self.bot_name = Config.BOT_NAME
        self.__trig_turn_on = ["turn on", " ligar", "acord", "bom dia", "boa tarde", "boa noite", "despert"]

    def mic_on(self):
        voice = input("... ")
        if self.bot_name in voice:
            if "console" in voice: return "fechar console"
            for command_voice in self.__trig_turn_on:
                if command_voice in voice: return True
            return self.__sleeping()
        else: return self.__sleeping()

    def __sleeping(self):
        server.notification("Sleeping...", self.bot_name) 
        roll20 = randrange(1, 20)
        if roll20 >= 16: audio.toca_audios("go_to_sleep_2", "bot")
        return False