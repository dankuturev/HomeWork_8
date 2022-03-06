from pprint import pprint
import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Accept': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def _get_upload_link(self, path_to_file):
        upload_url = 'http://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path_to_file, 'owerwrite': "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        pprint(headers)
        return response.json()

    def upload_file(self, path_to_file, file_name):
        href = self._get_upload_link(path_to_file=path_to_file).get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Успешно')


if __name__ == '__main__':

    path_to_file = ''
    file_name = 'test_file.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload_file(path_to_file, file_name)
