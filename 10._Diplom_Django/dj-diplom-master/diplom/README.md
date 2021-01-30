## Для запуска проекта необходимо:

установить необходимые библиотеки:
```commandline
pip install -r requirements.txt
```

произведем миграции
```commandline
python manage.py migrate
```

загрузить базовое наполнение магазина:
```commandline
python manage.py loaddata shop.json
```

Теперь нам доступна демо-версия интернет маназина, а так же админ пользователь:
```commandline
login: admin
password: admin
```

Команда для запуска сервера:
```commandline
python manage.py runserver
```

*Переходим на [сайт магазина](http://127.0.0.1:8000/)*

