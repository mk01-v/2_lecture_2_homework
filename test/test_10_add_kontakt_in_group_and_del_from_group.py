# импорты
import random
from fixture.orm import ORMFixture
from model.kontakt import Kontakt
from model.group import Group


def test_add_kontakt_in_group(app, db):
    # план
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
    id_from_take_group = test.get_kontakts_in_group(Group(id=take_group.id))
    assert take_kontakt == id_from_take_group




