[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)


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

Примените миграции к базе данных:
```shell
$ make migrate
…
 ✔ Container notification-service-postgres-1  Started                                                                                                       3.4s 
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

Запустите приложение командой:

```shell
$ make run
```

## Как вести разработку
<a name="linters"></a>
### Линтеры
Для того чтобы при коммите автоматически запускались линтеры, установите [pre-commit package manager](https://pre-commit.com/).
Затем в корне репозитория запустите команду для настройки хуков:

```shell
$ pre-commit install
```
Если линтеры обнаружат проблемы в коде, коммит прервётся с сообщением об ошибке. 


Чтобы самостоятельно проверить линтером код в каталоге `/app/src/` запустите команду:

```shell
$ make lint
```

<a name="add-python-package-to-image"></a>
### Как обновить зависимости

В качестве менеджера пакетов для образа используется [Poetry](https://python-poetry.org/docs/).

Файлы Poetry `pyproject.toml` и `poetry.lock` проброшены в контейнер в виде volume, поэтому изменения 
зависимостей внутри контейнера попадают и наружу в git-репозиторий.

Например, чтобы добавить библиотеку `environs`, запустите все контейнеры, подключитесь к уже работающему 
контейнеру `app` и внутри запустите команду `poetry add environs`:

```shell
$ docker compose up -d
$ docker compose exec app bash
container:$ poetry add environs
container:$ exit
```

Конфигурационные файлы `pyproject.toml` и `poetry.lock` обновятся не только внутри контейнера, но и в репозитории 
благодаря настроенным docker volumes.
 
Не забудьте обновить докер-образ, чтобы новые контейнеры тоже получали свежий набор зависимостей:
```shell
$ docker compose build app
```
