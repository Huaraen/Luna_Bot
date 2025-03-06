import playsound as ps
from os import remove
from random import randrange
from time import sleep
from gtts import gTTS
from browser import Browser
browser = Browser()

class Audio:
    def __init__(self):
        self.__path = "Audios/"
        self.__path_voices = "Audios/bot_sound/"

    def toca_audios(self, nome, fonte="audios"):
        '''Reproduz audio.mp3, fonte "audios", "bot" ou informar caminho dentro da pasta Luna_bot terminando com /'''
        path = self.__path if fonte == "audios" else self.__path_voices if fonte == "bot" else fonte
        ps.playsound(f'{path}{nome}.mp3')

    def toca_randomic_audio(self, nome_audio, stop=2, start=1):
        random = str(randrange(start, stop + 1))
        self.toca_audios(nome_audio + random, fonte="bot")
        return random

    def cria_audio(self, texto, nome_audio):
        '''Cria áudio com base em texto'''
        tts = gTTS(texto, lang="pt-br")
        tts.save(f'{self.__path}{nome_audio}.mp3')
        self.toca_audios(nome_audio)
        sleep(1)
        remove(f'{self.__path}{nome_audio}.mp3')

    def playlist(self, album):
        '''Toca música'''
        if album == "bad apple":
            browser.open("https://open.spotify.com/track/3urItfkvXw8tPjwNs2lXdd?si=06f4bc2e97174db7")
        elif album == "anime":
            browser.open("https://open.spotify.com/playlist/3lsfveO1cBycWxcjbQ54Gw?si=d7fcc215816747ac")