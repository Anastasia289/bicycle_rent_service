#  Сервис аренды велосипедов

## Описание:
Backend для сервиса аренды велосипедов. Пользователь может зарегистрироваться, авторизоваться, просмотреть список доступных велосипедов, арендовать понравившийся, вернуть велосипед, а также посмотреть свою историю аренды. 

## Ссылки на проект:
[Backend тут ](https://bicyclesrentservice.myddns.me/)   
[Документация к проекту тут](https://bicyclesrentservice.myddns.me/swagger/)  


##  Примеры запросов 
**Получение токена**

```
POST api/v1/jwt/create/
Request: 
{
  "email": "admin@ad.ru",
  "password": "admin"
}

``` 

**Просмотр информации о пользователе.**

```
GET api/v1/users/{id}
Response:
{
    "id": 1,
    "username": "admin",
    "email": "admin@admin.ru",
    "rented_bicycles": [
        {
            "id": 1,
            "client": 1,
            "bicycle": 2,
            "rented_at": "2024-07-12T12:37:28.832546+03:00",
            "status": "returned",
            "returned_at": "2024-07-12T13:02:59.933188+03:00",
            "final_price": 30,
            "price_per_hour": 30,
            "rented_time_in_hours": 1
        },
        {
            "id": 2,
            "client": 1,
            "bicycle": 2,
            "rented_at": "2024-07-12T13:03:33.532627+03:00",
            "status": "returned",
            "returned_at": "2024-07-12T13:03:52.726078+03:00",
            "final_price": 30,
            "price_per_hour": 30,
            "rented_time_in_hours": 1
        },
        {
            "id": 3,
            "client": 1,
            "bicycle": 2,
            "rented_at": "2024-07-12T13:06:31.568347+03:00",
            "status": "returned",
            "returned_at": "2024-07-12T13:06:35.871814+03:00",
            "final_price": 30,
            "price_per_hour": 30,
            "rented_time_in_hours": 1
        }
    ]
}
``` 

**Создание пользователя**
```
POST api/v1/users/
Request: 
{
    "username": "pup",
    "password": "pypkin!!!!",
    "email": "pup@pupk.ru"
}
Response:
{
    "username": "pupqwer",
    "email": "puqqwep@pupk.ru",
    "id": 5
}
``` 

**Получение списка доступных велосипедов**

```
GET api/v1/bicycles/
Response:
{
    "username": "pup",
    "password": "pypkin!!!!",
    "email": "pup@pupk.ru"
}
``` 

**Аренда велосипеда**
```
POST api/v1/bicycles/{id}/rent_bicycle/
``` 

**Возврат велосипеда**

```
POST api/v1/bicycles/{id}/return_bicycle/
``` 

##  Запуск проекта

### Запуск в контейнерах

1. Убедиться, что установлен Docker
2. Скопировать docker-compose.yml
3. Создать .env и заполнить по образцу .env.example
4. Запустить docker-compose.yml, выполнить миграции и собрать статику
```
docker compose up
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /static/

``` 

### Запуск без контейнеров

Клонировать репозиторий:   
 https://github.com/Anastasia289/bicycle_rent_service.git 
   
Перейти в него в командной строке:  
```cd bicycle_rent_service```  

Cоздать виртуальное окружение:   
```python -m venv venv ```  
  
Активировать виртуальное окружение:   
```source venv/scripts/activate```  
  
Установить зависимости из файла requirements.txt:  
```python -m pip install -r requirements.txt```

Выполнить миграции:   
``` python manage.py migrate```  

Запустить проект:   
```python3 manage.py runserver  ```







## Технологии: 
- Backend: Django, Django Rest Framework
- База данных: PostgreSQL
- Контейнеризация: Docker

[![My Skills](https://skillicons.dev/icons?i=py,docker,postgres,django,)](https://skillicons.dev)
