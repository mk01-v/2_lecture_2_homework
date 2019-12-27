# импорты
import random
from fixture.orm import ORMFixture
from model.kontakt import Kontakt
from model.group import Group


def test_add_kontakt_in_group(app, db):
    # план
    # предусловие контакта.
    if app.kontakt.count_kontakt() == 0:
        app.kontakt.create_kontakt(Kontakt(username="11111",
                                           #middle_name="11111",
                                           last_name="11111",
                                           #nickname="11111",
                                           #title="11111",
                                           #company="11111",
                                           address="11111"
                                           #home="11111",
                                           #mobile="11111",
                                           #work="11111",
                                           #fax="11111",
                                           #email="11111",
                                           #email2="11111",
                                           #email3="11111",
                                           #homepage="11111",

                                           #bday="28",
                                           #bmonth="July",
                                           #byear="1992",

                                           #aday="1",
                                           #amonth="January",
                                           #ayear="2000",

                                           #secondary_address2="11111",
                                           #secondary_home2="11111",
                                           #secondary_notes="11111"
                                            ))
    # предуcловие группы.
    if app.group.count() == 0:
        app.group.create(Group(name="name_123", header="header_123"))
    # получить список контактов
    old_kontakts = db.get_kontakt_list_db()
    # получить список групп
    old_groups = db.get_group_list_db()
    # выбрать случайный контакт
    take_kontakt = random.choice(old_kontakts)
    # выбрать случайную группу
    take_group = random.choice(old_groups)
    # поместить случайный выбранный контакт в группу
    app.kontakt.add_kontakt_in_group(take_kontakt.id, take_group.name)
    # переход на группу?
    #app.kontakt.go_to_group(take_group.name)
    # assert с БД
    test = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    #id_from_take_group = test.convert_groups_to_model(Group(id=take_group.id))
    #assert take_kontakt == id_from_take_group
    assert take_kontakt in test.get_kontakts_in_group(Group(id=take_group.id))
    

