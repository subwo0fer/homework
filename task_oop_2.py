from abc import ABCMeta, abstractmethod
import os
import pickle
import json

class ParamHandler(metaclass=ABCMeta):
    types = {}

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not ParamHandler!'.format(klass)
            )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):

        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found!'.format(ext)
            )

        return klass(source, *args, **kwargs)



class TextParamHandler(ParamHandler):

    def read(self, file_path):
        """
        Чтение из текстового файла и присвоение значений в self.params
        """
        with open(file_path) as f:
            for line in f:
                buf = line.split(':')
                one_param_key, one_param_value = buf[0], buf[1].rstrip('\n')
                self.params.update({one_param_key:one_param_value})

    def write(self, file_path):
        """
        Запись в текстовый файл параметров self.params
        """
        with open(file_path, 'w') as f:
            for line in self.params:
                f.write(str(line) + ':' + str(self.params.get(line)) + '\n')

class PickleParamHandler(ParamHandler):

    def read(self, file_path):
        """
        Чтение в формате Pickle и присвоение значений в self.params
        """
        with open(file_path, 'rb') as f:
            readed_data = pickle.load(f)
            for line in readed_data:
                self.params[line] = readed_data[line]

    def write(self, file_path):
        """
        Запись в формате Pickle параметров self.params
        """
        with open(file_path, 'wb') as f:
            pickle.dump(self.params, f)


class JsonParamHandler(ParamHandler):

    def read(self, file_path):
        """
        Чтение в формате Json и присвоение значений в self.params
        """
        with open(file_path) as f:
            readed_data = json.load(f)
            for line in readed_data:
                self.params[line] = readed_data[line]

    def write(self, file_path):
        """
        Запись в формате Json параметров self.params
        """
        with open(file_path, 'w') as f:
            json.dump(self.params, f)


class ParamHandlerException(Exception):
    pass

if __name__ == '__main__':
    ParamHandler.add_type('txt', TextParamHandler)
    ParamHandler.add_type('pickle', PickleParamHandler)
    ParamHandler.add_type('json', JsonParamHandler)

    obj_config = ParamHandler.get_instance('./config.txt')

    obj_config.add_param('v', 'k')
    obj_config.write('config.txt')
    print(obj_config.get_all_params())

    obj_config.read('config.txt')

    print(obj_config.get_all_params())
