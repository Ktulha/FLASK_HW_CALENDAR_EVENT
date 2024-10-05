## FLASK_CALENDAR_EVENT

### API CRUD интерфейс для работы с событиями в календаре.

#### Модель данных :

      CalendarEvent:

      - _id: int (Уникальный идентификатор события)
      - date: str  (Дата события)
      - topic: str (Заголовок события)
      - content: str  (Текст события)

#### Ограничения значений:
    - date: str (формат 'YYYY-MM-DD', уникальные значения)
    - topic: str (Максимальная длина 30  символов)
    - content: str (Максимальная длина 2000 символов)
    -  _id: str (автоматически генерируется при создании)



#### API  интерфейс:
```
GET - получить список всех событий
    $ curl http://localhost:5000/api/v1/calendar/

POST -  создать новое событие
    curl http://localhost:5000/api/v1/calendar/ -X POST -d DATE|TOPIC|CONTENT

GET - получить  событие по id
    curl http://localhost:5000/api/v1/calendar/<id>

PUT - изменить  событие по id (ограничения на уникальность, формат и длину)
    curl http://localhost:5000/api/v1/calendar/<id> -X PUT -d  DATE|TOPIC|CONTENT

DELETE - удалить   событие по id
    curl http://localhost:5000/api/v1/calendar/<id> -X DELETE




