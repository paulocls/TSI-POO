import requests
import tkinter as tk
from tkinter import messagebox

def consultar_banco():
    cod_banco = entry1.get()
    url = f"https://brasilapi.com.br/api/banks/v1/{cod_banco}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            resultado_label.config(text="Resultado da Consulta: Banco Cadastrado na Base")
            nome_banco_label.config(text=data["name"])
            
        else:
            resultado_label.config(text="Resultado da Consulta: Banco Inválido")
            nome_banco_label.config(text="Nome do Banco")
           
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar banco: {e}")

# Criando a interface TKinter
root = tk.Tk()
root.title("Consulta de Banco")
root.geometry('300x300')

tk.Label(root, text="Código do Banco:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Button(root, text="Consultar Banco", command=consultar_banco, bg='green', fg='white').pack()


resultado_label = tk.Label(root, text="Resultado da Consulta:")
resultado_label.pack()

nome_banco_label = tk.Label(root, text="Nome do Banco")
nome_banco_label.pack()
nome_banco_label['bg'] = 'yellow'

root.mainloop()