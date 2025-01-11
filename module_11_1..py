import requests # делаем запрос на чтение страницы https://www.youtube.com/results
url = 'https://www.youtube.com/results'
query = {'search_query':'куплинов'}
response = requests.get(url, params=query)

print(response.url, 'url')
print(response.text, 'text')