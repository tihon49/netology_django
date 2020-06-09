from django.db import models
from django.template.defaultfilters import slugify

"""
Что необходимо сделать:

В файле models.py нашего приложения создаем модель Phone с полями id, name, price, image, release_date, 
lte_exists и slug. Поле id - должно быть основным ключом модели.
Значение поля slug должно устанавливаться слагифицированным значением поля name.
Написать скрипт для переноса данных из csv-файла в модель Phone. Скрипт необходимо разместить в файле 
import_phones.py в методе handle(self, *args, **options)
При запросе <имя_сайта>/catalog - должна открываться страница с отображением всех телефонов.
При запросе <имя_сайта>/catalog/iphone-x - должна открываться страница с отображением информации по телефону.
В каталоге необходимо добавить возможность менять порядок отображения товаров: по названию (в алфавитном порядке) 
и по цене (по-убыванию и по-возрастанию).
"""



class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(
        max_length=20,
        default=None,
        db_index=True,)
    price = models.DecimalField(
        max_digits=7,
        decimal_places=0,)
    image = models.ImageField(upload_to=None)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)


    def get_slug(self):
        self.slug = slugify(self.name)
