from functions import searchWeb
from scrubLyrics import scrubLyrics
from mutagen.id3 import ID3, USLT, ID3NoHeaderError

def getLyrics(file_path, change, extra):
    try:
        audio = ID3(file_path)
    except ID3NoHeaderError:
        audio = ID3()

    artista = ""
    nome = ""

    for key, value in audio.items():
            #printa na tela o nome e o artista da música respectivamente
            if key == "TIT2":
                nome = value
            if key == "TPE1":
                artista = value

    # if artista == "":
    #     a
    # if nome == "":
    #     b

    url = searchWeb(nome, artista, extra)
    lyrics = scrubLyrics(url)

    if change == True:
        print("Adicionado letras!")
        audio["USLT::   "] = USLT(encoding=3, lang='eng', desc='desc', text=lyrics)
        audio.save(file_path)

    return [lyrics, nome, artista]