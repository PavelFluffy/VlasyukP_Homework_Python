import requests
import pytest


token = 'Вставить токен'
head = {"Authorization": token, "Content-Type": "application/json"}


@pytest.fixture()
def test_post_positive():
    resp = requests.post('https://yougile.com/api-v2/projects/',
                         headers=head,
                         json={"title": "Домашка"})
    assert resp.status_code == 201
    project_id = resp.json()["id"]
    yield project_id
    requests.put(f'https://yougile.com/api-v2/projects/{project_id}',
                 headers=head,
                 json={"deleted": True})


def test_post_negative():
    resp = requests.post('https://yougile.com/api-v2/projects/',
                         headers=head,
                         json={"title": ""})
    assert resp.status_code == 400
