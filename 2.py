import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
download_images(query, folder_name, num_images):

    # Путь к рабочему столу пользователя
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    # Путь к папке "lab PD" на рабочем столе
    lab_pd_path = os.path.join(desktop_path, 'lab PD')

    # Установка текущей рабочей директории в "lab PD"
    os.chdir(lab_pd_path)

    # Подготовка запроса для поиска изображений на Яндекс.Картинках
    search_url = f'https://yandex.ru/images/search?text={query}&size=large&from=tabbar'

    # Добавление параметра timeout
    response = requests.get(search_url, timeout=10)

    # Парсинг HTML-страницы с результатами поиска
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img', class_='serp-item__thumb')

    # Создание папки для класса
    class_folder = os.path.join('dataset', folder_name)
    os.makedirs(class_folder, exist_ok=True)
