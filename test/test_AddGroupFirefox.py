
from model.group import group


def test_add_group(app):

    app.group.create(group(name="group_name_cool", header="group_header_cool_logo"))


def test_add_empty_group(app):

    app.group.create(group(name="", header=""))


