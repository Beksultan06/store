# Generated by Django 4.2.7 on 2024-01-31 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('frist_name', models.CharField(max_length=155, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=155, verbose_name='ФИО')),
                ('company_name', models.CharField(max_length=155, verbose_name='Название компаний')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=100, verbose_name='Электронная почта')),
                ('country', models.CharField(max_length=55, verbose_name='Строна')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('state_country', models.CharField(max_length=155, verbose_name='Состояние/Строна')),
                ('postcode', models.CharField(max_length=155, verbose_name='Почтовый индекс')),
                ('order_notes', models.CharField(max_length=155, verbose_name='Примечания к заказу')),
                ('order', models.CharField(max_length=155, verbose_name='Твоя очередь')),
                ('product', models.CharField(max_length=100, verbose_name='Продукт')),
                ('total', models.CharField(max_length=155, verbose_name='Общий')),
                ('espresso_premiym', models.CharField(max_length=155, verbose_name='Количество Товара')),
                ('subtotal', models.CharField(max_length=155, verbose_name='Промежуточный итог')),
                ('total2', models.CharField(max_length=100, verbose_name='Общий')),
            ],
        ),
    ]