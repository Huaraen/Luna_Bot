from commands import Utility, Datahora, Audio, Server, Browser, App, Watch
from random import randrange
from time import sleep

class Body:
    def __init__(self, prox_comando=None):
        self.__bot = "luna"
        self.__prox_comando = prox_comando

    def proximo_comando_a_ser_executado (self, voice):
        '''retorna string'''
        if self.__prox_comando is None:
            return ''
        else:
            return self.__prox_comando.check(voice)

    @property
    def bot (self):
        '''retorna string do bot'''
        return self.__bot
    @property
    def bot_name(self):
        '''retorna string do bot formatado'''
        return self.__bot.title()

    def procura_em_lista_e_executa_programa (self, self_lista, voz_ouvida):
        for frase in self_lista:
            if frase in voz_ouvida:
                sett.check_comando_executado("comando executado")
                return True
        return False


class Set_up:
    __cute_mode = False
    __anger = 0
    
    def __init__(self):
        self.algum_comando_foi_executado = Comando_nao_executado()

    @property
    def mood (self):
        '''check quantidade de raiva'''
        return self.__anger

    def check_comando_executado(self, comando):
        return self.algum_comando_foi_executado.check_comando_executado(self, comando)
    def comando_executado (self):
        self.algum_comando_foi_executado.comando_executado(self)
    def comando_nao_executado (self):
        self.algum_comando_foi_executado.comando_nao_executado(self)

<<<<<<< HEAD
=======
class Comando_ja_executado:
    def check_comando_executado (self, Setup, comando):
        if comando == "startando comandos":
            self.comando_nao_executado(Setup)
        elif comando == "comando foi executado":
            return True            
    def comando_executado (self, Setup):
        server.notification("comando já foi executado")
    def comando_nao_executado (self, Setup):
        Setup.algum_comando_foi_executado = Comando_nao_executado()

class Comando_nao_executado:
    def check_comando_executado (self, Setup, comando):
        if comando == "comando executado":
            self.comando_executado(Setup)
        elif comando == "comando foi executado":
            return False
    def comando_executado (self, Setup):
        Setup.algum_comando_foi_executado = Comando_ja_executado()
    def comando_nao_executado (self, Setup):
        server.notification("comando ainda não foi executado")


class Angry:
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
    def angry (self):
        '''retorna True caso ela esteja brava'''
        roll20 = randrange(1,21)
        if roll20 <= sett.mood:
            audio.toca_randomic_audio("angry_", 6)
            self.somar_mood(1)
            return True
        else: return False

    def somar_mood(self, anger):
        '''soma raiva atual com a causa'''
        sett.__anger += anger
        if sett.mood < 0: sett.__anger = 0


<<<<<<< HEAD
class Comando_ja_executado:
    def check_comando_executado (self, Setup, comando):
        if comando == "Iniciando comandos":
            self.comando_nao_executado(Setup)
        elif comando == "Comando foi executado":
            return True            
    def comando_executado (self, Setup):
        server.notification("Comando já foi executado")
    def comando_nao_executado (self, Setup):
        Setup.algum_comando_foi_executado = Comando_nao_executado()


class Comando_nao_executado:
    def check_comando_executado (self, Setup, comando):
        if comando == "Comando executado":
            self.comando_executado(Setup)
        elif comando == "Comando foi executado":
            return False
    def comando_executado (self, Setup):
        Setup.algum_comando_foi_executado = Comando_ja_executado()
    def comando_nao_executado (self, Setup):
        server.notification("Comando ainda não foi executado")


class Just_voice:
    def check(self, voz):
        if sett.angry(): 
            if sett.mood >= 9 and "desculp" in voz:
                x = audio.toca_randomic_audio("angry_mood_sorry_", stop=4)
                if x == 1: sett.somar_mood (-4)
                else: sett.somar_mood (-2)
                return "still angry "
            return "angry"
=======
class Just_voice:
    def check(self, voz):
        if angry.angry(): return "angry"
        elif sett.mood >= 9 and "desculp" in voz:
            x = audio.toca_randomic_audio("angry_mood_sorry_", stop=4)
            if x == 1: angry.somar_mood (-4)
            else: angry.somar_mood (-2)
            return "still angry "
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
        else:
            yes_or_no_questions = ["você conhece", "você gosta", "você está", "você é"]
            if   "fogo" in voz or "fire" in voz:
                server.notification("Fogoo!!", body.bot_name)
                audio.toca_audios("fire_fire")
                return "audio "
            elif "macaco" in voz or "trol" in voz:
                server.notification("\n.   _/﹋\_\n    (҂`_´)\n    <,︻╦̵̵̿╤─ ҉     ~  •", body.bot_name)
                audio.toca_audios("hello_monkeys")
                return "audio "
