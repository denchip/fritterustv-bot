"""
A renderer returns a tuple of (text, keyboard) which is sent to the user.
I advise you to follow this structure.
"""

from telegram import InlineKeyboardButton

# Write your renderers here


# Example:
def example_markup(user):

    text = 'Example text'

    keyboard = [
        [InlineKeyboardButton(text='Example button')]
    ]

    return text, keyboard
