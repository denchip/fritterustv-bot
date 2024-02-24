from django.contrib import admin

from . import models


@admin.register(models.Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(models.QueryAnswer)
class QueryAnswerAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'query')
    search_fields = ('query__title', 'pattern', 'clean_text')
