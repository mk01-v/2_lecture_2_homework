
class Group:

    def __init__(self, name=None, header=None, id=None):
        self.name = name
        self.header = header
        self.id = id

    #вывод содержимое объектов, а не адресов памяти.
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    # чтобы не сравнивал по физическому расположению, а сравнивал логически - индификаторы и имена.
    # необходимо для сравнения самих объектов.
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name