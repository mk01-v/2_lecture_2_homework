from model.kontakt import Kontakt
from random import randrange

def test_delete_kontakt(app):
    if app.kontakt.count_kontakt() == 0:
        app.kontakt.create_kontakt(Kontakt(username="11",
                                           middle_name="22",
                                           last_name="33",
                                           nickname="44",
                                           title="55",
                                           company="66",
                                           address="77",
                                           home="88",
                                           mobile="99",
                                           work="00",
                                           fax="111",
                                           email="222",
                                           email2="333",
                                           email3="444",
                                           homepage="555",

                                           bday="16",
                                           bmonth="July",
                                           byear="2008",

                                           aday="16",
                                           amonth="January",
                                           ayear="2010",

                                           secondary_address2="666",
                                           secondary_home2="777",
                                           secondary_notes="888"))
    app.kontakt.delete_kontakt()

def test_delete_kontakt_list(app):
    if app.kontakt.count_kontakt() == 0:
        app.kontakt.create_kontakt(Kontakt(#username="11",
                                           #middle_name="22",
                                           last_name="33"
                                           #nickname="44",
                                           #title="55",
                                           #company="66",
                                           #address="77",
                                           #home="88",
                                           #mobile="99",
                                           #work="00",
                                           #fax="111",
                                           #email="222",
                                           #email2="333",
                                           #email3="444",
                                           #homepage="555",

                                           #bday="16",
                                           #bmonth="July",
                                           #byear="2008",

                                           #aday="16",
                                           #amonth="January",
                                           #ayear="2010",

                                           #secondary_address2="666",
                                           #secondary_home2="777",
                                           #secondary_notes="888"
        ))
    old_kontakts = app.kontakt.get_kontakt_list()
    index = randrange(len(old_kontakts))
    app.kontakt.delete_kontakt_by_index(index)
    new_kontakts = app.kontakt.get_kontakt_list()
    assert len(old_kontakts) - 1 == len(new_kontakts)
    old_kontakts[index:index+1] = []
    assert old_kontakts == new_kontakts



