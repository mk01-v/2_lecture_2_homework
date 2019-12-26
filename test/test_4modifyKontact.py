from model.kontakt import Kontakt
from random import randrange
import random

#def test_modif_kontakt(app):
#    if app.kontakt.count_kontakt() == 0:
#        app.kontakt.create_kontakt(Kontakt(username="11111",
#                                           middle_name="11111",
#                                           last_name="11111",
#                                           nickname="11111",
#                                           title="11111",
#                                           company="11111",
#                                           address="11111",
#                                           home="11111",
#                                           mobile="11111",
#                                           work="11111",
#                                           fax="11111",
#                                           email="11111",
#                                           email2="11111",
#                                           email3="11111",
#                                           homepage="11111",
#
#                                           bday="28",
#                                           bmonth="July",
#                                           byear="1992",
#
#                                           aday="1",
#                                           amonth="January",
#                                           ayear="2000",
#
#                                           secondary_address2="11111",
#                                           secondary_home2="11111",
#                                           secondary_notes="11111"))
#    app.kontakt.modif_kontakt(Kontakt(username="Artur123123",
#                                      middle_name="Middle_name: 1230000",
#                                      last_name="000",
#                                      nickname="000",
#                                      title="000",
#                                      company="000",
#                                      address="000",
#                                      home="000",
#                                      mobile="000",
#                                      work="000",
#                                      fax="000",
#                                      email="000",
#                                      email2="000",
#                                      email3="000",
#                                      homepage="000",
#
#                                      bday="1",
#                                      bmonth="October",
#                                      byear="1999",
#
#                                      aday="20",
#                                      amonth="December",
#                                      ayear="1999",
#
#                                      secondary_address2="000",
#                                      secondary_home2="000",
#                                      secondary_notes="000"))
#
#def test_modif_kontakt2(app):
#    if app.kontakt.count_kontakt() == 0:
#        app.kontakt.create_kontakt(Kontakt(username="11111",
#                                           middle_name="11111",
#                                           last_name="11111",
#                                           nickname="11111",
#                                           title="11111",
#                                           company="11111",
#                                           address="11111",
#                                           home="11111",
#                                           mobile="11111",
#                                           work="11111",
#                                           fax="11111",
#                                           email="11111",
#                                           email2="11111",
#                                           email3="11111",
#                                           homepage="11111",
#
#                                           bday="28",
#                                           bmonth="July",
#                                           byear="1992",
#
#                                           aday="1",
#                                           amonth="January",
#                                           ayear="2000",
#
#                                           secondary_address2="11111",
#                                           secondary_home2="11111",
#                                           secondary_notes="11111"))
#    app.kontakt.modif_kontakt(Kontakt(username="66666",
#                                      bday="10",
#                                      bmonth="July",
#                                      byear="1992",
#
#                                      aday="1",
#                                      amonth="October",
#                                      ayear="2000"))
#
## редактирование по индексу.
#def test_modif_kontakt_list(app):
#    if app.kontakt.count_kontakt() == 0:
#        app.kontakt.create_kontakt(Kontakt(username="11111",
#                                           #middle_name="11111",
#                                           last_name="11111"
#                                           #nickname="11111",
#                                           #title="11111",
#                                           #company="11111",
#                                           #address="11111",
#                                           #home="11111",
#                                           #mobile="11111",
#                                           #work="11111",
#                                           #fax="11111",
#                                           #email="11111",
#                                           #email2="11111",
#                                           #email3="11111",
#                                           #homepage="11111",
#
#                                           #bday="28",
#                                           #bmonth="July",
#                                           #byear="1992",
#
#                                           #aday="1",
#                                           #amonth="January",
#                                           #ayear="2000",
#
#                                           #secondary_address2="11111",
#                                           #secondary_home2="11111",
#                                           #secondary_notes="11111"
#                                            ))
#    old_kontakts = app.kontakt.get_kontakt_list()
#    index = randrange(len(old_kontakts))
#    Kontakt_peremen = Kontakt(username='123123123user', last_name="123123123last_name")
#    Kontakt_peremen.id = old_kontakts[index].id
#    app.kontakt.modif_kontakt_by_index(index, Kontakt_peremen)
#    new_kontakts = app.kontakt.get_kontakt_list()
#    assert len(old_kontakts) == len(new_kontakts)
#    old_kontakts[index] = Kontakt_peremen
#    assert sorted(old_kontakts, key=Kontakt.id_or_max_kontakt) == sorted(new_kontakts, key=Kontakt.id_or_max_kontakt)

# поиск по id
def test_modif_kontakt_list(app, db):
    if app.kontakt.count_kontakt() == 0:
        app.kontakt.create_kontakt(Kontakt(username="11111",
                                           #middle_name="11111",
                                           last_name="11111"
                                           #nickname="11111",
                                           #title="11111",
                                           #company="11111",
                                           #address="11111",
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
    old_kontakts = db.get_kontakt_list_db()
    take_kontakt = random.choice(old_kontakts)
    Kontakt_peremen = Kontakt(username='USERS_test', last_name="LAST_NAME_test")
    Kontakt_peremen.id = take_kontakt.id
    app.kontakt.modif_kontakt_by_id(take_kontakt.id, Kontakt_peremen)
    new_kontakts = db.get_kontakt_list_db()
    old_kontakts.remove(take_kontakt)
    old_kontakts.append(Kontakt_peremen)
    assert len(old_kontakts) == len(new_kontakts)
    assert sorted(old_kontakts, key=Kontakt.id_or_max_kontakt) == sorted(new_kontakts, key=Kontakt.id_or_max_kontakt)













