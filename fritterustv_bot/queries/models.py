from django.db import models


class Query(models.Model):
    """
    Query
    """

    title = models.CharField(max_length=255, verbose_name='Заголовок (если запрос без текста)')
    title_pattern = models.CharField(max_length=255,
                                     verbose_name='Шаблон заголовка (текст запроса помечается как {text})')
    image = models.FileField(upload_to='media/', verbose_name='Картинка', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Описание')

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return f'{self.title}'


class QueryAnswer(models.Model):
    """
    Query answer
    """

    query = models.ForeignKey(Query, on_delete=models.CASCADE, verbose_name='Запрос')
    pattern = models.CharField(max_length=255, verbose_name='Шаблон ответа (текст запроса помечается как {text})')
    clean_text = models.CharField(max_length=255, verbose_name='Ответ (если запрос без текста)')

    class Meta:
        verbose_name = 'Ответ на запрос'
        verbose_name_plural = 'Ответы на запрос'

    def __str__(self):
        return f'{self.pattern}'
