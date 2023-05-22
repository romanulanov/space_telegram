import requests
import os
from urllib.parse import urlparse, unquote


def dwnld_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_file_ext(url):
    url = urlparse(unquote(url))
    return os.path.splitext(url.path)[1]
