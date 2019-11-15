from model.kontakt import kontakt

def test_delete_kontakt(app):
    if app.kontakt.count_kontakt() == 0:
        app.kontakt.create_kontakt(kontakt(username="11",
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
