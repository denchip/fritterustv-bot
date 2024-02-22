"""
Command handlers
https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html?highlight=CommandHandler
"""

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ConversationHandler

# Write your command handlers here


# Example: /start
def start(update, context):

    update.message.reply_text(
        text='Этот бот предназначен для уморительного времяпрепровождения в чате канала https://t.me/fritterustv'
    )
