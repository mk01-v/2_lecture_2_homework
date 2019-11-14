
from model.group import group


def test_modifgroup_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(group(name="hhh1"))
    app.session.logout()

def test_modifgroup_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(group(header="hhh41"))
    app.session.logout()
