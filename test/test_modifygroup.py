
from model.group import Group


def test_modifgroup_name(app):
    app.group.modify_first_group(Group(name="hhh1"))


def test_modifgroup_header(app):
    app.group.modify_first_group(Group(header="hhh41"))

