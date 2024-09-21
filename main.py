import json
import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent

# URL для сайта, с которого будем получать новости
# URL for the site to scrape news
url = 'https://www.securitylab.ru/news/'

# Заголовки для запроса. Включает различные типы принимаемого контента
# Headers for the request, including accepted content types
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'user-agent': ua.random  # Использовать можно, если необходимо случайный User-Agent
    # Uncomment above if you need to use a random User-Agent
}

# Отправляем запрос и получаем HTML контент страницы
# Send a request and retrieve HTML content of the page
response = requests.get(url, headers=headers)

# Создаем объект BeautifulSoup для парсинга страницы
# Create a BeautifulSoup object to parse the page
soup = BeautifulSoup(response.text, 'lxml')


def main():
    # Определяем количество страниц новостей
    # Determine the number of news pages
    last_page = int(soup.find('div', class_='page-picker').find('input').attrs['max'])

    # Получаем все ссылки на новости на первой странице
    # Retrieve all news links from the first page
    all_url_news = soup.find_all('a', class_='article-card')
    
    # Формируем полный URL для каждой новости
    # Form full URLs for each news item
    url_news = tuple(['https://www.securitylab.ru' + url.get('href') for url in all_url_news])

    all_data = []

    # Цикл по всем страницам новостей
    # Loop through all pages of news
    for page in range(1, last_page + 1):
        page = f'https://www.securitylab.ru/news/page1_{page}.php'
        print(page)
        
        # Извлекаем данные по каждой новости
        # Extract data from each news URL
        for url in url_news:
            all_data.append(schema_extract(url))

    # Сохраняем данные в файл JSON
    # Save the data to a JSON file
    with open("www_securitylab_ru.json", "w", encoding="utf-8") as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)
        print("Data collection completed")


def schema_extract(url):
    # Отправляем запрос на страницу новости
    # Send a request to the news page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # Выводим информацию о сборе данных с текущей новости
    # Print information about the current news data collection
    print(f"Сollecting data from the news: {url}")
    print("*" * 75)

    # Извлекаем автора, дату публикации, заголовок и описание
    # Extract the author, date, title, and description
    author = soup.find(attrs={"itemprop": "author"}).text.strip()
    date = soup.find(attrs={"itemprop": "datePublished"}).text.strip()
    title = soup.find(attrs={"itemprop": "headline"}).text.strip()
    body = soup.find(attrs={"itemprop": "description"}).text.strip()

    # Возвращаем данные в виде словаря
    # Return the data as a dictionary
    return {
        "url_news": url,
        "author": author,
        "date": date,
        "title": title,
        "body": body,
    }


if __name__ == '__main__':
    main()  # Запускаем основную функцию / Run the main function
