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


def test_put_positive(create):
    resp = requests.put(f'https://yougile.com/api-v2/projects/{create}',
                        headers=head,
                        json={"deleted": False, "title": "Домашка: Новое "
                        "значение", "users": {
                            '01050c0b-231a-4ee3-b7f4-22435fe483c3': 'admin'}})
    assert resp.status_code == 200


def test_put_negative(create):
    resp = requests.put(f'https://yougile.com/api-v2/projects/{create}',
                        headers=head,
                        json={"deleted": False, "title": "", "users": {
                            '01050c0b-231a-4ee3-b7f4-22435fe483c3': 'admin'}})
    assert resp.status_code == 400
