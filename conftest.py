from fixture.application import Open_close_browser
from fixture.application import Application
import pytest

#@pytest.fixture(scope = 'session')
#@pytest.fixture()
#def app(request):
#    fixture = Application()
#    request.addfinalizer(fixture.destroy)
#   return fixture

@pytest.fixture(scope = 'session')
def ocb(request):
    fixture = Open_close_browser()
    request.addfinalizer(fixture.exit_browser)
    return fixture
