from model.group import Group


def test_add_group(app):
    #объявляем старый список групп.
    old_groups = app.group.get_group_list()
    group = Group(name="group_name_cool", header="group_header_cool_logo")
    app.group.create(group)
    new_groups = app.group.get_group_list()

    #Проверки со слова assert. Условие выполнилось, т.к. создалась 1 группа.
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    # Проверка что остаемся в сессии.
    app.session.logout()

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)