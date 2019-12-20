from fixture.application import Application
import pytest
import json


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
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
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