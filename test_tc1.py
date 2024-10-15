import pytest
a=3
@pytest.mark.skip("dev will fix in next build")
def test_tc1():
    print("testcase1")

@pytest.mark.skipif(a>2,reason="skip if a>2")
def test_tc2():
    print("testcase2")