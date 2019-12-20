from model.group import Group
import random
import string
import os.path





# генератор данных.
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits # + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#Вводимые данные
testdata = [Group(name="", header="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")
with open(file, "w") as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__))