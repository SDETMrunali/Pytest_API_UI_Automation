import pytest

@pytest.fixture(scope="function")
def set_up():
    print(" code runs at the start of testcase")
    print("__________________________________")
    yield
    print(" code runs at the end of testcase")
    print("__________________________________")

@pytest.mark.smoke
def test_tc3(set_up):
    print("testcase3")

@pytest.mark.sanity
def test_tc4(set_up):
    print("testcase4")