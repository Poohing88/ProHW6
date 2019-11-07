import requests
from pprint import pprint
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate():
    text = input("Введите текст для перевода ")
    params = {
        'key': API_KEY,
        'text': text,
        'lang': input("Введите с какого языка на каком перевести")
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    text_out = ''.join(json_['text'])
    return text_out, response.json()['code']


def translate_request_return():
    text = input("Введите текст для перевода ")
    params = {
        'key': API_KEY,
        'text': text,
        'lang': input("Введите с какого языка на каком перевести")
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return json_


if __name__ == '__main__':
    print(translate())
