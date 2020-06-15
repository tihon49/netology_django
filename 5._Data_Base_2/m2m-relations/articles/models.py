from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название', db_index=True)
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title



class ArticleThematic(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    thematic_section = models.ForeignKey('Thematic_section', on_delete=models.CASCADE)
    isMain = models.BooleanField(default=False)



class Thematic_section(models.Model):
    name = models.CharField(max_length=35)
    articles = models.ManyToManyField(
        Article,
        through=ArticleThematic,
        related_name='sections'
    )

    def __str__(self):
        return self.name