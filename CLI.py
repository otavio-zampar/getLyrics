from getLyrics import getLyrics
from googlesearch import search

# for x in search("genius" + "YOASOBI Yuusha romanized" + "lyrics"):
#     print(x)

for x in getLyrics("./a.mp3", False, "YOASOBI Yuusha"):
    print(x)