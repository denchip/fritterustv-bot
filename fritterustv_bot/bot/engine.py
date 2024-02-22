"""
The bot engine.
Define all of your commands, callbacks and handlers here.
Go to `Bot` class and fill the handlers.
"""

import telegram
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    InlineQueryHandler,
    MessageHandler,
    Filters,
)
from python_telegram_bot_django_persistence.persistence import DjangoPersistence
from django.conf import settings

from . import commands, callbacks, constants, messages, inline_queries, models


class Bot(object):

    """
    Add your commands here, placing them on `commands.py`.
    """
    command_handlers = {
        'start': commands.start,
    }

    """
    Add your callback query handlers here, placing them on `callbacks.py`.
    """
    callback_query_handlers = {
        'main': callbacks.example_callback_query_handler,
    }

    """
    Add your inline query handlers here, placing them on `inline_queries.py`.
    """
    inline_query_handlers = {
        'inline_query': inline_queries.inline_query,
    }

    """
    Add your message handlers here, placing them on `messages.py`.
    """
    message_handlers = [
        (Filters.text, messages.echo)
    ]

    def __init__(self):

        token = settings.TELEGRAM_TOKEN

        self.updater = Updater(token=token, use_context=True, workers=200, persistence=DjangoPersistence())
        self.bot = telegram.Bot(token=token)

        dp = self.updater.dispatcher
        dp.add_error_handler(self.error_handler)

        # Init command handlers
        for key, value in self.command_handlers.items():
            dp.add_handler(CommandHandler(key, value))

        # Init callback query handlers
        for key, value in self.callback_query_handlers.items():
            dp.add_handler(CallbackQueryHandler(value, pattern=key))

        # Init inline query handlers
        for key, value in self.inline_query_handlers.items():
            dp.add_handler(InlineQueryHandler(value))

        # Init filters
        for message_filter, callback in self.message_handlers:
            dp.add_handler(MessageHandler(message_filter, callback))

    def error_handler(self, update, context):
        """
        You can define here what to do with the errors raised by the bot.
        In this case, we only print those errors to the logs.
        """
        try:
            raise context.error
        except telegram.TelegramError as e:
            print(e.message)

    def start(self):
        """
        Handle the traffic of your bot with polling technique or define a webhook.
        """
        self.updater.start_polling(allowed_updates=telegram.Update.ALL_TYPES)

        print('[BOT] Running at https://t.me/{}'.format(self.bot.username))
        self.updater.idle()
