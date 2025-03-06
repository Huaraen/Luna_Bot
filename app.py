from os import system as os_system
from audio import Audio
from server import Server

class App:
    def __init__(self, path_atalhos):
        self.__path = path_atalhos

    def abrir_aplicativo(self, app):
        '''Abre aplicativo pelo atalho.lnk dentro da pasta Atalhos'''
        os_system(f"start /d {self.__path} {app}.lnk")

    def abrir_programa(self, app):
        '''Abre programa direto'''
        os_system(f"start {app}")

    def fechar_aplicativo(self, app):
        '''Fecha aplicativo.exe'''
        try:
            os_system(f'taskkill /f /im {app}.exe')
        except:
            Server().notification(f"{app}: Aplicativo não encontrado na barra de tarefas")
            Audio().cria_audio("Arquivo não encontrado", 'fechar_aplicativo')