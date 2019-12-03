from sys import maxsize


class kontakt:

    def __init__(self, username=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None, home=None,
                 mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None, ayear=None, secondary_address2=None, secondary_home2=None, secondary_notes=None, id=None, all_phones_from_home_page=None):
        self.username = username
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.secondary_address2 = secondary_address2
        self.secondary_home2 = secondary_home2
        self.secondary_notes = secondary_notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    #вывод содержимое объектов, а не адресов памяти. Строковое представление в консоли.
    def __repr__(self):
        return "%s:%s" % (self.id, self.last_name)

    # чтобы не сравнивал по физическому расположению, а сравнивал логически - индификаторы и имена.
    # необходимо для сравнения самих объектов.
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name

    def id_or_max_kontakt(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
