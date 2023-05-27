from configparser import ConfigParser
from os import path, mkdir

class InitStatusError(Exception):
    def __init__(self, status):
        self.status = status

    def __str__(self):
        return f'Config init error: INIT_STATUS is {self.status}\nYou must first call the init() function'

class ConfigWork:
    # задает статус и путь к конфигу
    def __init__(self, path = 'config/config.ini'):
        self.INIT_STATUS = 0
        self.path = path

    # инициализирует, обрабатывает путь к папке
    def init(self):
        cpath = self.path.split('/')[0]
        if not path.exists(cpath):
            mkdir(cpath)
        else:
            if not path.isdir(cpath):
                mkdir(cpath)
        self.INIT_STATUS = 1

    # проверяет статус инициализации
    def check_init(self):
        if self.INIT_STATUS == 0:
            raise InitStatusError(self.INIT_STATUS)

    # создает конфиг с указанными параметрами
    def create_config(self, section_name: str, **kwargs):
        self.check_init()
        config = ConfigParser()
        config.add_section(section_name)
        for key, value in kwargs.items():
            config.set(section_name, key, value)

        with open(self.path, 'w') as config_file:
            config.write(config_file)
            config_file.close()

    # читает значения по ключам
    def read_config(self, section_name: str, read_keys: list):
        self.check_init()
        config = ConfigParser()
        config.read(self.path)
        result = []
        for key in read_keys:
            result.append(config.get(section_name, key))

        return result

    # изменяет уже существующие значения
    def update_key(self, section_name: str, **kwargs):
        self.check_init()
        config = ConfigParser()
        config.read(self.path)
        for key, nvalue in kwargs.items():
            config.set(section_name, key, nvalue)

        with open(self.path, 'w') as config_file:
            config.write(config_file)
            config_file.close()

    # удаляет пару ключ=значение из конфига
    def remove_key(self, section_name: str, remove_keys: list):
        self.check_init()
        config = ConfigParser()
        config.read(self.path)
        for key in remove_keys:
            config.remove_option(section_name, key)

        with open(self.path, 'w') as config_file:
            config.write(config_file)
            config_file.close()
