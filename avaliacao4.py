import random

from tkinter import *

class App():
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('300x200')
        self.janela.title('Números da Mega Sena')

        self.fram1 = Frame(self.janela)
        self.fram1.pack(pady=10)
        self.rotulo = Label(self.fram1, text="Os numeros da Mega Sena")
        self.rotulo.pack(side=LEFT)

        self.fram2 = Frame(self.janela)
        self.fram2.pack(pady=10)
        self.botao = Button(self.fram2, text="Gerar números", width=100, command=self.loteria)
        self.botao.pack(side=LEFT, pady=20, padx=10)

        self.fram3 = Frame(self.janela)
        self.fram3.pack(pady=10)

        self.label1 = Label(self.fram3)
        self.label1['bg'] = 'green'
        self.label1['font'] = 'bold'
        self.label1.pack()

        self.janela.mainloop()

    def loteria(self):
        #Gerar seis números aleatórios
        num = [random.randint(1,60) for i in range(6)]

        #Criar um lista 
        lista = list(set(num))
        lista_ordenada = sorted(lista)
        self.label1.config(text=f'{lista_ordenada}')
        
aplicacao=App()

