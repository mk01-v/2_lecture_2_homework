from model.group import Group
import random
import string
import os.path
import jsonpickle
#import json
# для чтения опций командной строки (getopt).
# sys для получения доступа к этим опциям (sys).
import getopt
import sys

# параметризованный генератор.
# Пример из официальной документации как читать опции из командной строки.
# преобразование в комфортный вид.
# "n:f:" - кол-во генерации, в какой файл.
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

#анализ параметров.
n = 5
f = "data/kontakts.json"
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

def random_telephone(maxlen):
    symbols = string.digits
    return ([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_day():
    return str(random.randint(1,30))

def random_month():
    return str(random.choice(['January','February','March','April', 'May', 'June', 'July',
                            'August', 'September', 'October', 'November', 'December']))

def random_year():
    return str(random.choice([1900, 2019]))


#Вводимые данные
testdata = [Kontakt(username="",
                    middle_name="",
                    last_name="",
                    nickname="",
                    title="",
                    company="",
                    address="",
                    home="",
                    mobile="",
                    work="",
                    fax="",
                    email="",
                    email2="",
                    email3="",
                    homepage="",

                    bday="-",
                    bmonth="-",
                    byear="-",

                    aday="-",
                    amonth="-",
                    ayear="-",

                    secondary_address2="",
                    secondary_home2="",
                    secondary_notes=""
                    )] + [
    Kontakt(username=random_string("username", 10),
            middle_name=random_string("middlename", 10),
            last_name=random_string("lastname", 10),
            nickname=random_string("nickname", 10),
            title=random_string("title", 10),
            company=random_string("company", 10),
            address=random_string("address", 10),
            home=random_telephone(10),
            mobile=random_telephone(10),
            work=random_telephone(10),
            fax=random_telephone(10),
            email=random_string("email", 10),
            email2=random_string("email2", 10),
            email3=random_string("email3", 10),
            homepage=random_string("homepage", 10),

            bday=random_day(),
            bmonth=random_month(),
            byear=random_year(),

            aday=random_day(),
            amonth=random_month(),
            ayear=random_year(),

            secondary_address2=random_string("address2", 10),
            secondary_home2=random_telephone(10),
            secondary_notes=random_string("notes", 10))
    for i in range(n)
]

# вывод данных в файл json "kontakts.json".
# ".." переход на 2 уровня выше
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    # записывает данные в файл тестовых данных, импорт нужен json, _dict_ дефолт настройки для преобразования данных и
    # .. и превращаем в словарь. Indent для вывода строк в столбец
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    # jsonpickle - была проблема восстановить обратно объект по этим данным и заполнятся нужными свойствами. Расширение json.
    # преобразовывать произвольные объекты в формат json и обратно.
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))