from fixture.application import Application
import pytest


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

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_Url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_Url=base_Url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_Url=base_Url)
    fixture.session.ensure_login(username="admin", password="secret")
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
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")