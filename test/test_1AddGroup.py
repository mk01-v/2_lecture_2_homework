from model.group import Group
import pytest
#from data.add_group import testdata

# если мы не хотим импользовать генератор, а быстро проверить какие-то теории.
from data.add_group import constant as testdata


# Или другой генератор данных. (пустой name, пустой header;
#                               пустой name, заполненный header
#                               заполненный name, пустой header;
#                               заполненный name, заполненный header
# на видео оставили 1 вариант
#testdata = [
#    Group(name=name, header=header)
#    for name in ["", random_string("name", 10)]
#    for header in ["", random_string("header", 20)]
#]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    #pass
    # добавляем тестовые данные
    # добаляем цикл данных
    #объявляем старый список групп.
    old_groups = app.group.get_group_list()
    # теперь строка загрузки данных не нужна.
    #group = Group(name="group_name_cool", header="group_header_cool_logo")
    app.group.create(group)
    #Проверки со слова assert. Условие выполнилось, т.к. создалась 1 группа. Сравниваем длину 2-х списков.
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Проверка что остаемся в сессии.
    #app.session.logout()


#def test_add_group(app):
#    #объявляем старый список групп.
#    old_groups = app.group.get_group_list()
#    group = Group(name="group_name_cool", header="group_header_cool_logo")
#    app.group.create(group)
#
#    #Проверки со слова assert. Условие выполнилось, т.к. создалась 1 группа. Сравниваем длину 2-х списков.
#    assert len(old_groups) + 1 == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups.append(group)
#
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
#    # Проверка что остаемся в сессии.
#    app.session.logout()

#def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="")
#    app.group.create(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)