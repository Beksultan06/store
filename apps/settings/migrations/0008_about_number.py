# Generated by Django 5.0 on 2024-01-09 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_about_delete_aboutstatic'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='number',
            field=models.CharField(default=1, max_length=50, verbose_name='Статистика'),
            preserve_default=False,
        ),
    ]
