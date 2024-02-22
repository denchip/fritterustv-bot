from django.contrib import admin

from . import models


@admin.register(models.Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(models.QueryAnswer)
class QueryAnswerAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'query')
