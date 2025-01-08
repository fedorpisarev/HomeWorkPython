import requests # делаем запрос на чтение страницы https://sky.pro/media/
response = requests.get('http://www.constitution.ru/symbols/anthem.htm')
print(response.text)