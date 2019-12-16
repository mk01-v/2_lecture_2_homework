Чтение данных.
f = open("C:\\Python\\NEWS.txt")
text = f.read()
text
>>>куча текста.
f. close() - если это не сделать, то могут быть траблы системные.

Запись в другой файл, W - открыть режим на запись.
f2 = open("C:\\testpy\\NEWS.txt", "w")
f2.write(text)
f2.close()