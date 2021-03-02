# Generated by Django 3.1.6 on 2021-03-01 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210301_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='recipes',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.products', verbose_name='Продукты'),
        ),
    ]