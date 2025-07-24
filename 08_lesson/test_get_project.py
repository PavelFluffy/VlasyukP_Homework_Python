import requests
import pytest


token = 'token'
head = {"Authorization": token, "Content-Type": "application/json"}


@pytest.fixture()
def create():
    resp = requests.post('https://yougile.com/api-v2/projects/',
                         headers=head,
                         json={"title": "Домашка", "users": {
                             '01050c0b-231a-4ee3-b7f4-22435fe483c3': 'admin'}})
    project_id = resp.json()["id"]
    yield project_id
    requests.put(f'https://yougile.com/api-v2/projects/{project_id}',
                 headers=head,
                 json={"deleted": True})


def test_get_positive(create):
    resp = requests.get(f'https://yougile.com/api-v2/projects/{create}',
                        headers=head)
    assert resp.status_code == 200


def test_get_negative():
    resp = requests.get('https://yougile.com/api-v2/projects/123',
                        headers=head)
    assert resp.status_code == 404
