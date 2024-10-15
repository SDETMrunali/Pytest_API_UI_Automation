import json

import jsonpath
import pytest
import requests

expected = 12
ex2 = 10


# @pytest.mark.smoke
# def test_tc5():
#     print("testcase1")
#     actual = 12
#     assert actual == expected, "actual and expected not matched"
#     assert actual != ex2, "actual and expected matched"


@pytest.mark.sanity
def test_tc6():
    global id
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("Pytest_Project_API/Student_Management_system_Project_Pytest/student_details.json", 'r')
    request_json = json.loads(f.read())
    response = requests.post(api_url, params=request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])


def test_tc7():
    api_url = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(api_url)
    print(response.status_code)
    assert response.status_code == 200
