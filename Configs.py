from fake_useragent import UserAgent

URL = 'https://texnomart.uz/ru/katalog/'
HOST = 'https://texnomart.uz'


def GetUserAgent():
    UA = UserAgent()
    Headers = {
        'User-Agent': f'{UA.random}'
    }
    return Headers

