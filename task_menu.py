from abc import ABCMeta, abstractmethod


class Menu(metaclass=ABCMeta):



    def __init__(self):
        self.commands = {}
        self.counter = -1



    def __iter__(cls):
        return cls

    def __next__(self):

        if self.counter + 1 < len(list(self.commands)):
            self.counter += 1
            return (list(self.commands)[self.counter], self.commands.get(list(self.commands)[self.counter]))
        else:
            raise StopIteration



    def add_command(self, name, klass):

        if not name:
            raise CommandException('Command must have a name!')

        if not issubclass(klass, Command):
            raise ParamHandlerException(
                'Class "{}" is not Command!'.format(klass)
            )

        self.commands[name] = klass

    
    def execute(self, name, *args, **kwargs):
        if name not in self.commands:
            raise CommandException(
                'Command with name "{}" not found'.format(name)
            )
        klass = self.commands.get(name)
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
