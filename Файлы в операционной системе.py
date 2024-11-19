import  os
import  time

file = 'Учёт товаров'

for root, dirs, files in os.walk('Учёт товаров'):
  for file in files:
    filepath = os.path.join(r'Z:\python\pythonProject26\HomeWorkPython')
    filetime = os.path.getmtime(r'Z:\python\pythonProject26\HomeWorkPython')
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(r'Z:\python\pythonProject26\HomeWorkPython')
    parent_dir = os.path.dirname(r'Z:\python\pythonProject26\HomeWorkPython')
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')