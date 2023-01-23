#Нужно написать программу, которая принимает на вход
# путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.

import requests
import os

class YaUploader:

    base_host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        filename = os.path.basename(file_path)

        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params1 = {'path': filename, 'overwrite': True}
        responce = requests.get(request_url, headers=self.get_headers(), params = params1)
        upload_url = responce.json()['href']

        responce = requests.put(upload_url, data=open(file_path, 'rb'), headers=self.get_headers())
        if responce.status_code == 201:
            print('Загрузка произошла успешно')
        else:
            print(f'Ошибка №{responce.status_code}')


if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу и его имя: ')
    TOKEN = ''
    ya = YaUploader(TOKEN)
    ya.upload(path_to_file)

