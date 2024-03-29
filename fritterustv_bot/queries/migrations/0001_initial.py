# Generated by Django 3.2.24 on 2024-02-22 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.FileField(upload_to='media/', verbose_name='Картинка')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
            },
        ),
        migrations.CreateModel(
            name='QueryAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(max_length=255, verbose_name='Шаблон ответа')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queries.query', verbose_name='Запрос')),
            ],
            options={
                'verbose_name': 'Ответ на запрос',
                'verbose_name_plural': 'Ответы на запрос',
            },
        ),
    ]
