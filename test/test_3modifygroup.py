from model.group import Group

def test_modifgroup_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="000", header="000"))
    app.group.modify_first_group(Group(name="hhh!name"))


def test_modifgroup_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="ЙЙЙ", header="ЙЙЙ"))
    app.group.modify_first_group(Group(header="hhh10!header"))
