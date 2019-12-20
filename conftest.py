from fixture.application import Application
import pytest
import json
import os.path
import importlib


#Для быстрого запуска - в рамках одной сессии.
#@pytest.fixture(scope = 'session')
#Для медленного запуска, сессия создается заново при инициализации теста.
#pytest.fixture

#@pytest.fixture(scope = 'session')
#def app(request):
#    fixture = Application()
#    fixture.session.login(username="admin", password="secret")
#    def fin():
#        fixture.session.logout()
#        fixture.destroy()
#    request.addfinalizer(fin)
#    return fixture

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    # не забыть указать корень директории проекта, иначе не будет работать target.json
    # *запуск проектов* - edit configuration - working directory.
    # C:\Python\Projects\2_lecture_2_homework
    if target is None:
        # прописывание директории по-умолчанию, т.к. не цеплялся файл json к проекту.
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid:
        fixture = Application(browser=browser, base_Url=target['baseUrl'])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

# срабатывание всегда из-за autouse.
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

# Зацепка (hook). Добавляет доп. параметр. 1 параметр добавляем браузер, 2 действие - сохранить, 3 по умолчанию.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Firefox")
    parser.addoption("--target", action="store", default="target.json")

#
def pytest_genearate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str[x] for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata








