"""
Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой системе,
функция имеет два параметра: ссылка на файл и имя на файловой системе. В качестве примера ссылки на файл
можно использовать лицензию из ГитХаба из вашего репозитория:
https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE
"""

import requests

r = requests.get("https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE")

open("LICENSE", "wb").write(r.content)