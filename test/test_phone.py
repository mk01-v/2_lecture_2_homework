

def test_phones_on_home_page(app):
    kontakt_from_home_page = app.kontakt.get_kontakt_list()[0]
    kontakt_from_edit_page = app.kontakt.get_kontakt_info_from_edit_page(0)
    assert kontakt_from_home_page.home == kontakt_from_edit_page.home
    assert kontakt_from_home_page.mobile == kontakt_from_edit_page.mobile
    assert kontakt_from_home_page.work == kontakt_from_edit_page.work
    assert kontakt_from_home_page.fax == kontakt_from_edit_page.fax

























