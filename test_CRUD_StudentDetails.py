# •	WEBSITE : Web API Help Page (thetestingworldapi.com)
# CRUD Operations using Pytest(we are Providing json_body as input
# •	Add New Student
# •	Fetch Student details
# •	Update student details
# •	Delete student details
# run command for below code - pytest  -s Pytest_Project_API/Student_Management_system_Project_Pytest/test_CRUD_StudentDetails.py


import jsonpath
import json

import pytest
import requests

URL = "https://thetestingworldapi.com/"


@pytest.fixture(scope="function")
def set_json_body():
    jsofile = open("Pytest_Project_API/Student_Management_system_Project_Pytest/student_details.json", 'r')
    json_body = json.loads(jsofile.read())
    return json_body

@pytest.fixture
def set_json_for_updateAPI(test_add_new_student):
    return {
      "id": test_add_new_student,
      "first_name": "piyush",
      "middle_name": "mmtestm",
      "last_name": "gaikwad",
      "date_of_birth": "16/06/1996"
    }


@pytest.fixture
def test_add_new_student(set_json_body):
    response = requests.post(URL + "api/studentsDetails", set_json_body)
    json_res = response.json()
    print(json_res)
    id = jsonpath.jsonpath(json_res, 'id')
    student_id = str(id[0])
    return student_id


def test_fetch_new_student(test_add_new_student):
    response = requests.get(URL + "api/studentsDetails/" + test_add_new_student)
    json_res = response.json()
    print(json_res)


def test_update_student_details(test_add_new_student, set_json_for_updateAPI):
    response = requests.put(URL + "api/studentsDetails/" + test_add_new_student, set_json_for_updateAPI)
    json_res = response.json()
    print(json_res)

def test_delete_student_details(test_add_new_student):
    response = requests.delete(URL + "api/studentsDetails/" + test_add_new_student)
    json_res = response.json()
    print(json_res)