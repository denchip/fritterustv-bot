from django.contrib.admin.apps import AdminConfig
from django.contrib import admin, auth
import django.contrib.auth.models
from python_telegram_bot_django_persistence import models


class CustomAdminSite(admin.AdminSite):
    site_header = "FritterusTV Chat bot administration"


class CustomAdminConfig(AdminConfig):
    default_site = "fritterustv_bot.core.admin.CustomAdminSite"


