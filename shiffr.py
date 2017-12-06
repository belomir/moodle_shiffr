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
    if lis==None: return mes
    le = len(lis)
    key %= le
    return "".join(map(lambda l: lis[(lis.index(l)+key)%le] if l in lis else l, mes))

def cesar(mes: str, key: int = 1, mode="encode") -> str:
    return slide(mes, key * (1 if mode=="encode" else -1))

def vigener(mes: str, key: str, mode="encode") -> str:
    spaces = list()
    for i in range(mes.count(' ')):
        spaces.append(mes.index(" ", 0 if len(spaces)==0 else spaces[-1]+1))
    mes = mes.replace(' ', '')
    res = list(map(lambda p: slide(p[0], index(p[1]) * (1 if mode=="encode" else -1)), zip(mes, key*(len(mes)//len(key)+1))))
    for i in spaces:
        res.insert(i, ' ')
    return "".join(res)

init()
#print(vigener("привет тебе от всех нас", "ши"))
#print(vigener("зщбкэы ыэйэ", "ши", "decode"))
#print(vigener("зщбкэы", "ши", "decode"))
#print(cesar("фхнжйч", 5, "decode"))
