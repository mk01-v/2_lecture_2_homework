from model.kontakt import kontakt

def test_add_modif_kontakt(app):
    app.kontakt.modif_kontakt(kontakt(username="Artur123123", middle_name="Middle_name: 1230000", last_name="", nickname="",
                            title="", company="", address="", home="",
                            mobile="", work="", fax="", email="",
                            email2="", email3="", homepage="", bday="10", bmonth="October", byear="1992",
                            aday="10", amonth="December", ayear="2000", secondary_address2="", secondary_home2="",
                            secondary_notes=""))
