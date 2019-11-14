
from model.group import group


def test_modifgroup_name(app):

    app.group.modify_first_group(group(name="hhh1"))


def test_modifgroup_header(app):

    app.group.modify_first_group(group(header="hhh41"))

