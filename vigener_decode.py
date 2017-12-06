#!/usr/bin/env python3

import shiffr
import gift

ru_text = """
информатика
математика
физика
компьютер
процессор
оперативная память
накопитель информации
информация
операционная система
интернет
сервер
дисплей
контроллер
шина данных
драйвер
жёсткий диск
"""
en_text = """
windows
linux
operating system
firefox
internet
server
display
computer
science
computer science
controller
data bus
driver
usb bus
serial bus
com port
cpu unit
memory
hard drive
flash
"""

ru_key = """
тест
мод
пик
куча
пир
порт
"""
en_key="""
test
mod
peak
heap
peer
port
"""

def listize(text: str) -> list:
    return list(filter(lambda line: line != "", text.split("\n")))

en_text = listize(en_text)
ru_text = listize(ru_text)
en_key = listize(en_key)
ru_key = listize(ru_key)

en = [(l, k) for l in en_text for k in en_key]
ru = [(l, k) for l in ru_text for k in ru_key]

template = {"comment": "{comment}", "text": """[html]<p>Сообщение</p>
<pre>{line}</pre>
<p>было зашифровано шифром Виженера с&nbsp;ключом</p>
<pre>{key}</pre>
<p>Расшифруйте его.</p>""", "answer": "{answers}", "name": "{name}"}

result = list()

for line, key in en+ru:
    answer = line
    line = shiffr.vigener(line, key, "encode")
    answers = list()
    answers.append(answer.lower())
    if " " in answer:
        answer = "".join(answer.split())
        answers.append(answer.lower())
    answers = "\n".join(list(map(lambda a: "="+a, answers)))
    value = dict()
    value["comment"] = template["comment"].format(comment="виженер:"+line+":"+str(key))
    value["text"] = template["text"].format(line=line, key=key)
    value["answer"] = template["answer"].format(answers=answers)
    value["name"] = template["name"].format(name=value["comment"])
    result.append(value)

#print(result[5])
#print(gift.question(**result[-1]))
for question in result:
    print(gift.question(**question))
