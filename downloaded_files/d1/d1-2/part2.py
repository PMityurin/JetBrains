# shop_scraper.py
import random
from asyncio import sleep
import requests
from bs4 import BeautifulSoup
import time


headers = {
    'Accapt': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

def search(list_pokupok):
    for product in list_pokupok:
        url = f'https://dixy.ru/catalog/search.php?q={product}'


        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('div', class_='dixyCatalogItem')
        if items:
            with open(f'data/{product}.txt', 'w', encoding='utf-8') as file:

                for n, i in enumerate(items, start=1):
                    itemName = i.find('div', class_='dixyCatalogItem__title').text.strip()
                    itemPrice = i.find('p').text.strip()
                    print(f'{n}:  {itemPrice} за {itemName}')
                    print('***')
                    file.write(f'{n}:  {itemPrice} за {itemName}\n')
        else:
            print(f'{product} - None')
        # sleep(random.randrange(2, 8))
want_to_byu = ['сыр', 'булка', 'фарш']
search(want_to_byu)
