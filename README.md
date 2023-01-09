
Web-приложение для определения заполненных форм:
----------------

- Для сборки контейнера в корневой папке проекта ввести:

    ```bash
    docker build -t formchecker .  
    ```
- По завершению сборки, для запуска контейнера  ввести:

  ```bash
  docker run -d -p 80:80 formchecker 
  ```
- В базе данных хранится список шаблонов форм, полный список можно увидеть по ссылке:
**[http://127.0.0.1/db_all](http://127.0.0.1/db_all)**
- На вход по урлу /get_form POST запросом передаются данные такого вида:
f_name1=value1&f_name2=value2. В ответ нужно вернуть имя шаблона формы, если она была найдена.
При переходе по следующей ссылке внутри контейнера запустится тестирующий скрипт:
**[http://127.0.0.1/test](http://127.0.0.1/test)**
- Результатом работы скрипта будет спискок JSON объектов следующего типа:
  ```yaml
  {"accepted_answer":
        {"field_name_1":FIELD_TYPE,"field_name_2":FIELD_TYPE},
   "data": 
        {"field_name_1":"some data","field_name_2":"some data"},
   "result":"boolean test result"}
  ```
  - или подобным если ожидается что совпадение формы будет найдено в базе:
  ```yaml
  {"accepted_answer": 
        {"name": "Order form"}
   "data": 
       {"order_date": "valid date", 
        "client_email": "valid email",
        "order_text": 'some text',
        "field from another form": "some valid type"},
   "result":"boolean test result"}
  ```
