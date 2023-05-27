# ConfigWork

Код содержит два класса: `InitStatusError` и `ConfigWork`.

Первый класс из вышеописанных необходим для выбрасывания исключения, если Вы вдруг не вызывали `ConfigWork().init()` функцию, необходимую для первоначальной работы с папками.

Второй класс отвечает за все основные функции работы с файлом `.ini`.


```python
from config import ConfigWork

settings = ConfigWork("config/conf.ini")
settings.init()

settings.create_config("conf", a="5", b="7")

result = settings.read_config("conf", ["a","b"])

settings.update_key("conf", a="9", b="11")

settings.remove_key("conf", ["a","b"])
```
