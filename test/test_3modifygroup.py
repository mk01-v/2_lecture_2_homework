from model.group import Group

def test_modifgroup_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="000", header="000"))
    app.group.modify_first_group(Group(name="hhh!name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modifgroup_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="ЙЙЙ", header="ЙЙЙ"))
    app.group.modify_first_group(Group(header="hhh10!header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)