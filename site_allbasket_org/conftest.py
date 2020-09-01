import pytest
from new_application import New_Application


@pytest.fixture
def app(request):
    fixture = New_Application()
    request.addfinalizer(fixture.destroy)
    return fixture
