# Generated by Django 3.2.24 on 2024-02-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0003_alter_query_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='title_pattern',
            field=models.CharField(default='', max_length=255, verbose_name='Шаблон заголовка (текст запроса помечается как {text})'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='query',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок (если запрос без текста)'),
        ),
    ]