<<<<<<< HEAD
            elif "é um robo" in voz or "e um robo" in voz:
=======
            elif "é um robo" in voz:
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
                audio.toca_randomic_audio("are_you_a_bot_", 6)
                return "audio "
            elif "*" in voz:
                audio.toca_randomic_audio("been_rude_with_bot_", 3)
<<<<<<< HEAD
                sett.somar_mood (4)
                return "audio "
            elif "sentido da vida" in voz:
                audio.toca_audios("meaning_of_life", "bot")
                sett.somar_mood (-1)
=======
                angry.somar_mood (4)
                return "audio "
            elif "sentido da vida" in voz:
                audio.toca_audios("meaning_of_life", "bot")
                angry.somar_mood (-1)
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
                return "audio "
            elif "sobre você" in voz:
                audio.toca_randomic_audio("tell_me_something_about_yourself_", 4)
                return "audio "
            elif "você é d" in voz or "você veio d" in voz or "nasceu" in voz:
                audio.toca_randomic_audio("where_are_you_from_", 8)
<<<<<<< HEAD
                sett.somar_mood (-1)
                return "audio "
            elif "vinho" in voz:
                audio.toca_audios("osmanthus_wine_taste_the_same_as_I_remember","bot")
                sett.somar_mood (-1)
=======
                angry.somar_mood (-1)
                return "audio "
            elif "vinho" in voz:
                audio.toca_audios("osmanthus_wine_taste_the_same_as_I_remember","bot")
                angry.somar_mood (-1)
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
                return "audio "
            elif "você é solteir" in voz:
                audio.toca_audios("are_you_single","bot")
                return "audio "
            elif "você gosta d" in voz:
                audio.toca_randomic_audio("do_you_like_",11)
                return "audio "
            elif body.procura_em_lista_e_executa_programa(yes_or_no_questions, voz) or "ta bem" in voz or "está bem" in voz:
                rolld6 = randrange(1, 7)
                if   rolld6 == 1 or rolld6 == 4:
                    audio.toca_randomic_audio("y_n_classic_five_responses_", 4)
                elif rolld6 == 2 or rolld6 == 5:
                    audio.toca_randomic_audio("no_", 11)
                elif rolld6 == 3 or rolld6 == 6:
                    audio.toca_randomic_audio("yes_", 10)
                return "audio "
            return "sem audio "


class Audio_Command:
<<<<<<< HEAD
    '''Retorna Comandos de áudio '''
=======
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
    def accept(self, is_random = True):
        ''' 1 = roger_that, 2 = oky, 3 = jg Song, else = Yeah_no_problem'''
        if is_random: random_number = randrange(1, 5)
        else: random_number = is_random

        if   random_number == 1:
            audio.toca_audios("roger_that", "bot")
        elif random_number == 2:
            audio.toca_audios("oky", "bot")
        elif random_number == 3:
            audio.toca_audios("jp_wakatta", "bot")
        else:
            audio.toca_audios("yeah_no_problem", "bot")


class Set:
    def check (self, voz):
        if "humor" in voz: self.__irritada (voz)
        elif "especial" in voz or "configuração" in voz or "fofa" in voz or "cute" in voz or "fofura" in voz: self.__cute_mode(voz)
        else: return Just_voice().check(voz)

    def __cute_mode (self, trigger):
        if sett.__cute_mode: sett.__cute_mode = False, print ("off")
        else: sett.__cute_mode = True, print ("on")
        server.notification("Mood Changed")
        audio_cmd.accept(3)

    def __irritada(self, trigger):
        new_anger = utility.separar_numeros_da_frase(trigger)
        try:
            audio.toca_audios("number_{}".format(new_anger), "bot")
        except:
            raise server.notification("Executando..")
        finally:
            server.notification("Changed...")
            self.__set_anger (new_anger)
            audio_cmd.accept()
            
    def __set_anger(self, new_anger):
        sett.__anger = new_anger
        if sett.__anger is None: sett.__anger = 0

