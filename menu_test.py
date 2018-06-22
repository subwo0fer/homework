from abc import ABCMeta, abstractmethod


class Menu(object):

    commands = {}
    counter = -1

    def __init__(self):
        pass



    def __iter__(self):
        return self

    def __next__(cls):
        commands_items = cls.commands.items()
        commands_list = []
        for command in commands_items:
            commands_list.append(command)

        if cls.counter < len(commands_list) - 1:
            cls.counter += 1
            return commands_list[cls.counter]


        else:
            raise StopIteration


    @classmethod
    def add_command(cls, name, klass):

        if not name:
            raise CommandException('Command must have a name!')

        if not issubclass(klass, Command):
            raise ParamHandlerException(
                'Class "{}" is not Command!'.format(klass)
            )

        cls.commands[name] = klass


    def execute(cls, name, *args, **kwargs):
        if name not in cls.commands:
            raise CommandException(
                'Command with name "{}" not found'.format(name)
            )
        return cls.commands.get(name)(*args, **kwargs).execute(*args, **kwargs)

class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


class ShowCommand(Command):
    def __init__(self, task_id):
        self.task_id = task_id

    def execute(self, task_id):
        pass

class ListCommand(Command):
    def __init__(self):
        pass

    def execute(self):
        pass

class AddTaskCommand(Command):
    def __init__(self):
        pass

    def execute(self):
        pass


class EditTaskCommand(Command):
    pass

class TaskDoneCommand(Command):
    pass

class TaskUndoneCommand(Command):
    pass

class ExitCommand(Command):
    pass

class CommandException(Exception):
    pass


if __name__ == '__main__':
    menu = Menu()
    print(menu)
    menu.add_command('show', ShowCommand)
    menu.add_command('list', ListCommand)
    menu.add_command('add_task', AddTaskCommand)
    menu.execute('show', 1)
    menu.execute('list')
    menu.execute('add_task')

    #menu.execute('unknown')

    #print(menu.__next__())
    #print(menu.__next__())
    #print(menu.__next__())
    #print(menu.__next__())

    for name, command in menu:
        print(name, command)
