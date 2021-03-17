from mvideo import Mvideo
from technopark import Technopark
from ozon import Ozon

handler_list = (
    Mvideo,
    Technopark,
    Ozon,
)

for handler in handler_list:
    handler().write_data()

print('aloha')
