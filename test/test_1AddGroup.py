from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="group_name_cool", header="group_header_cool_logo"))
    # Проверка что остаемся в сессии.
    app.session.logout()

def test_add_empty_group(app):
    app.group.create(Group(name="", header=""))


