import re

def test_phones_on_home_page(app):
    kontakt_from_home_page = app.kontakt.get_kontakt_list()[0]
    kontakt_from_edit_page = app.kontakt.get_kontakt_info_from_edit_page(0)
    assert kontakt_from_home_page.home == clear(kontakt_from_edit_page.home)
    assert kontakt_from_home_page.mobile == clear(kontakt_from_edit_page.mobile)
    assert kontakt_from_home_page.work == clear(kontakt_from_edit_page.work)
    assert kontakt_from_home_page.secondary_home2 == clear(kontakt_from_edit_page.secondary_home2)

    # clear, данные из формы редактирования нужно удалить, будем убирать лишние символы.

def clear(s):
    # 1 параметр что убираем, 2 на что, 3 параметр где заменять.
    return re.sub("[() -]", "", s)

























