import sys

from my_diary import storage

from datetime import datetime, date, time

get_connection = lambda: storage.connect('diary.sqlite')

def action_show_tasks():
    with get_connection() as conn:
        tasks = storage.show_tasks(conn)

    template = 'Задача: {} Описание: {} Подробное описание: {} Статус: {} Время выполнения: {}'

    for task in tasks:
        print(template.format(task[0], task[1], task[2], task[3], task[4]))

def action_add_task():
    task = input('\nВведите задачу: ')
    y = int(input('\nВведите год выполнения: '))
    m = int(input('\nВведите месяц выполнения: '))
    d = int(input('\nВведите день выполнения: '))
    h = int(input('\nВведите час выполнения: '))
    task_description = input('\nВведите описание задачи: ')
    data = datetime(y, m, d, h)
    with get_connection() as conn:
        storage.add_task(conn, task, task_description, data)


def action_edit_task():

    id = input('Введите номер задачи: ')
    edited_task = input('Введите исправление задачи: ')
    with get_connection() as conn:
        storage.edit_task(conn, edited_task, id)


def action_end_task():
    done_id = int(input('Введите номер завершенной задачи: '))
    with get_connection() as conn:
        storage.end_task(conn, done_id)

def action_repeat_task():
    repeat_id = int(input('Введите номер задачи которую нужно повторить: '))
    with get_connection() as conn:
        storage.repeat_task(conn, repeat_id)

def action_delete_task():
    id = input('Введите номер задачи для удаления: ')
    with get_connection() as conn:
        storage.delete_task(conn, id)

def action_show_menu():

    print('''
1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Удалить задачу
m. Показать меню
q. Выйти
''')


def action_exit():
    sys.exit(0)


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    actions = {
        '1': action_show_tasks,
        '2': action_add_task,
        '3': action_edit_task,
        '4': action_end_task,
        '5': action_repeat_task,
        '6': action_delete_task,
        'm': action_show_menu,
        'q': action_exit,
    }

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда')
