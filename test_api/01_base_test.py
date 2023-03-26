import requests


def test_get_api_newfile_status_code_200():
    response = requests.get("http://127.0.0.1:8000/API/newfile/")
    assert response.status_code == 200


def test_get_api_newfile_content_type_json():
    response = requests.get("http://127.0.0.1:8000/API/newfile/")
    assert response.headers['Content-Type'] == "application/json"


def test_post_api_newfile_status_code_201():
    with open("test_api/data_test/test2.txt", "r", encoding="UTF-8") as f:
        test_text = f.read()
    response = requests.post("http://127.0.0.1:8000/API/newfile/", json={"description": test_text})
    assert response.status_code == 201


def test_post_api_newfile_content_result():
    with open("test_api/data_test/test2.txt", "r", encoding="UTF-8") as f:
        test_text = f.read()
    response = requests.post("http://127.0.0.1:8000/API/newfile/", json={"description": test_text})
    response_body = response.json()
    assert response_body["result"] == "downloaded_files/d2/Zad11.1.py | 73 matches | 100.0 %"