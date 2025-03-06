import re

class Utility:
    def separar_numeros_da_frase(self, trigger):
        '''Recebe texto, mantém e retorna somente números em inteiro'''
        apenas_digitos = int(''.join(re.findall(r'\d+', trigger)))
        return apenas_digitos
    
    