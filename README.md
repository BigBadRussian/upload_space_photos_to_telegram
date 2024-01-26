# Космические фото
Бот для телеграм, который постит в телеграм канал фотографии космоса.
Есть возможность постить указанную фотографию по выбору, либо делать посты в бесконечном цикле.
Также включены 3 скрипта по загрузке фотографий для постинга с трёх api (запуски SpaceX, [nasa apod](https://apod.nasa.gov/apod/astropix.html) и [nasa epic](https://epic.gsfc.nasa.gov/)
### Как установить
Для работы скриптов вам понадобится токен доступа к api nasa_apod и api nasa_epic.
[Вот ссылка на получение токена.](https://api.nasa.gov/#signUp)  
Создать бота в телеграм:  
@BotFather (https://t.me/BotFather)
```
/start
```
```
/newbot
```
Сохраните  токен nasa, токен вашего бота и chat_id вашего телеграм канала в .env файл:
```
NASA_TOKEN = 'ваш nasa токен'
post_space_photos_bot_token = 'токен вашего бота'
CHAT_ID = 'chat_id вашего канала'
```
Python3 должен быть уже установлен.  
Установите зависимости:
```commandline
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
### Пример запуска скриптов
Данный репо содержит несколько скриптов. Ниже приведены примеры запуска.

```commandline
python3 fetch_spaceX_images.py -l=61e048bbbe8d8b66799018d
```
Скрипт загрузит в директорию images фотографии запуска space X. Если такой директории нет, то скрипт создаст ее. Параметр -l позволяет указать id запуска, фотографии которого вам требуются.
Т.к. ответ на запрос последнего запуска не всегда содержит ссылки на фотографии, по умолчанию значение данного параметра запрашивает фото запуска id - 61eefaa89eb1064137a1bd73.  
```commandline
python3 fetch_nasa_apod_photos.py -c=5
```
Скрипт загрузит в директорию images 5 фотографий сервиса NASA Astronomy Picture Of the Day. Если такой директории нет, то скрипт создаст ее. Параметр -c позволяет указать количество фотографий. Значение по умолчанию - 5.
  
```commandline
python3 fetch_nasa_epic_photos.py
```
fetch_nasa_epic_photos.py - скрипт загружает фотографии сервиса NASA Earth Polychromatic Imaging Camera. Если такой директории нет, то скрипт создаст ее.  
```commandline
python3 bot_post_single_photo.py -n=spaceX_3.jpg
```
Скрипт отправит в ваш телеграм канал указанную фотографию. Если фотографию не указать, будет отправлена случайная фотография из папки images.
```commandline
python3 bot_post_photos_on_timer.py -t=3600
```
Скрипт запускается на неограниченное время и постит фотграфии из папки images по одной каждый час (3600 секунд), не повторяясь. Когда скрипт пройдёт все фото из папки, скрипт пойдёт на второй круг, но последоательность отправки фотографий будет также случайной.
Если параметр -t опустить, время между постами будет равно 4 часам.
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).