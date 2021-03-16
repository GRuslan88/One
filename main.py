from mvideo_pars import M_video
from technopark_pars import Technopark
from ozon_pars import Ozon

handler_list = (
    M_video,
    Technopark,
    Ozon,
)

for handler in handler_list:
    handler().write_data()

print('aloha')
