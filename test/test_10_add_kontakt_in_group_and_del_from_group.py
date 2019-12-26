# импорты
import random


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
    # переход на группу
    app.kontakt.go_to_group(take_group.name)
    # assert с БД
