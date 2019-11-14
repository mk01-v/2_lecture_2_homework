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
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
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
