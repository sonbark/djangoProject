from django.db import models
from django.urls import reverse


class Recipes(models.Model):
    title = models.CharField(verbose_name='Название блюда',
                             max_length=100)
    products = models.ManyToManyField('Products', verbose_name='Продукты',
                                      null=False)
    recipe = models.TextField(verbose_name='Рецепт', blank=True)
    calories = models.CharField(verbose_name='Калорийность',
                                max_length=10)
    time = models.CharField(verbose_name='Время приготовления, мин',
                            max_length=4)
    photo = models.ImageField(verbose_name='Изображения',
                              upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(verbose_name='Публиковать',
                                       default=True)

    def get_absolute_url(self):
        return reverse('news_view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['title']


class Products(models.Model):
    name = models.CharField(verbose_name='Продукт', max_length=50)

    def get_absolute_url(self):
        return reverse('news_view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
