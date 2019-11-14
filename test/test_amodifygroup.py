
from model.group import group


def test_modifgroup(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(group(name="hhh1", header="hhh2"))
    app.session.logout()
