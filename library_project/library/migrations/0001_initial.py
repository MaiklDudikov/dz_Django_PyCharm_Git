# Generated by Django 5.1.2 on 2024-12-04 17:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название книги')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('year', models.IntegerField(verbose_name='Год издания')),
                ('style', models.CharField(max_length=50, verbose_name='Стиль')),
                ('publisher', models.CharField(max_length=100, verbose_name='Издательство')),
                ('available', models.BooleanField(default=True, verbose_name='В наличии')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('join_date', models.DateField(auto_now_add=True, verbose_name='Дата приёма в библиотеку')),
                ('borrowed_books', models.ManyToManyField(blank=True, to='library.book', verbose_name='Взятые книги')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
