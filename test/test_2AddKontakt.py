from model.kontakt import kontakt

def test_add_kontakt_firefox(app):
    app.kontakt.create_kontakt(kontakt(username="First_name: Artur",
                                       middle_name="Middle_name: 123",
                                       last_name="Last_name: Piroshkov",
                                       nickname="Nickname: 123",
                                       title="Title: addressbook",
                                       company="Company: OOO Privet",
                                       address="Address: Michurina 3",
                                       home="Home: 3",
                                       mobile="Mobile: 9232847147",
                                       work="Work: None",
                                       fax="Fax: None",
                                       email="E-mail: 123@gmail.com",
                                       email2="E-mail2: 234@gmail.com",
                                       email3="E-mail3: 345@gmail.com",
                                       homepage="Homepage: None",

                                       bday="28",
                                       bmonth="July",
                                       byear="1992",

                                       aday="1",
                                       amonth="January",
                                       ayear="2000",

                                       secondary_address2="Secondary-address: Michurina 10",
                                       secondary_home2="Secondary-home: 10",
                                       secondary_notes="Secondary-notes: None"))


def test_add_kontakt_list(app):
    old_kontakts = app.kontakt.get_kontakt_list()
    Kontakt = kontakt(#username="Artur",
                      #middle_name="123",
                      last_name="Piroshkov",
                      #nickname="123",
                      #title="addressbook",
                      #company="OO Privet",
                      #address="Michurina 3",
                      #home="3",
                      #mobile="9232847147",
                      #work="work",
                      #fax="fax",
                      #email="123@gmail.com",
                      #email2="234@gmail.com",
                      #email3="345@gmail.com",
                      #homepage="homepage",
                      #
                      #bday="28",
                      #bmonth="July",
                      #byear="1992",
                      #
                      #aday="1",
                      #amonth="January",
                      #ayear="2000",
                      #
                      #secondary_address2="Michurina 1",
                      #secondary_home2="10",
                      #secondary_notes="qqq"
                      )

    app.kontakt.create_kontakt(Kontakt)
    assert len(old_kontakts) + 1 == app.kontakt.count_kontakt()
    new_kontakts = app.kontakt.get_kontakt_list()
    old_kontakts.append(Kontakt)
    assert sorted(old_kontakts, key=kontakt.id_or_max_kontakt) == sorted(new_kontakts, key=kontakt.id_or_max_kontakt)
    # Проверка что остаемся в сессии.
    app.session.logout()
#--------------------------------------------------------------------------------------------
import pytest
import random
import string
# Задание № 15 - генерация.
# генератор данных.
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits # + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_day(d):
    #numeral = random.randint(1, 28)
    return d(random.randint(1, 28))

def random_month(n):
    #numeral = random.randint(1, 28)
    return n(random.choice(['January','February','March','April', 'May', 'June', 'July',
                            'August', 'September', 'October', 'November', 'December']))

def random_year(y):
    #numeral = random.randint(1, 28)
    return y(random.choice(['January','February','March','April', 'May', 'June', 'July',
                            'August', 'September', 'October', 'November', 'December']))


#Вводимые данные
testdata = [kontakt(username="",
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

                    bday="",
                    bmonth="",
                    byear="",

                    aday="",
                    amonth="",
                    ayear="",

                    secondary_address2="",
                    secondary_home2="",
                    secondary_notes=""
)] + [
    kontakt(        username=random_string("username", 10),
                    middle_name=random_string("middlename", 10),
                    last_name=random_string("lastname", 10),
                    nickname=random_string("nickname", 10),
                    title=random_string("title", 10),
                    company=random_string("company", 10),
                    address=random_string("address", 10),
                    home=random_string("home", 10),
                    mobile=random_string("mobile", 10),
                    work=random_string("work", 10),
                    fax=random_string("fax", 10),
                    email=random_string("email", 10),
                    email2=random_string("email2", 10),
                    email3=random_string("email3", 10),
                    homepage=random_string("homepage", 10),

                    bday=,
                    bmonth=,
                    byear=,

                    aday=,
                    amonth=,
                    ayear=,

                    secondary_address2=random_string("address2", 10),
                    secondary_home2=random_string("phone2", 10),
                    secondary_notes=random_string("notes", 10))
    for i in range(5)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    #pass
    # добавляем тестовые данные
    # добаляем цикл данных
    #объявляем старый список групп.
    old_groups = app.group.get_group_list()
    # теперь строка загрузки данных не нужна.
    #group = Group(name="group_name_cool", header="group_header_cool_logo")
    app.group.create(group)
    #Проверки со слова assert. Условие выполнилось, т.к. создалась 1 группа. Сравниваем длину 2-х списков.
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Проверка что остаемся в сессии.
    #app.session.logout()





















