import sqlite3
import tkinter as tk

# Inicializa banco de dados e tabela
def inicializar_banco():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            matricula TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para incluir aluno
def incluir_aluno():
    matricula = entry_matricula.get().strip()
    nome = entry_nome.get().strip()

    if not matricula or not nome:
        label_resultado.config(text="Por favor, preencha os dois campos.")
        return

    try:
        conn = sqlite3.connect('alunos.db')
        cursor = conn.cursor()

        # Verifica se já existe a matrícula
        cursor.execute("SELECT * FROM registros WHERE matricula = ?", (matricula,))
        resultado = cursor.fetchone()

        if resultado is not None:
            label_resultado.config(text="Matrícula já Cadastrada")
        else:
            cursor.execute("INSERT INTO registros (matricula, nome) VALUES (?, ?)", (matricula, nome))
            conn.commit()
            label_resultado.config(text="Aluno Cadastrado com Sucesso!!!")

            # Mostrar todos os alunos no console
            cursor.execute("SELECT * FROM registros")
            print("\nLista atual de alunos:")
            for m, n in cursor.fetchall():
                print(f"Matrícula: {m}, Nome: {n}")
    except Exception as e:
        label_resultado.config(text=f"Erro: {str(e)}")
    finally:
        conn.close()

# Inicializa banco
inicializar_banco()

# Interface gráfica
root = tk.Tk()
root.title("Cadastro de Alunos")

# Entrada Matrícula
tk.Label(root, text="Matrícula:").grid(row=0, column=0, padx=5, pady=5)
entry_matricula = tk.Entry(root)
entry_matricula.grid(row=0, column=1, padx=5, pady=5)

# Entrada Nome
tk.Label(root, text="Nome do Aluno:").grid(row=1, column=0, padx=5, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

# Botão
btn_incluir = tk.Button(root, text="Incluir Aluno", command=incluir_aluno)
btn_incluir.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Resultado
label_resultado = tk.Label(root, text="")
label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

# Loop da interface
root.mainloop()
