from googlesearch import search

def searchWeb(song, artist, extra):
    a = search(f"genius {artist} {song} {extra} lyrics", num_results=1)
    return next(a)

def find_all(a_str, subStart, subEnd):
    start = 0
    while True:
        start = a_str.find(subStart, start)
        end = a_str.find(subEnd, start)
        if start == -1: return
        yield [start, end]
        start += len(subStart)