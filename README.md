## Как запустить
Склонируйте репозиторий:
```
git clone https://github.com/elnarmen/notification-service.git
cd notification-service
```

Перед запуском Docker Compose в корне репозитория создайте файл `.env` со следующими переменными:

``` bash
SECRET_KEY='some_secret_key'
DEBUG=True
POSTGRES_DB=db_name
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_password
DATABASE_URL=postgresql://db_user:db_password@postgres:5432/db_name
```
Скачайте и соберите докер-образы с помощью Docker Сompose:

```shell
$ make build
```

Примените миграции и создайте суперюзера:
```shell
$ make first_start
```

Запустите приложение командой:

```shell
$ make run
```

## В апи реализованы эндпоинты:

http://0.0.0.0:8000/docs/ - Swagger UI с подробным описанием API

https://0.0.0.0:8000/swagger.json - описание реализованных методов в json-формате 

https://0.0.0.0:8000/swagger.yaml - описание реализованных методов в yaml-формате 

http://0.0.0.0:8000/admin/ - администраторский Web UI

http://0.0.0.0:5555 - celery flower

### Clien API

http://0.0.0.0:8000/api/v1/clients/
- **POST:** создание нового клиента

http://0.0.0.0:8000/api/v1/clients/{pk}
- **PUT:** полное обновление данных клиента
- **PATCH:** частичное обновление данных клиента
- **DELETE:** удаление клиента

http://0.0.0.0:8000/api/v1/mailing/ 
- **GET:** получение списка всех рассылок
- **POST** создание новой рассылки

http://0.0.0.0:8000/api/v1/mailing/{id}
- **GET:** получение детальной информации о рассылке
- **PUT:** полное обновление данных рассылки
- **PATCH:** частичное обновление данных рассылки
- **DELETE:** удаление рассылки
<hr>

Техзадание: https://www.craft.do/s/n6OVYFVUpq0o6L

## Дополнительно выполненные задания
1. организовать тестирование написанного кода
2. подготовить docker-compose для запуска всех сервисов проекта одной командой
3. сделать так, чтобы по адресу /docs/ открывалась страница со Swagger UI и в нём отображалось описание разработанного API.
4. реализовать администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям
5. удаленный сервис может быть недоступен, долго отвечать на запросы или выдавать некорректные ответы. Необходимо организовать обработку ошибок и откладывание запросов при неуспехе для последующей повторной отправки. Задержки в работе внешнего сервиса никак не должны оказывать влияние на работу сервиса рассылок.
