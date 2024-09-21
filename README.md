
# 📰 News Scraper for SecurityLab.ru

### 🛠 Description:

**News Scraper** is a Python script that scrapes the latest news from SecurityLab.ru, retrieving details such as the author, publication date, title, and description of each news post. The collected data is saved in JSON format for further analysis or processing.

---

### 🛠 Описание проекта:

**News Scraper** — это Python-скрипт для парсинга новостей с сайта SecurityLab.ru. Он собирает информацию, такую как автор, дата публикации, заголовок и описание каждой новости, и сохраняет её в формате JSON для дальнейшего анализа или обработки.

---

### 🔍 Features / Основные функции:

- Scrapes news from SecurityLab.ru.
- Extracts and stores the following information for each news post:
  - 🖋️ Author
  - 🕒 Date of publication
  - 📰 Title
  - 📝 Description
  - 🌐 URL of the news post

---

- Парсинг новостей с SecurityLab.ru.
- Извлечение и сохранение следующей информации о каждой новости:
  - 🖋️ Автор
  - 🕒 Дата публикации
  - 📰 Заголовок
  - 📝 Описание
  - 🌐 URL новости

---

### 📂 Project Structure / Структура проекта:

- `main.py` — The main script that scrapes the website and saves the data.
- `requirements.txt` — File with dependencies to install.

---

- `main.py` — Основной скрипт, который парсит сайт и сохраняет данные.
- `requirements.txt` — Файл с зависимостями для установки.

---

### 🚀 Installation and Running / Установка и запуск:

1. Clone the repository:
   ```bash
   git clone https://github.com/one-one-five/News_Scraper.git
   ```

2. Navigate to the project directory:
   ```bash
   cd News_Scraper
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python main.py
   ```

---

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/one-one-five/News_Scraper.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd News_Scraper
   ```

3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустите скрипт:
   ```bash
   python main.py
   ```

---

### 🧰 Dependencies / Зависимости:

- ![requests](https://img.shields.io/badge/requests-2.25.1-green)
- ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.9.3-blue)
- **json** — for handling JSON data.

---

- ![requests](https://img.shields.io/badge/requests-2.25.1-green)
- ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.9.3-blue)
- **json** — для работы с JSON-файлами.

---

### 🔧 How the script works / Как работает скрипт:

1. The script sends a request to SecurityLab.ru to retrieve the number of pages with news.
2. It loops through each page, collecting data from the news posts.
3. The data is saved in a JSON file.

---

1. Скрипт отправляет запрос на SecurityLab.ru, чтобы получить количество страниц с новостями.
2. Затем он проходит по каждой странице, собирая данные с новостных постов.
3. Данные сохраняются в файл JSON.

---
