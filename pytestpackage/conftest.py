"""
This file has been modified through the entire chapter
it will not work for the earlier files
"""

import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(browser, osType):
    print("Running one time setUp")
    if browser == "firefox":
        print("Running Test on FF")
    else:
        print("Running test on Chrome")
    yield
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")