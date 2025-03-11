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
            # Extrai o tempo do comando usando a função separar_numeros_da_frase
            tempo = Utility().separar_numeros_da_frase(trigger)
        except ValueError:
            # Extrai o tempo do comando usando a função separar_numeros_da_frase
            tempo = 30

        # Lista de alertas de tempo
        mute_alert = [5, 15, 35, 55, 75, 95]
        self.notification(f"Muted for {tempo} Seconds")

        # Áudio de confirmação
        Audio().toca_audios("yeah_no_problem", "bot")

        # Contagem regressiva
        for sec in range(tempo):
            sleep(1)
            if sec in mute_alert:
                self.notification(f"Muted for {tempo - sec} Seconds")
        
        # Áudio de desmutar
        self.notification("Unmuter!")
        Audio().toca_randomic_audio("turn_on_", 5)

    def comando_invalido(self, trigger):
        '''Alerta na tela e áudio de comando inválido'''
        Audio().toca_audios("what")
        self.notification(f'Comando  ==> {trigger} <== Não Existente')


        