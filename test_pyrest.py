#run using below command
#pytest -s test_file.py

import pytest
num = 1

@pytest.fixture(scope="class")
def setup_class():
    print("this is set up")
    yield
    print("this is teardown")

class Testm:

    @pytest.mark.skip("this will fix in build")
    def test_tc11(self, setup_class):
        print("this is test1")

    @pytest.mark.skipif(num == 1, reason="Skipping because num is 1")
    def test_tc12(self):
        print("this is test2")

    @pytest.mark.smoke
    def test_tc13(self, setup_class):
        print("this is test3")

    @pytest.mark.sanity
    def test_tc14(self, setup_class):
        num1 = 2
        assert num != num1
