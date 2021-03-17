from mvideo import M_video
from technopark import Technopark
from ozon import Ozon

handler_list = (
    M_video,
    Technopark,
    Ozon,
)

for handler in handler_list:
    handler().write_data()

print('aloha')
