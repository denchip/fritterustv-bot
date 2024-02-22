from django.core.management.base import BaseCommand

from fritterustv_bot.bot.engine import Bot


class Command(BaseCommand):
    help = 'Run bot'

    def handle(self, *args, **options):
        bot = Bot()
        bot.start()