<<<<<<< HEAD
'''
verifica_voz = "verifica_voz.txt"
verifica_voz_arquivo = open(verifica_voz, 'w')
lista_voz = ("defin", "mude", "mudar", "set")
verifica_voz_arquivo.write(lista_voz)
    verifica_voz_arquivo = open ('verifica_voz.txt')
'''
class Verifica_voz(Body):    
=======

class Verifica_voz(Body):
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
    def realiza_comandos (self, voz):
        __config_options = ["defin", "mude", "mudar", "set"]
        if body.procura_em_lista_e_executa_programa(__config_options, voz): Set().check(voz)
        sett.check_comando_executado("startando comandos")
        lista_de_comandos = Dia(Hora(Musica(Navegador(Assistir(Programas_abrir(Programas_fechar
        (Algo_youtube(Mute(Desligar(Unknown_command()))))))))))
        return lista_de_comandos.check(voz)
    
    def command_voice(self, voz):
        '''retorna set config, unknown command ou lista de comandos'''
        config_options = ["defin", "mude", "mudar"]
        for gatilho in config_options:
            if gatilho in voz: return sett.check(voz)
        if "unknown command" in voz: return unknown__commando.check()
        else: 
            print ("executando comando com bot")
            return self.proximo_comando_a_ser_executado(voz)
    
    def voz_bot(self):
        '''executa comando de voz ao chamar pelo bot'''
        audio.toca_audios("nya_button")
    def just_voice(self, voz):
        '''executa comando quandos solicitado somente voz'''
        return Just_voice().check(voz)


class Base_Comandos(Body):
    def check(self, voz):
        if self.tem_palavra_chave_e_comando(voz):
            return self.executa_comando(voz)
        else: return self.nao_tem_comando_ir_ao_proximo_da_lista(voz)

    def tem_palavra_chave_e_comando (self, voz):
        pass
    def executa_comando (self, voz):
        pass
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        pass


class Dia(Base_Comandos):
    __trig_dia = ["data de hoje", "dia é hoje"]
    def tem_palavra_chave_e_comando (self, voz):
        if "dia" in voz or "data" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_dia, voz)
        else: return False
    def executa_comando (self, voz):
        dh.dia
        return self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)
        

class Hora(Base_Comandos):
    __trig_hour = ["que horas são", "diga as hora"]
    def tem_palavra_chave_e_comando (self, voz):
        if "hora" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_hour, voz)
        return False            
    def executa_comando (self, voz):
        dh.hora
        return self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Musica(Base_Comandos):
<<<<<<< HEAD
    __trig_musica = ["anime", "bad apple"] 
=======
    __trig_musica = ["anime", "bad apple"]
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
    def tem_palavra_chave_e_comando (self, voz):
        if "toca" in voz or "tocar" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_musica, voz)
        else: return False
    def executa_comando (self, voz):
        for musica in self.__trig_musica:
            if musica in voz:
                server.notification("tocando musica {}".format (musica), body.bot_name)
                audio.playlist (musica)
        return self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)
        

class Navegador(Base_Comandos):
    __trig_browser = ["google", "navegador", "discord", "youtube", "allura", "alura",
                    "curso", "whatsapp"]
    def tem_palavra_chave_e_comando (self, voz):
        if "abrir" in voz or "abre" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_browser, voz)
        return False
    def executa_comando (self, voz):
        for aba_browser in self.__trig_browser:
            if aba_browser in voz:
                browser.abrir_aba_navegador(aba_browser)
        return self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)

