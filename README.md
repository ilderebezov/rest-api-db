# Тестирование Python 

Общие требования к реализации практической задаче:

Есть структура БД из трёх таблиц

Таблица 1 – Абоненты/Пользователи

id	Текущий баланс	Дата добавления	Возраст	Город проживания	Временная метка последней активности	Активный тариф
1	    0.0	        2002-01-01	    40	        Москва	            2022-01-30 15:40:11	                        1
2	    199.0	    2018-05-15	    25	        Москва	            2022-03-05 00:30:56	                        2
...	...	...	...	...	...	...
Таблица 2 – Тарифы

id	Название	Дата начала действия	Дата конца действия*	Объем минут	Объем смс	Объем трафика (мб)
1	БезПереплат	    2020-01-01	        2021-01-01	                300	        150	        1024
2	Максимум	    2021-11-15	        2030-01-01	                800	        500	        16384
...	...	...	...	...	...	...
Таблица 3 – События (Факты использования абонентами услуг)

id	Метка времени	    id абонента	Тип услуги (звонок, смс, трафик)	Объем затраченных единиц
1	2022-01-30 15:40:11	1	            Звонок	                                5
2   2022-01-30 15:40:11 1	            смс	                                    1
...	...	...	...	...

Задача. Создать REST-сервис со встраиваемой БД (Например, Датафрейм или SQLite). Сервис должен предоставлять
возможность вставки, чтения, удаления и изменения данных в этом хранилище данных. Используемый стек ничем не ограничен.


## Рабочее окружение
Для начала разработки необходимо настроить рабочее окружение. Нам понадобятся следующие системные зависимости: 
- [python](https://www.python.org/downloads/) версии 3.9 или выше
- менеджер зависимостей [poetry](https://python-poetry.org/docs/#installation) версии 1.0 или выше

Настройка окружения:
1. Настроить репозиторий
    ```shell script
    git clone ...
    ```
2. Установить зависимости. Зависимости установятся в виртуальное окружение.
    ```shell script
    poetry install
    ```

## Запуск

Подключение виртуального окружения
```shell script
poetry shell
```

Из виртуального окружения сервис запускается командой
```shell script
python main.py
```

примеры запросов:
1. запрос для вывода данных всех трех таблиц БД в адресной строке браузера ввести
        http://0.0.0.0:8080
2. добавление нового пользователя в таблицу:
    curl --header "Content-Type: application/json" --request POST --data '{"user_id":"15","balance":"24.5","data_adding":"2020-10-10","age":"50","city_of_living":"Omsk","data_last_activity":"2020-11-11","current_tariff":"1"}'  http://localhost:8080/user
3. добавление нового тарифа в таблицу:
   curl --header "Content-Type: application/json" --request POST --data '{"tariff_id":"10","tariff_name":"TARIFFFF","data_start":"2021-10-10","data_end":"2021-11-11","number_of_min":"333","number_of_sms":"444","number_of_mb":"1111"}'  http://localhost:8080/tariff
4. добавление нового события в таблицу:
   curl --header "Content-Type: application/json" --request POST --data '{"event_id":"22","time_event":"2122-10-10 14-10-10","user_id":"1","service_type":"Звонок","units_spent":"3"}' http://localhost:8080/event
5. удаление пользователя из таблицы:
   curl -d 'user_id' -X DELETE http://localhost:8080/user_del
6. удаление тарифа из таблицы:
    curl -d 'tariff_id' -X DELETE http://localhost:8080/tariff_del
7. удаление события из таблицы:
    curl -d 'event_id' -X DELETE http://localhost:8080/event_del
8. обновление данных пользователя в таблице:
   curl --header "Content-Type: application/json" --request PUT --data '{"user_id":"15","balance":"24.5","data_adding":"2020-10-10","age":"50","city_of_living":"Omsk","data_last_activity":"2020-11-11","current_tariff":"1"}'  http://localhost:8080/user_update
9. обновление данных тарифа в таблице:
   curl --header "Content-Type: application/json" --request PUT --data '{"tariff_id":"15","tariff_name":"TARIFFFF","data_start":"2021-10-10","data_end":"2021-11-11","number_of_min":"333","number_of_sms":"444","number_of_mb":"1111"}'  http://localhost:8080/tariff_update
10. обновление данных события в таблице:
    curl --header "Content-Type: application/json" --request PUT --data '{"event_id":"2","time_event":"2022-10-10 14-10-10","user_id":"1","service_type":"Звонок","units_spent":"3"}' http://localhost:8080/event_update
11. удаление данных пользователя из таблицы:
    curl -d 'user_id' -X DELETE http://localhost:8080/user_del
12. удаление тарифа из таблицы:
    curl -d 'tariff_id' -X DELETE http://localhost:8080/tariff_del
13. удаление события из таблицы:
    curl -d 'event_id' -X DELETE http://localhost:8080/event_del