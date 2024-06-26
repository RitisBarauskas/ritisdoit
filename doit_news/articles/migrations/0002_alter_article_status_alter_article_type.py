# Generated by Django 5.0.3 on 2024-03-07 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Черновик'), ('PUBLISHED', 'Опубликовано'), ('ARCHIVED', 'В архиве')], max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(choices=[('NEWS', 'Новость'), ('LONG_READ', 'Лонгрид'), ('INTERVIEW', 'Интервью')], max_length=50, verbose_name='Тип'),
        ),
    ]
