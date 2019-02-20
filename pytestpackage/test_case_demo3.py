"""
file name should start with test
test method name should start with test

py.test test_mod.py #run test in module
py.test somepath    # run all tests below somepath
py.test test_module.py::test_method #only run test_method in test_module

-s to print statements
-v verbose
"""

import pytest

@pytest.yield_fixture()
def setUp():
    print("running demo3 setup")
    yield
    print("Running demo3 tearDown")

def test_demo3_methodA(setUp):
    print("Running demo3 method A")

def test_demo3_methodB(setUp):
    print("Running demo3 method B")