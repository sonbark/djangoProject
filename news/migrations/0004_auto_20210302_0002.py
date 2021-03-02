# Generated by Django 3.1.6 on 2021-03-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210301_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='products',
        ),
        migrations.AddField(
            model_name='recipes',
            name='products',
            field=models.ManyToManyField(to='news.Products', verbose_name='Продукты'),
        ),
    ]
