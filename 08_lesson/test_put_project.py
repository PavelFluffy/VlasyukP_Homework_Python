import requests
import pytest

token = 'Вставить токен'
head = {"Authorization": token, "Content-Type": "application/json"}


@pytest.fixture()
def create():
    resp = requests.post('https://yougile.com/api-v2/projects/',
                         headers=head,
                         json={"title": "Домашка"})
    project_id = resp.json()["id"]
    yield project_id
    requests.put(f'https://yougile.com/api-v2/projects/{project_id}',
                 headers=head,
                 json={"deleted": True})


def test_put_positive(create):
    resp = requests.put(f'https://yougile.com/api-v2/projects/{create}',
                        headers=head,
                        json={"title": "Домашка: Новое значение"})
    assert resp.status_code == 200


def test_put_negative(create):
    resp = requests.put(f'https://yougile.com/api-v2/projects/{create}',
                        headers=head,
                        json={"title": ""})
    assert resp.status_code == 400
