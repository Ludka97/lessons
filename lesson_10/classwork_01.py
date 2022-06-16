"""
Создать функцию при помощи регулярных выражений для проверки, что строка является валидным телефонным номером в формате
+375 (29) 299-29-29.
"""
import logging
import re

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

def is_mobile_phone(string):
    return re.search(r"^\+\d{3}\s\(\d\d\)\s\d{3}-\d\d-\d\d", string)

if __name__ == "__main__":
    for item in ("+375 (29) 299-29-29", "+375 (29) 299-29-29"):
        assert is_mobile_phone(item) is not None

    for item in ("(29) 299-29-29", "+37529299-29-29"):
        assert is_mobile_phone(item) is None

logger.debug("All test are OK")

"""if is_mobile_phone("+375 (29) 299-29-29"):
    print("Yes")
else:
    print("No")"""