from django.contrib import admin, auth
import django.contrib.auth.models
from python_telegram_bot_django_persistence import models
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'get_full_name', 'is_superuser']
    list_filter = ['is_superuser']
    search_fields = ['username', 'first_name', 'last_name']


admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(auth.models.Group)
admin.site.unregister(models.BotData)
admin.site.unregister(models.ChatData)
admin.site.unregister(models.CallbackData)
admin.site.unregister(models.ConversationData)
admin.site.unregister(models.UserData)
