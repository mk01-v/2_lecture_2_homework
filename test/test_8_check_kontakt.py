#Задание №14: Реализовать проверки для всех полей контакта на главной странице
#Реализовать тест, который проверяет, что для некоторого одного случайно выбранного контакта информация на главной странице
#(в таблице) соответствует информации, представленной в форме редактирования контакта (где задаются все его свойства),
#при этом проверяться должны все представленные свойства -- имя, фамилия, адрес, телефоны, адреса электронной почты.
#Для телефонов и адресов электронной почты используйте технику обратных проверок.

import re

def test_all_list_kontakt(app):
    kontakt_from_home_page = app.kontakt.get_kontakt_list()[0]
    kontakt_from_edit_page = app.kontakt.get_kontakt_info_from_edit_page(0)
    assert kontakt_from_home_page.username == kontakt_from_edit_page.username
    assert kontakt_from_home_page.last_name == kontakt_from_edit_page.last_name
    assert kontakt_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(kontakt_from_edit_page)
    assert kontakt_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(kontakt_from_edit_page)

# соединяем в 1 список
# чтобы везде не писать у kontakt.home и тд "clear(kontakt.home)" - используем map.
# применяем filter чтобы убрать строки, которые не учавствуют.
def merge_phones_like_on_home_page(kontakt):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [kontakt.home, kontakt.mobile, kontakt.work, kontakt.secondary_home2]))))

def merge_email_like_on_home_page(kontakt):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [kontakt.email, kontakt.email2, kontakt.email3]))))


    # clear, данные из формы редактирования нужно удалить, будем убирать лишние символы.
def clear(s):
    # 1 параметр что убираем, 2 на что, 3 параметр где заменять.
    return re.sub("[() -]", "", s)



