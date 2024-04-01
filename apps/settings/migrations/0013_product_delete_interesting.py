# Generated by Django 5.0 on 2024-01-09 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_interesting_cart_interesting_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product', verbose_name='Фото')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('context', models.CharField(max_length=255, verbose_name='Описание')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('cart', models.CharField(max_length=20, verbose_name='Корзина')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Наши продукты',
            },
        ),
        migrations.DeleteModel(
            name='Interesting',
        ),
    ]
