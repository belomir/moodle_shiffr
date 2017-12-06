#!/usr/bin/env python3

import shiffr
import gift

text = """
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
text += """
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

lines = list(filter(lambda line: line != "", text.split("\n")))

template = {"comment": "{line}", "text": """[html]<p>Зашифруйте следующее сообщение шифром Цезаря с&nbsp;ключом {key}:</p>
<pre>{line}</pre>""", "answer": "{answers}", "name": "{name}"}

result = list()

for key in [k for k in range(-3, 4) if k != 0]:
    for line in lines:
        answer = shiffr.cesar(line, key, "encode")
        answers = list()
        answers.append(answer.lower())
        answers.append(answer.upper())
        if " " in answer:
            answer = "".join(answer.split())
            answers.append(answer.lower())
            answers.append(answer.upper())
        answers = "\n".join(list(map(lambda a: "="+a, answers)))
        value = dict()
        value["comment"] = template["comment"].format(line="цезарь:"+line+":"+str(key))
        value["text"] = template["text"].format(line=line, key=key)
        value["answer"] = template["answer"].format(answers=answers)
        value["name"] = template["name"].format(name=value["comment"])
        result.append(value)

for question in result:
    print(gift.question(**question))
