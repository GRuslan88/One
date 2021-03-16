from bs4 import BeautifulSoup
from parser_main import Scraping_Base

#  URL адрес сайта
URLMVIDEO = 'https://www.mvideo.ru/products/igrovaya-konsol-playstation-4-1tb-gts-hzd-spiderm-ps-3mes-40074231?cityId=CityCZ_1024'


class M_video(Scraping_Base):
    """класс для парсинга сайта Мвидео"""
    source_url = URLMVIDEO

    def parcing_page(self):
        """Парсинг сайта

        Returns:
            data (list): данные из 3-х элементов

        """
        soup = BeautifulSoup(self.get_html_data(), 'html.parser')
        return {
            self.data_name: soup.find('h1', class_='fl-h1').get_text(strip=True),
            self.data_link: self.source_url,
            self.data_price: soup.find('div', class_='fl-pdp-price__current').get_text(strip=True),
        }
