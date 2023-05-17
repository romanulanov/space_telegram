import requests
import os
from dotenv import load_dotenv
from download_jpg_and_file_extension import *


def main():
    load_dotenv()
    if not os.path.exists('images/'):
        os.makedirs('images/')


if __name__ == '__main__':
    main()
