from abc import ABCMeta, abstractmethod

class Validator(metaclass=ABCMeta):

    types = {}

    def __init__(self, source):
        self.source = source

    @abstractmethod
    def validate(self, value):
        pass


    @classmethod
    def add_type(cls, name, klass):

        if not name:
            raise ValidatorException('Validator must have a name!')

        if not issubclass(klass, Validator):
            raise ValidatorException(
                'Class "{}" is not Validator!'.format(klass)
            )

        cls.types[name] = klass

    @classmethod
    def get_instance(cls, name):


        klass = cls.types.get(name)

        if klass is None:
            raise ValidatorException(
                'Validator with name "{}" not found'.format(name)
            )

        return klass(name)


class EMailValidator(Validator):

    def validate(self, value):

        if value.find('@') != -1:
            return True
        else:
            return False

class DateTimeValidator(Validator):

    def data_check(self, data):
        if data.find('-') != -1:
            c = data.split('-')
            if int(c[0]) in range(1, 10000) and int(c[1]) in range(1, 13) and int(c[2])in range(1, 32):
                return True
        if data.find('.') != -1:
            c = data.split('.')
            if int(c[0]) in range(1, 32) and int(c[1]) in range(1, 13) and int(c[2])in range(1, 10000):
                return True
        if data.find('/') != -1:
            c = data.split('/')
            if int(c[0]) in range(1, 32) and int(c[1]) in range(1, 13) and int(c[2])in range(1, 10000):
                return True
        return False

    def time_check(self, time):
        c = time.split(':')
        if len(c) == 3:
            if int(c[0]) in range(24) and int(c[1]) in range(61) and int(c[2]) in range(61):
                return True
        if len(c) == 2:
            if int(c[0]) in range(24) and int(c[1]) in range(61):
                return True
        return False

    def validate(self, value):

        data_lst = value.split(' ')

        if len(data_lst) == 1:
            if self.data_check(data_lst[0]):
                return True

        if len(data_lst) == 2:
            if self.data_check(data_lst[0]) and self.time_check(data_lst[1]):
                return True

        return False




class ValidatorException(Exception):
    """Класс исключений"""




Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)

if __name__ == '__main__':
    valid = Validator.get_instance('datetime')

    print(valid.validate('12345-09-01'))
    print(valid.validate('2017-13-1'))
    print(valid.validate('2017-9-32'))
    print(valid.validate('2017-09-01 25:00'))
    print(valid.validate('2017-09-01 12:61:00'))
    print(valid.validate('1.9.2017'))
    print(valid.validate('1.09.2017'))
    print(valid.validate('01.09.2017'))
    print(valid.validate('1.9.2017 12:00'))
    print(valid.validate('1.9.2017 12:00:61'))
    print(valid.validate('1/9/2017'))
    print(valid.validate('1/09/2017'))
    print(valid.validate('01/09/2017'))
    print(valid.validate('1/9/2017 12:00'))
    print(valid.validate('1/9/2017 12:00:00'))
    print(valid.validate('asdfsdaf'))
    print(valid.validate('dfgsdfg'))
    print(valid.validate('2017,09,01'))

    validator = Validator.get_instance('email')
    print('\n')
    print(validator.validate('asdas@asdas.ru'))
    print(validator.validate('asdfsdfsdaf'))
    print(validator.validate('2423twe'))
    print(validator.validate('info@itmo-it.org'))
