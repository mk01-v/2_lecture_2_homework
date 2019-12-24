from model.group import Group
from timeit import timeit

def test_group_list(app, db):
    # время выполнения 2-ух операций
    print(timeit(lambda: app.group.get_group_list(), number=1))
    #ui_list = app.group.get_group_list()
    # удаление пробелов, временно для прохождения теста.
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list_db()), number=1000))
    #db_list = map(clean, db.get_group_list_db())
    assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
















