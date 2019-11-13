
from model.group import group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="group_name_cool", header="group_header_cool_logo"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="", header=""))
    app.session.logout()

