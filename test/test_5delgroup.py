from model.group import Group
# генерирует случайное целое число.
#from random import randrange
import random

#def test_delete_first_group(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test", header="qweqwe"))
#    app.group.delete_first_group()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) - 1 == len(new_groups)

#def test_delete_first_group2(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test", header="qweqwe"))
#    app.group.delete_first_group()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) - 1 == len(new_groups)
#    #Удаление 1 элемента, 2 не включается.
#    old_groups[0:1] = []
#    assert old_groups == new_groups

#def test_delete_some_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test", header="qweqwe"))
#    old_groups = app.group.get_group_list()
#    index = randrange(len(old_groups))
#    app.group.delete_group_by_index(index)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) - 1 == len(new_groups)
#    #Удаление 1 элемента, 2 не включается.
#    old_groups[index:index+1] = []
#    assert old_groups == new_groups

def test_delete_some_group(app, db):
    if len(db.get_group_list_db()) == 0:
        app.group.create(Group(name="test", header="qweqwe"))
    old_groups = db.get_group_list_db()
    group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list_db()
    assert len(old_groups) - 1 == len(new_groups)

    old_groups.remove(group)
    assert old_groups == new_groups