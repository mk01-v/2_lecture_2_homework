#удаление группы.
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="qweqwe"))
    app.group.delete_first_group()



#def test_delete_first_group2(app):
#    app.group.delete_first_group()
