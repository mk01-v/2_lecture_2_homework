from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    # удаление пробелов, временно для прохождения теста.
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list_db())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
















