import pytest

@pytest.yield_fixture()
def setUp():
    print("Running conftest demo method setUp")
    yield
    print("Running conftest demo tearDown")

@pytest.yield_fixture(scope="module")
def oneTimeSetUp():
    print("Running conftest demo one time setUp")
    yield
    print("Running conftest one time tearDown")