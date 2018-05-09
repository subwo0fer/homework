import os.path as Path
import sqlite3

SQL_INSERT_TASK = 'INSERT INTO diary (task, task_description, deadline) VALUES (?, ?, ?)'

SQL_SELECT_ALL = '''
    SELECT
        id, task, task_description, status, deadline
    FROM
        diary
'''

SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'

SQL_EDIT_TASK = '''
    UPDATE diary SET task=? WHERE id=?
'''

SQL_STATUS_DONE = '''
    UPDATE diary SET status='done' WHERE id=?
'''

SQL_STATUS_UNDONE = '''
    UPDATE diary SET status='not done' WHERE id=?
'''

SQL_DELETE_TASK = 'DELETE FROM diary WHERE id=?'

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'
    conn = sqlite3.connect(db_name)

    return conn

def initialize(conn):
    script_path = Path.join(Path.dirname(__file__), 'schema.sql')
    with conn, open(script_path) as f:
        conn.executescript(f.read())

def show_tasks(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)

        return cursor.fetchall()

def add_task(conn, task, task_description, deadline):
    if not task:
        raise RuntimeError("Task can't be empty.")
    with conn:
        cursor = conn.execute(SQL_INSERT_TASK, (task, task_description, deadline))
    #return task

def edit_task(conn, edited_task, id):

    with conn:
        cursor = conn.cursor()
        cursor.execute(SQL_EDIT_TASK, (edited_task, id,))



def end_task(conn, id):
    with conn:
        cursor = conn.cursor()
        cursor.execute(SQL_STATUS_DONE, (id,))



def repeat_task(conn, id):
    with conn:
        cursor = conn.cursor()
        cursor.execute(SQL_STATUS_UNDONE, (id,))


def delete_task(conn, id):
    with conn:
        cursor = conn.cursor()
        cursor.execute(SQL_DELETE_TASK, (id,))
