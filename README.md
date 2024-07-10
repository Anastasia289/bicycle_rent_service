backend сервиса аренды велосипедов



http://127.0.0.1:8000/api/v1/jwt/create/
{
  "email": "admin@ad.ru",
  "password": "admin"
}

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMDcwODQ5NiwiaWF0IjoxNzIwNjIyMDk2LCJqdGkiOiJmZTRlMzhkOWYxNGY0MWU1ODNjZDU5ZGU1YmU3ODk3ZiIsInVzZXJfaWQiOjF9.q3fmrrSWeSZDdqgWQUaOSmQ9lpwLI_iS7Glxg09LAig",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwNzA4NDk2LCJpYXQiOjE3MjA2MjIwOTYsImp0aSI6Ijk2Y2NlYTcyYzIwNjQ4NjE5NzJhM2YxMzdmMGJhYTIxIiwidXNlcl9pZCI6MX0.t_kgKGIE-EHZIB6vJZTg3amLJtI5CTJzvdCuxIWu36I"
}




http://127.0.0.1:8000/api/v1/users/

get 
{
    "username": "admin",
    "password": "pbkdf2_sha256$600000$GizABvzoTa5yVAIVvIW4FD$+rObqkmZT2lIXuolgEBD+1WqtSTqoJMpCFhszOm0WQs=",
    "id": 1,
    "email": "admin@ad.ru"
}


post

{
    "username": "pupkin",
    "password": "pypkinqwe",
    "email": "pupkin@pupkin.ru"
}
