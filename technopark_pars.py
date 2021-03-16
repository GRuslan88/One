from bs4 import BeautifulSoup
from parser_main import Scraping_Base

#  URL адрес сайта
URLTECHNOPARK = 'https://tyumen.technopark.ru/igrovaya-pristavka-sony-playstation-4-1000-gb-gts-hzd-spiderman/'


class Technopark(Scraping_Base):
    """класс для парсинга сайта Технопарк"""
    source_url = URLTECHNOPARK

    def parcing_page(self):
        """Парсинг сайта

        Returns:
            data (list): данные из 3-х элементов

        """
        soup = BeautifulSoup(self.get_html_data(), 'html.parser')
        return {
            self.data_name: soup.find('h1', class_='product-card__pseudo-name').get_text(strip=True),
            self.data_link: self.source_url,
            self.data_price: soup.find('span', class_='price product-card__price').get_text(strip=True),
        }
