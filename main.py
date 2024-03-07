import tkinter as tk
from tkinter import filedialog
from getLyrics import getLyrics

def selecionar_arquivo():
    filepath = filedialog.askopenfilename(filetypes=[("Arquivos MP3", "*.mp3")])
    if filepath:
        [lyrics, nome, artista] = getLyrics(filepath, change, extraEntry.get())
        labelNomeAutor.config(text=f"{nome} - {artista}")
        text_lyrics.config(state=tk.NORMAL)
        text_lyrics.delete('1.0', tk.END)
        text_lyrics.insert(tk.END, lyrics)
        text_lyrics.config(state=tk.DISABLED)
        scrollbar.config(command=text_lyrics.yview)

janela = tk.Tk()
janela.title("Seletor de Arquivo MP3")
janela.geometry("600x600")

labelGenius = tk.Label(janela, text="USE SOMENTE PARA ACHAR LETRAS DO SITE \"genius.com\"", wraplength=400)
labelGenius.pack(pady=[20,0])

botao_selecionar = tk.Button(janela, text="Selecione .MP3", command=selecionar_arquivo)
botao_selecionar.pack(pady=15)

labelExtra = tk.Label(janela, text="Parâmetros extras de pesquisa: ", wraplength=400, width=50)
labelExtra.pack()
extraEntry = tk.Entry(janela, width=75)
extraEntry.pack(pady=5)

labelNomeAutor = tk.Label(janela, text="", wraplength=400, width=50)
labelNomeAutor.pack()

change = tk.BooleanVar()
change.set(False)

checkbox_show_lyrics = tk.Checkbutton(janela, text="Colocar letras", var=change, width=50)
checkbox_show_lyrics.pack()

scrollbar = tk.Scrollbar(janela)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_lyrics = tk.Text(janela, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text_lyrics.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

janela.mainloop()