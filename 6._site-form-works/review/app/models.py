from django.db import models



class Product(models.Model):
    name = models.CharField('Название', max_length=50)
    img = models.FileField('Фото', upload_to='products/%Y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural ='Продукты'



class Review(models.Model):
    # author = models.ForeignKey(
    #     User,
    #     verbose_name='Автор',
    #     on_delete=models.CASCADE
    # )
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    text = models.TextField('Текст')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:50]

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        #Сортировка
        ordering = ['-create_date']

