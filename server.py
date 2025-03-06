from utility import Utility
from audio import Audio
from time import sleep

class Server:
    def notification(self, texto, cardinal="Cardinal"):
        '''Imprime a mensagem do sistema'''
        print(f"{cardinal}: {texto}")

    def mute(self, trigger):
        '''Mute'''
        try:
            tempo = Utility().separar_numeros_da_frase(trigger)
        except ValueError:
            tempo = 30
        mute_alert = [5, 15, 35, 55, 75, 95]
        Audio().toca_audios("yeah_no_problem", "bot")
        for sec in range(tempo):
            sleep(1)
            if sec in mute_alert:
                self.notification(f"Muted for {tempo - sec} Seconds")
        self.notification("Unmuter!")
        Audio().toca_randomic_audio("turn_on_", 5)

    def comando_invalido(self, trigger):
        '''Alerta na tela e áudio de comando inválido'''
        Audio().toca_audios("what")
        self.notification(f'Comando  ==> {trigger} <== Não Existente')


        