from tkinter import *

class App:
    def __init__(self):
        #iniciação da janela
        self.janela = Tk()
        self.janela.title('Agenda')
        self.janela.geometry('400x200')
        
        self.agenda = {} #Dicionário para guardar os contatos

        #Interface gráfica
        self.frame1 = Frame(self.janela)
        self.frame1.pack(pady=10)
        self.frame2 = Frame(self.janela)
        self.frame2.pack(pady=5)
        self.frame3 = Frame(self.janela)
        self.frame3.pack(pady=5)
        self.frame4 = Frame(self.janela)
        self.frame4.pack(pady=5)
        self.frame5 = Frame(self.janela)
        self.frame5.pack(pady=5)
        self.frame6 = Frame(self.janela)
        self.frame6.pack(pady=5)

        self.rotulo1 = Label(self.frame1, text='Insira Contatos na Agenda')
        self.rotulo1.pack(side=LEFT)

        self.rotulo2 = Label(self.frame2, text='Nome:')
        self.rotulo2.pack(side=LEFT)

        self.caixa2 = Entry(self.frame2)
        self.caixa2.pack(side=RIGHT)

        self.rotulo3 = Label(self.frame3, text='Telefone:')
        self.rotulo3.pack(side=LEFT)

        self.caixa3 = Entry(self.frame3)
        self.caixa3.pack(side=RIGHT)

        self.botao = Button(self.frame4, text='Inserir', width=100, command=self.cadastrar)
        self.botao.pack(side=LEFT, pady=20, padx=10)
       # self.figura = PhotoImage(file='Unidade5\btn_ok.png')
        #self.botao['compound'] = 'left'
        #self.botao['image'] = self.figura

        self.label5 = Label(self.frame5)
        self.label5['bg'] = 'green'
        self.label5['font'] = 'bold'
        self.label5.pack()
    
        self.janela.mainloop()

    #Função cadastrar o usuário
    def cadastrar(self):
        nome = self.caixa2.get()
        telefone = self.caixa3.get()

        if nome and telefone:
            self.agenda[nome] = telefone
            print("Agenda atualizada:", self.agenda)
            self.label5.config(text=f"Contato '{nome}' adicionado com sucesso!")
            self.caixa2.delete(0, END)
            self.caixa3.delete(0, END)
                  
aplicacao=App()