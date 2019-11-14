# -*- coding: utf-8 -*-
from model.group import kontakt

def test_add_kontakt_firefox(app):

    app.kontakt.create_kontakt(kontakt(username="First_name: Artur", middle_name="Middle_name: 123", last_name="Last_name: Piroshkov", nickname="Nickname: 123",
                            title="Title: addressbook", company="Company: OOO Privet", address="Address: Michurina 3", home="Home: 3",
                            mobile="Mobile: 9232847147", work="Work: None", fax="Fax: None", email="E-mail: 123@gmail.com",
                            email2="E-mail2: 234@gmail.com", email3="E-mail3: 345@gmail.com", homepage="Homepage: None", bday="28", bmonth="July", byear="1992",
                            aday="1", amonth="January", ayear="2000", secondary_address2="Secondary-address: Michurina 10", secondary_home2="Secondary-home: 10",
                            secondary_notes="Secondary-notes: None"))


def test_add_modif_kontakt(app):

    app.kontakt.modif_kontakt(kontakt(username="Artur123123", middle_name="Middle_name: 1230000", last_name="", nickname="",
                            title="", company="", address="", home="",
                            mobile="", work="", fax="", email="",
                            email2="", email3="", homepage="", bday="10", bmonth="October", byear="1992",
                            aday="10", amonth="December", ayear="2000", secondary_address2="", secondary_home2="",
                            secondary_notes=""))



#def test_delete_kontakt(app):

#    app.kontakt.delete_kontakt()
