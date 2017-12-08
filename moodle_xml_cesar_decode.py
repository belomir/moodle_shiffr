ifile = open("input.xml", mode='r', encoding="utf-8")
ofile = open("output.xml", mode='w', encoding="utf-8")

message = str()
key=0

lat = "abcdefghijklmnopqrstuvwxyz"
cyr = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

for line in ifile:
    if key == 0:
        ofile.write(line)
        if "<pre>" in line:
            line = line.strip("<pre>")
            line = line[:line.index('<')]
            if message == "":
                message = line
            else:
                key = int(line)
    else:
        if "</question>" in line:
            if message[0] in lat:
                alph = [lat, lat[-key:]+lat[:-key]]
            else:
                alph = [cyr, cyr[-key:]+cyr[:-key]]
            ofile.write("    <hint format=\"html\"><text><![CDATA[\n")
            ofile.write("<p>"+"Ключ {} это замена каждого символа на символ, стоящий в&nbsp;алфавите на {} символ{} {}.\nПри шифровании использовался ключ {}, значит дешифровать нужно ключом {}.".format(key, abs(key), "а" if abs(key) in [2,3,4] else "", "правее" if key>0 else "левее", key, -key)+"</p>\n")
            ofile.write("    ]]></text></hint>\n")
            ofile.write("    <hint format=\"html\"><text><![CDATA[\n")
            ofile.write("<p>"+"При шифровании использовался ключ {}, значит символ {} нужно обратно заменить на {}, {} на {}, {} на {} и&nbsp;т.д.".format(key, alph[0][0], alph[1][0], alph[0][10], alph[1][10], alph[0][-1], alph[1][-1])+"</p>\n")
            ofile.write("    ]]></text></hint>\n")
            ofile.write("    <hint format=\"html\"><text><![CDATA[\n")
            ofile.write("<pre>"+"\n".join(alph)+"</pre>\n")
            ofile.write("    ]]></text></hint>\n")
            ofile.write(line)
            message = str()
            key = 0
        else:
            ofile.write(line)

ifile.close()
ofile.close()
