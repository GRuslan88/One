from mvideo import Mvideo
from technopark import Technopark
from ozon import Ozon
import time

handler_list = (
    Mvideo,
    Technopark,
    Ozon,
)


def check_currency():
    """Запуск скрипта через каждые 24 часа

    """
    for handler in handler_list:
        handler().write_data()
    time.sleep(86400)
    check_currency()


check_currency()
print('aloha')
