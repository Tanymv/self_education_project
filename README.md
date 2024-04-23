# Дипломная работа OB1. Проект самообучения.
## Задание:
Реализовать функционал самообучения для студентов. Для этого необходимо создать платформу, которая работает только с авторизованными пользователями. На платформе необходимо предусмотреть функционал разделов и материалов. Управление всеми сущностями необходимо реализовать через стандартный Django admin. Реализовать либо Rest API, либо SSR с использованием Bootstrap. Для реализации проекта использовать фреймворк Django.
## План работы:
1) Создать проект в Django. Установить все необходимые зависимости.
2) Прописать настройки.
3) Создать приложения users и materials. Прописать модели пользователя, раздела и материала.
4) Реализовать CRUD.
5) Написать тесты на реализованный функционал.
6) Проверить работу сервиса.
7) Выложить готовый проект на GitHub.
## Описание проекта:
Авторизация осуществляется через электронную почту, предоставляя студентам удобный и безопасный доступ к обучающим ресурсам. Они могут погружаться в различные обучающие разделы в удобное для себя время, не заботясь о конфликтах с расписанием очных занятий.

В каждом из этих разделов у студентов открывается множество материалов, представленных для изучения. Этот разнообразный контент обеспечивает возможность глубокого погружения в тему и расширения знаний в свободное время.

Авторизованные пользователи, наслаждаясь своим доступом, могут также легко управлять своим профилем. Они имеют возможность редактировать или удалять свои данные, подстраивая свой профиль под собственные потребности и предпочтения. Кроме того, студенты могут изучать профили других участников, обогащая свой опыт общения и обмена знаниями.

Важно отметить, что пользователи могут активно участвовать в улучшении обучающего опыта, внося свой вклад в контент. Они имеют возможность выделять важные моменты, добавлять дополнительные материалы и удалять устаревшие или ненужные данные. Этот коллективный подход к обучению способствует развитию коллективного знания и стимулирует активное взаимодействие между участниками.
## Инструкция по запуска проекта:
В файле .env.example обязательно следует указать SECRET_KEY, а также предоставить значения для других переменных окружения, которые могут быть установлены по умолчанию. Важно помнить, что эти значения следует изменить перед запуском проекта, чтобы обеспечить безопасность.

Для установки всех необходимых зависимостей необходимо активировать виртуальное окружение, выполнив команду venv\Scripts\activate, а затем установить пакеты, перечисленные в файле requirements.txt, с помощью команды pip install -r requirements.txt.

Прежде чем начать использовать приложение, необходимо создать базу данных. Для этого следует подключиться к серверу PostgreSQL с помощью команды psql -U <ваш логин>, ввести пароль, а затем выполнить команду create database <название базы данных>;. После подтверждения создания базы данных можно выйти из интерфейса PostgreSQL, набрав команду \q.

Затем следует применить миграции к базе данных, используя команду python manage.py migrate, чтобы создать необходимые таблицы и структуру данных. После этого можно запустить сервер, выполнив команду python manage.py runserver.

Для доступа к административной панели приложения необходимо создать суперпользователя. Для этого можно воспользоваться командой python manage.py createsuperuser. По умолчанию будут использованы логин 'admin@sky.pro' и пароль '12345', но рекомендуется изменить их на более безопасные значения.
