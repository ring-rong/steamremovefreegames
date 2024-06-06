from bs4 import BeautifulSoup

# Открытие и чтение содержимого HTML файла
with open('steam_games.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение всех значений data-appid
app_ids = [tag['data-appid'] for tag in soup.find_all('tr', class_='app owned')]

print(app_ids)
