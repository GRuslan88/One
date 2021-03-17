from bs4 import BeautifulSoup
from parser_main import Scraping_Base

#  URL адрес сайта
URLOZON = 'https://www.ozon.ru/context/detail/id/199743309/'


class Ozon(Scraping_Base):
    """класс для парсинга сайта Озон"""
    source_url = URLOZON

    def parcing_page(self):
        """Парсинг сайта

        Returns:
            data (list): данные из 3-х элементов

        """
        soup = BeautifulSoup(self.get_html_data(), 'html.parser')
        return {
            self.data_name: soup.find('h1', class_='b3a8').get_text(strip=True),
            self.data_link: self.source_url,
            self.data_price: soup.find('span', class_='c2h5 c2h7').get_text(strip=True),
        }
