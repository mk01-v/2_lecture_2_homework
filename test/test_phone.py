import re

def test_phones_on_home_page(app):
    kontakt_from_home_page = app.kontakt.get_kontakt_list()[0]
    kontakt_from_edit_page = app.kontakt.get_kontakt_info_from_edit_page(0)
    assert kontakt_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(kontakt_from_edit_page)

# соединяем в 1 список
# чтобы везде не писать у kontakt.home и тд "clear(kontakt.home)" - используем map.
# применяем filter чтобы убрать строки, которые не учавствуют.
def merge_phones_like_on_home_page(kontakt):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [kontakt.home,kontakt.mobile,kontakt.work,kontakt.secondary_home2]))))



# тесты упадут, если не будут присутствовать данные в полях.
# тест не будут работать, т.к. убрали получение списка по отдельным телефонам.
#def test_phones_on_home_page(app):
#    kontakt_from_home_page = app.kontakt.get_kontakt_list()[0]
#    kontakt_from_edit_page = app.kontakt.get_kontakt_info_from_edit_page(0)
#    assert kontakt_from_home_page.home == clear(kontakt_from_edit_page.home)
#    assert kontakt_from_home_page.mobile == clear(kontakt_from_edit_page.mobile)
#    assert kontakt_from_home_page.work == clear(kontakt_from_edit_page.work)
#    assert kontakt_from_home_page.secondary_home2 == clear(kontakt_from_edit_page.secondary_home2)

# тесты упадут, если не будут присутствовать данные в полях.
# тест не будут работать, т.к. убрали получение списка по отдельным телефонам.
#def test_phone_on_contact_view_page(app):
#    kontakt_from_view_page = app.kontakt.get_kontakt_from_view_page(0)
#    kontakt_from_edit_page = app.kontakt.get_kontakt_info_from_edit_page(0)
#    assert kontakt_from_view_page.home == kontakt_from_edit_page.home
#    assert kontakt_from_view_page.mobile == kontakt_from_edit_page.mobile
#    assert kontakt_from_view_page.work == kontakt_from_edit_page.work
#    assert kontakt_from_view_page.secondary_home2 == kontakt_from_edit_page.secondary_home2


    # clear, данные из формы редактирования нужно удалить, будем убирать лишние символы.
def clear(s):
    # 1 параметр что убираем, 2 на что, 3 параметр где заменять.
    return re.sub("[() -]", "", s)

























