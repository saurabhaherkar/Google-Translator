from googletrans import Translator, LANGUAGES

class MyTranslator:
    def __init__(self):
        self.lang = list(LANGUAGES.values())
        print(self.lang)

    def run(self, txt = 'Type text here', src = 'english', dest = 'hindi'):
        self.translator = Translator()
        self.txt = txt
        self.src = src
        self.dest = dest
        try:
            self.translated = self.translator.translate(self.txt, src=self.src, dest=self.dest)
        except:
            self.translated = self.translator.translate(self.txt)
        self.tt = self.translated.text
        return self.tt

if __name__ == '__main__':
    a = MyTranslator()