from datetime import datetime
from audio import Audio

class Datahora:
    '''Retorna hora e/ou data atual'''
    def _data_agora(self):
        '''Retorna dia/mês'''
        return datetime.now().strftime("%d/%m")

    def _hora_agora(self):
        '''Retorna Horas:Minutos'''
        return datetime.now().strftime("%H:%M")

    def _data_hora(self):
        '''Retorna dia/mês/ano Horas:Minutos'''
        return datetime.now().strftime("%d/%m/%Y %H:%M")

    @property
    def dia(self):
        '''Imprime, cria e reproduz áudio com a data atual'''
        data = f"hoje é dia {self._data_agora()}"
        print(data)
        Audio().cria_audio(data, "data_atual")

    @property
    def hora(self):
        '''Imprime, cria e reproduz áudio com as horas'''
        horas = f"agora são, {self._hora_agora()}"
        print(horas)
        Audio().cria_audio(horas, "hora_atual")

    @property
    def data(self):
        '''Retorna data atual em string'''
        return self._data_agora()