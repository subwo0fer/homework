from abc import ABCMeta, abstractmethod


class Menu(metaclass=ABCMeta):

    commands = {}
    counter = -1

    #def __init__(self):
        #pass



    def __iter__(cls):
        return cls

    def __next__(cls):

        if cls.counter + 1 < len(list(cls.commands)):
            cls.counter += 1
            return (list(cls.commands)[cls.counter], cls.commands.get(list(cls.commands)[cls.counter]))
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

    @classmethod
    def execute(cls, name, *args, **kwargs):
        if name not in cls.commands:
            raise CommandException(
                'Command with name "{}" not found'.format(name)
            )
        klass = cls.commands.get(name)
        return klass(*args, **kwargs).execute()

class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


class ShowCommand(Command):

    def __init__(self, task_id, *args, **kwargs):
        self.task_id = task_id
        self.args = args
        self.kwargs = kwargs
    def execute(self):
        pass #print(self.task_id, self.args, self.kwargs)


class ListCommand(Command):
    pass

class AddTaskCommand(Command):
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

    menu.add_command('show', ShowCommand)
    menu.add_command('list', ListCommand)
    menu.add_command('add_task', AddTaskCommand)
    menu.execute('show', 1, 2, 3, 4, 5, ads='asd', sdfsd='asd')
    #menu.execute('list')
    #menu.execute('add_task')

    #menu.execute('unknown')

    #print(menu.__next__())
    #print(menu.__next__())
    #print(menu.__next__())


    #for item in menu:
        #print(item)

    for name, command in menu:
        print(name, command)
