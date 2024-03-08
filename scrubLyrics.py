from re import sub
from urllib import request
from html import unescape
from functions import find_all

# url = "https://genius.com/Yoasobi-yuusha-lyrics"
# # url = "https://genius.com/Chinese-man-Get-Up-lyrics"

def scrubLyrics(url):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = request.urlopen(req)
    htmlCode = unescape(page.read().decode("utf-8"))

    indexes = list(find_all(htmlCode, '<div data-lyrics-container="true"', '</div>')) # genius.com
    all_lyrics = ''

    for x in indexes:
        lyrics = htmlCode[x[0]:x[1]]
        all_lyrics += lyrics + "\n"

    all_lyrics = all_lyrics[:-1]
    all_lyrics = sub(r'<br/>', '\n', all_lyrics)
    cleaned_string = sub(r'<[^>]+>', '', all_lyrics)
    return cleaned_string