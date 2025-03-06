import webbrowser as browser

class Browser:
    def abrir_aba_navegador(self, http):
        '''Abre browser selecionado'''
        urls = {
            "whatsapp": "https://web.whatsapp.com/",
            "google": "https://www.google.com.br/",
            "navegador": "https://www.google.com.br/",
            "youtube": "https://www.youtube.com/",
            "alura": "https://cursos.alura.com.br/category/data-science",
            "curso": "https://cursos.alura.com.br/category/data-science",
            "allura": "https://cursos.alura.com.br/category/data-science",
            "discord": "https://discord.com/channels/490586921664512001/708076678924206170"
        }
        if http in urls:
            browser.open(urls[http])
            print(f"Abrindo {http.capitalize()}")
        else:
            print(f"URL para {http} não encontrada")

    def procurar_youtube(self, search):
        '''Procura no youtube'''
        search = search.replace(" ", "+")
        browser.open(f"https://www.youtube.com/results?search_query={search}")
        print("Abrindo Youtube")