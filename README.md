#  Сервис аренды велосипедов

## Описание:
Здесь реализован backend для сервиса аренды велосипедов. Пользователь может зарегистрироваться, авторизоваться, просмотреть список доступных велосипедов, арендовать понравившийся, вернуть велосипед, а также посмотреть свою историю аренды. 

## Ссылки на проект:
[Backend развернут здесь ](https://bicyclesrentservice.myddns.me/)   
[Документация к проекту ](https://bicyclesrentservice.myddns.me/swagger/)  


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
    "email": "admin@ad.ru",
    "rented_bicycles": [
        {
            "id": 16,
            "client": 1,
            "bicycle": 2,
            "rented_at": "2024-07-11T00:22:17.250485+03:00",
            "status": "returned",
            "returned_at": "2024-07-11T02:10:13+03:00",
            "final_price": null,
            "price_per_hour": 100,
            "rented_time_in_hours": 2
        },
        {
            "id": 17,
            "client": 1,
            "bicycle": 2,
            "rented_at": "2024-07-11T00:23:47.204608+03:00",
            "status": "rented",
            "returned_at": null,
            "final_price": null,
            "price_per_hour": 100,
            "rented_time_in_hours": null
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



## Технологии: 
[![My Skills](https://skillicons.dev/icons?i=py,docker,postgres,django,)](https://skillicons.dev)
