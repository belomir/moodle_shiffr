ifile = open("input.xml", mode='r', encoding="utf-8")
ofile = open("output.xml", mode='w', encoding="utf-8")

message = str()
key = str()

lat = "abcdefghijklmnopqrstuvwxyz"
cyr = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

for line in ifile:
    if key == "":
        ofile.write(line)
        if "<pre>" in line:
            line = line.strip("<pre>")
            line = line[:line.index('<')]
            if message == "":
                message = line
            else:
                key = line
    else:
        if "</question>" in line:
            if message[0] in lat:
                alph = lat#[lat, lat[key:]+lat[:key]]
            else:
                alph = cyr#[cyr, cyr[key:]+cyr[:key]]
            message = list(filter(lambda l: l!=' ', message))
            key = list((key*(len(message)//len(key)+1))[:len(message)])
            arrows = ['↓'for l in key if l!=' ']
            hint1 = "{message}\n{arrows}\n{key}".format(message="".join(message), arrows="".join(arrows), key="".join(key))
            arrows = ['  ↓'for l in key if l!=' ']
            hint2 = "{hint}\n{arrows}\n{key}".format(hint="".join("{:>{n}}".format(l, n=1 if l=="\n" else 3) for l in hint1), arrows="".join(arrows), key="".join("{:>3}".format(alph.index(l)) for l in key))
            ofile.write("    <hint format=\"html\"><text><![CDATA[\n")
            ofile.write("<pre>{hint}</pre>\n".format(hint=hint1))
            ofile.write("    ]]></text></hint>\n")
            key = list(map(lambda l: alph.index(l) if l in alph else ' ', list(key)))
            ofile.write("    <hint format=\"html\"><text><![CDATA[\n")
            ofile.write("<pre>{hint}</pre>\n".format(hint=hint2))
            #ofile.write("<pre>{message}\n{arrows}\n{key}</pre>\n".format(message="".join("{:3}".format(l)for l in message if l != ' '), arrows="".join('  ↓'for l in key if l!=' '), key="".join("{:3}".format(l)for l in key if l != ' ')))
            ofile.write("    ]]></text></hint>\n")
            ofile.write("    <hint format=\"html\"><text><![CDATA[\n")
            ofile.write("<pre>"+"\n".join(alph)+"</pre>\n")
            ofile.write("    ]]></text></hint>\n")
            ofile.write(line)
            message = str()
            key = str()
        else:
            ofile.write(line)

ifile.close()
ofile.close()
