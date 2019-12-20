from model.group import Group
import random
import string
import os.path
import json
# для чтения опций командной строки (getopt).
# sys для получения доступа к этим опциям (sys).
import getopt
import sys

# параметризованный генератор.
# Пример из официальной документации как читать опции из командной строки.
#
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

#анализ параметров.
n = 5
f = "data/groups.json"
# как устроена переменная opts прочитанная парсером getopt.
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a
# в edit configuration - Parametrs - указываем "-n 10 -f data/test.json"
# создает 10 групп (11, т.к. + без значений) и  помещает в файл test.json.


# генератор данных.
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits # + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#Вводимые данные
testdata = [Group(name="", header="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20))
    for i in range(n)
]

# вывод данных в файл json "groups.json".
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    # записывает данные в файл тестовых данны, импорт нужен json, _dict_ дефолт настройки для преобразования данных и
    # .. и превращаем в словарь. Indent для вывода строк в столбец
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))