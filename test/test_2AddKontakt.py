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




