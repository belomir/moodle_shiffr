#!/usr/bin/env python3

def init():
    global alph
    alph = {
        "num": list(map(chr, range(ord('0'), ord('9')+1))),
        "lat": list(map(chr, range(ord('a'), ord('z')+1))),
        "Lat": list(map(chr, range(ord('A'), ord('Z')+1))),
        "cyr": list(map(chr, range(ord('а'), ord('я')+1))),
        "Cyr": list(map(chr, range(ord('А'), ord('Я')+1))),
    }
    alph["cyr"].insert(alph["cyr"].index('е')+1, 'ё')
    alph["Cyr"].insert(alph["Cyr"].index('Е')+1, 'Ё')

def itslist(mes: str) -> list:
    global alph
    for nam, lis in alph.items():
        if mes[0] in lis:
            return lis
    return None

def index(let: str) -> int:
    lis = itslist(let)
    return None if lis==None else lis.index(let)

def slide(mes: str, key: int = 0) -> str:
    lis = itslist(mes)
    le = len(lis)
    key %= le
    return "".join(map(lambda l: lis[(lis.index(l)+key)%le] if l in lis else l, mes))

def cesar(mes: str, key: int = 1, mode="encode") -> str:
    if mode=="encode":
        return slide(mes, key)
    else:
        return slide(mes, -key)

def vigener(mes: str, key: str, mode="encode") -> str:
    if mode=="encode":
        return "".join(map(lambda p: slide(p[0], index(p[1])), zip(mes, key*(len(mes)//len(key)+1))))
    else:
        return "".join(map(lambda p: slide(p[0], -index(p[1])), zip(mes, key*(len(mes)//len(key)+1))))

init()
#print(viginer("привет", "ши"))
#print(vigener("зщбкэы", "ши", "decode"))
#print(cesar("фхнжйч", 5, "decode"))
