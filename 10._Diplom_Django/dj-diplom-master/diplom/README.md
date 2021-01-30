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

## Дизайн

* [Главная страница](https://github.com/tihon49/netology_django/blob/master/10._Diplom_Django/dj-diplom-master/diplom/shop/templates/shop/base.html).
* [Страница раздела](./resources/smartphones.html).
* [Страница незаполненного раздела](./resources/empty_section.html).
* [Страница товара](./resources/phone.html).
* [Страница корзины](./resources/cart.html).
* [Страница входа](./resources/login.html).
