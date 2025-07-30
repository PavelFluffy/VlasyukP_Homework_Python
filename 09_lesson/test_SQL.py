from sqlalchemy import create_engine
from sqlalchemy import text
import pytest


db_connecting = 'postgresql://postgres:123654@localhost:5432/QA'


@pytest.fixture()
def connect():
    db = create_engine(db_connecting)
    yield db
    sql_delete = text("delete from teacher where teacher_id = :teacher_id")
    db.execute(sql_delete, teacher_id=1)


def test_insert(connect):
    db = connect
    sql_insert = text('insert into teacher ("teacher_id", "email", "group_id")\
    values (:teacher_id, :email, :group_id)')
    db.execute(sql_insert, teacher_id=1, email='test123@yandex.ru',
               group_id=126)

    rows = db.execute("select* from teacher where teacher_id = 1").fetchall()
    row = rows[0]
    assert row['teacher_id'] == 1


def test_update(connect):
    db = connect
    sql_insert = text('insert into teacher ("teacher_id", "email", "group_id")\
    values (:teacher_id, :email, :group_id)')
    db.execute(sql_insert, teacher_id=1, email='test123@yandex.ru',
               group_id=126)

    sql_update = text("update teacher set email = 'update@gmail.com'\
    where teacher_id = :teacher_id")
    db.execute(sql_update, teacher_id=1)

    rows = db.execute("select* from teacher where teacher_id = 1").fetchall()
    row = rows[0]
    assert row['email'] == 'update@gmail.com'


def test_delete(connect):
    db = connect
    sql_insert = text('insert into teacher ("teacher_id", "email", "group_id")\
    values (:teacher_id, :email, :group_id)')
    db.execute(sql_insert, teacher_id=1, email='test123@yandex.ru',
               group_id=126)

    sql_delete = text("delete from teacher where teacher_id = :teacher_id")
    db.execute(sql_delete, teacher_id=1)

    row = db.execute("select* from teacher where teacher_id = 1").fetchall()
    assert len(row) == 0
