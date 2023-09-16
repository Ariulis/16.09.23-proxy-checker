import os

from loguru import logger
from dotenv import load_dotenv

dotenv_path = '.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

logger.add('log/debug.log', level='DEBUG',
           format='{time} {level} {message}', rotation='10 KB', compression='zip')

PROXY_LOGIN = os.getenv('PROXY_LOGIN')
PROXY_PASSWORD = os.getenv('PROXY_PASSWORD')
PROXY_IP = os.getenv('PROXY_IP')
PROXY_PORT = os.getenv('PROXY_PORT')

URL = 'https://2ip.ru'
HEADERS = {
    "Host": "2ip.ru",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
}
PROXY = {
    'https': f'https://{PROXY_LOGIN}:{PROXY_PASSWORD}@{PROXY_IP}:{PROXY_PORT}'
}
