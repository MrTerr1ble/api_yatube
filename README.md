

# yatube_api

 yatube_api - API для социальной сети yatube.

## О проекте

yatube_api - это RESTful API, которое позволяет взаимодействовать с социальной сетью yatube. API предоставляет возможности для создания, чтения, обновления и удаления постов, комментариев и групп.

## Основные функции

* Создание, чтение, обновление и удаление постов
* Создание, чтение, обновление и удаление комментариев
* Создание, чтение, обновление и удаление групп
* Получение списка всех постов, комментариев и групп

## Технологии

* Python 3.9+
* Django 3.2+
* Django REST framework 3.12+

## Установка и запуск

1. Клонировать репозиторий: `git clone https://github.com/MrTerr1ble/api_yatube.git`
2. Перейти в папку с проектом: `cd yatube_api`
3. Установить зависимости: `pip install -r requirements.txt`
4. Выполнить миграции: `python manage.py migrate`
5. Запустить сервер: `python manage.py runserver`

## Использование API

API доступен по адресу `http://localhost:8000/`. Для взаимодействия с API необходимо использовать HTTP-запросы.

### Примеры запросов

* Получить список всех постов: `GET http://localhost:8000/posts/`
* Создать новый пост: `POST http://localhost:8000/posts/` с данными в формате JSON
* Получить информацию о конкретном посте: `GET http://localhost:8000/posts/<id>/`
