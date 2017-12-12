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
            line = line[line.index('>')+1:]
            line = line[:line.index('<')]
            if message == "":
                message = line
            else:
                key = line
    else:
        if "</question>" in line:
            if message[0] in lat:
                alph = lat
            else:
                alph = cyr
            message = message.replace(' ', '')
            key_str = (key*(len(message)//len(key)+1))[:len(message)]
            hint1 = "{message}\n{key}".format(message=message, key=key_str)
            keys = [-alph.index(l) for l in key]
            hint2 = "\n".join("{}: {}".format(k, n)for k,n in zip(key, keys))
            ofile.write("    <hint format=\"html\"><text><![CDATA[\n")
            ofile.write("<pre>{hint}</pre>\n".format(hint=hint1))
            ofile.write("    ]]></text></hint>\n")
            ofile.write("    <hint format=\"html\"><text><![CDATA[\n")
            ofile.write("<pre>{hint}</pre>\n".format(hint=hint2))
            ofile.write("    ]]></text></hint>\n")
            hint3 = "     {alph}".format(alph=alph)
            for k in sorted(set(keys)):
                hint3 += "\n{key:>3}: {alph}".format(key=k,alph=alph[k:]+alph[:k])
            ofile.write("    <hint format=\"html\"><text><![CDATA[\n")
            ofile.write("<pre>{hint}</pre>\n".format(hint=hint3))
            ofile.write("    ]]></text></hint>\n")
            ofile.write(line)
            message = str()
            key = str()
        else:
            ofile.write(line)

ifile.close()
ofile.close()
