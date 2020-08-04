from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class MyTranslator:
    def __init__(self):
        self.lang = list(LANGUAGES.values())

    def run(self, txt = 'Type text here', src='english', dest='hindi'):
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

def doaction():
    s = ssrlang.get()
    d = dstlang.get()
    message = sourceText.get(1.0, END)
    translator = MyTranslator()
    text = translator.run(txt=message, src=s, dest=d)
    destText.delete(1.0, END)
    destText.insert(END, text)

app = Tk()
app.geometry('350x520')
app.title('Google Translator')
app.resizable(0, 0)
app.config(bg='blue')

appName = Label(app, text='Google Translate', font=('Arial 20'), fg='goldenrod1', bg='green', height=2)
appName.pack(side=TOP, fill=BOTH, pady=0)
version = Label(app, text='beta', bg='green').place(x=250, y=45)

frame = Frame(app).pack(side=BOTTOM)
sourceText = Text(frame, font=('arial 10'), height=11, wrap=WORD)
sourceText.pack(side=TOP, padx=5, pady=5)

trans = Button(frame, text='Translate', font=('arial 10 bold'), fg='red', bg='blue', activebackground='green', relief=GROOVE, command=doaction)
trans.pack(side=TOP, pady=15)

langs = MyTranslator().lang

ssrlang = ttk.Combobox(frame, values=langs, width=10)
ssrlang.place(x=30, y=280)
ssrlang.set('english')

dstlang = ttk.Combobox(frame, values=langs, width=10)
dstlang.place(x=240, y=280)
dstlang.set('hindi')

destText = Text(frame, font=('arial 10'), height=12, wrap=WORD)
destText.pack(side=TOP, padx=5, pady=5)

app.mainloop()