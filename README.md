# ConfigWork

Установить библиотеку можно так:
``` pip install siconfig ```

```python
from siconfig import ConfigWork

settings = ConfigWork("config/conf.ini")
settings.init_config()

# create_config(self, section: str, **pairs)
settings.create_config('config', version='1.5', api='1.2')

# get_config(self)
result = settings.get_config()

# get_key(self, key: str)
key = settings.get_key('version')

# set_key(self, key: str, value: str)
settings.set_key(key='version', value='1.4')

# remove_key(self, key: str)
settings.remove_key(key='api')
```