class Assistir(Base_Comandos):
    __trig_assistir = ["anime", "filme", "série"]
    def tem_palavra_chave_e_comando(self, voz):
        if "assisti" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_assistir, voz)
        return False
    def executa_comando (self, voz):
        if "anime" in voz: 
            server.notification("Abrindo site para assistir animes", body.bot_name)
            assistir_app.assistir("anime")
        elif "série" in voz or "filme" in voz:
            server.notification("Abrindo site para assistir séries", body.bot_name)
            assistir_app.assistir("série")
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Programas_abrir(Base_Comandos):
    __trig_programas = ["bloco de notas", "sul", "league of legends", "navegador", "spotify", "gerenciador de tarefas"]
    def tem_palavra_chave_e_comando (self, voz):
        if "abrir" in voz or "abre" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_programas, voz)
        else: return False
    def executa_comando (self, voz):
        if "league" in voz or "legends" in voz:
            server.notification("Abrindo lolzinho", body.bot_name)
            app.abrir_aplicativo("League_of_Legends")
        elif "spotify" in voz:
            server.notification("Abrindo Spotify", body.bot_name)
            app.abrir_aplicativo("spotify")
        elif "sul" in voz:
            server.notification("Abrindo Osu!", body.bot_name)
            app.abrir_aplicativo("osu!")
        elif "bloco de notas" in voz:
            server.notification("Abrindo bloco de notas", body.bot_name)
            app.abrir_programa("notepad")
        elif "gerenciador de tarefas" in voz:
            server.notification("Abrindo Gerenciador de tarefas", body.bot_name)
            app.abrir_programa("taskmgr")
        return self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Programas_fechar(Programas_abrir):
    __trig_programas = ["bloco de notas", "sul", "league of legends", "navegador", "spotify"]
    def tem_palavra_chave_e_comando (self, voz):
        if "fecha" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_programas, voz)
        else: return False
    def executa_comando (self, voz):
        if "navegador" in voz:
            server.notification("Fechando navegador", body.bot_name)
            app.fechar_aplicativo("msedge")
        elif "league" in voz or "legends" in voz:
            server.notification("Fechando Lolzinho", body.bot_name)
            app.fechar_aplicativo("LeagueClient")
        elif "spotify" in voz:
            server.notification("Fechando Spotify", body.bot_name)
            app.fechar_aplicativo("spotify")
        elif "sul" in voz:
            server.notification("Fechando Osy!", body.bot_name)
            app.fechar_aplicativo("osu!")
        elif "bloco de notas" in voz:
            server.notification("Fechando bloco de notas", body.bot_name)
            app.fechar_aplicativo("notepad")
        return self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Algo_youtube(Base_Comandos):
    def tem_palavra_chave_e_comando (self, voz):
        if  "procur" in voz and " no youtube" in voz or "pesquis" in voz and " no youtube" in voz:
            return True
        else: return False
    def executa_comando (self, voz):
        pesquisar_sobre = self.formatacao_para_pesquisar(voz)
        server.notification("Abrindo Youtube e pesquisando", body.bot_name)
        browser.procurar_youtube(pesquisar_sobre)
        sett.check_comando_executado("comando executado")
        return self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)

    def formatacao_para_pesquisar(self, voz):
        __filtro_de_palavras = ["procurar", "procure", "procura", "sobre", "no youtube", "pesquisar", "pesquise",
<<<<<<< HEAD
                                    "pesquisa", "pra mim", "para mim", "luna"]
=======
                                    "pesquisa", "pra mim", "para mim"]
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
        for palavras in __filtro_de_palavras:
            if palavras in voz:
                voz = voz.replace (palavras+' ', "")
                voz = voz.replace (' '+palavras, "")
        return voz


class Mute(Base_Comandos):    
    __trig_mute = ["mutar", "mute", "silenci", "quiet"]
    def tem_palavra_chave_e_comando (self, voz):
        return self.procura_em_lista_e_executa_programa(self.__trig_mute, voz)
    def executa_comando (self, voz):
        server.mute(voz)
        return self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Desligar(Base_Comandos):
    __trig_turn_off = ["desligue", "desligar", "desativar", "desative", "tchau", "até mais"]
    def tem_palavra_chave_e_comando (self, voz):
        return self.procura_em_lista_e_executa_programa(self.__trig_turn_off, voz)
    def executa_comando (self, voz):
        server.notification("Going Home", body.bot_name)
        audio.toca_randomic_audio("go_home_", 6)
        sleep(1)
        exit()
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Unknown_command:
    def check(self, voz):
        if not sett.check_comando_executado("comando foi executado"):
            x =  Just_voice().check(voz)
            if "sem audio" in x:
                audio.toca_audios("what")
                server.notification('Comando  ==> {} <== Não Existente'.format(voz))
                return "comando desconhecido"
            else: return x
        else: return "executado"


# Commands
utility           = Utility()
dh                = Datahora()
audio             = Audio()
server            = Server()
browser           = Browser()
assistir_app      = Watch()
app               = App("Atalhos")

# Gatilhos
body              = Body()
sett              = Set_up()
<<<<<<< HEAD
=======
angry             = Angry()
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
audio_cmd         = Audio_Command()
unknown__commando = Unknown_command()

if __name__ == "__main__": 
<<<<<<< HEAD
    paralelo = False
    while paralelo:
=======
    while True:
>>>>>>> 05513dda182a0d74069cdb35a5c8e885b22396d0
        voice = (input(">> "))
        Verifica_voz().realiza_comandos(voice)
        if voice == "sair":
            exit()
        