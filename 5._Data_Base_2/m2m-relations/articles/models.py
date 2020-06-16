from django.db import models



#класс статьи
class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название', db_index=True)
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField('Section', through='ArticleSection')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title



#промежуточный класс
class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной раздел')



#класс тематики
class Section(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование раздела')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name