from django.db import models
from django.conf import settings

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Material(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(verbose_name='Наполнение')
    url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Раздел', related_name='category')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Cоздатель материалов',
                             related_name='user', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
