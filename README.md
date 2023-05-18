В README есть примеры запуска всех скриптов
# Космический Телеграм

Программа скачивает фото с сайтов NASA и Spacex, а также размещает фото в телеграм канале с помощью бота.  

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Инструкция по настройке рабочего окружения

Для работы с переменными окружения сначала установим пакет python-dotenv:
```
pip install python-dotenv
```
Он позволяет загружать переменные окружения из файла .env в корневом каталоге приложения. Проект будет использовать функцию getenv() для поиска переменной окружения APOD_TOKEN. [Как сгенерировать APOD_TOKEN смотри здесь.](https://api.nasa.gov/) Также понадобится токен телеграм бота TG_TOKEN (см. [инструкция](https://web7.pro/kak-poluchit-token-bota-telegram-api/)). Для работы потребуется создать файл .env и задать в нём значение переменных APOD_TOKEN и TG_TOKEN, например:
    APOD_TOKEN = 66e6428d0f7
    TG_TOKEN = 613188451:ACA_8r71xAEZ5u-ue4AfU6mn1XAe3-V1F28
Для постинга фото в телеграм канал сделайте бота администратором канала и укажите в CHAT_ID адрес канала:
    CHAT_ID = @spacespacspace
Также необходимо задать переменную RATE, которая будет отвечать за частоту автоматического постинга фото, например:
    RATE = 4
будет означать, что фото в телеграм канале будут публиковаться один раз в 4 часа.
### Пример запуска проекта

Если хотите скачать фото последнего полёта Spacex напишите в окружении просто:

    python fetch_spacex_images.py
Чтобы скачать фото конкретного полёта укажите id полёта Spacex в окружении:
    
    python fetch_spacex_images.py 5eb87ce4ffd86e000604b338
Чтобы скачать 30 фото APOD с сайта Nasa напишите в окружении:

    python fetch_apod_image.py
Чтобы скачать фото Земли с сайта Nasa напишите в окружении:

    python fetch_epic_image.py
Все скаченные фотографии будут храниться в папке /images внутри проекта.
Для публикации конкретной фотографии в телеграм канале укажите в окружении имя существующего фото, например:

    python publish_photo.py spacex0.jpeg
Для автоматической публикации фото в телеграм канале напишите в окружении:

    python auto_publish.py
В случае, если фотографии в папке /images закончатся, программа перемешает фотографии и начнёт публиковать их заново.
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).