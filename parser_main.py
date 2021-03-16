#  ипорт модулей
import requests
import csv

DATA_FILE = 'base.csv'

HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.41 '
                  'YaBrowser/21.2.0.1099 Yowser/2.5 Safari/537.36',
    'cookie': 'PHPSESSID=1dep67t5q6e6k8caeag61hjuae; region=14',
    'accept-language': 'ru,en;q=0.9'
}


class Scraping_Base:
    """Базовый класс для разбора сайтов"""
    source = None
    source_url = None
    csv_column = ['Название продукта', 'Ссылка', 'Цена']

    data_name = 'name'
    data_link = 'link'
    data_price = 'price'

    data_field = {
        'Название продукта': data_name,
        'Ссылка': data_link,
        'Цена': data_price,
    }

    def __init__(self):
        """Инициализация класса для разбора страницы
        """
        self.source = self.__class__.__name__

    def parcing_page(self):
        """Разбор страницы с целью извлечения данных
        """
        raise NotImplementedError(f'Определите parcing_page в {self.__class__.__name__}')

    def get_html_data(self):
        """Получение содержимого страницы

        Returns:
            requests.models.Response: содержимое страницы
        """
        request_data = requests.get(self.source_url, headers=HEADERS)
        if request_data.status_code != 200:
            print('ERROR!!!!!')
            return ''
        return request_data.text

    def write_data(self):
        """Записать данные в файл
        """
        data = self.parcing_page()
        with open(DATA_FILE, 'a+', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';',)
            csv_writer.writerow([data['name'], data['link'], data['price']])
