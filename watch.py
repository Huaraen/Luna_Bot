import webbrowser as browser

class Watch:
    def assistir(self, o_que_quer_assistir):
        if o_que_quer_assistir == "anime":
            browser.open("https://animesonline.cc/episodio/")
        elif o_que_quer_assistir == "série":
            browser.open("https://pobreflix.top/")