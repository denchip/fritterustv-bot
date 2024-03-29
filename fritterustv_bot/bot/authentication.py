from . import models


def authenticate(chat):
    """
    Authenticating on user means:
    1. Getting the chat id.
    2. Creating the user if it doesn't exist.
    3. Updating the user info. Useful to get the latest username, first name & last name values.
    4. Reporting the date and time of the latest user action.

    This method should be called whenever you want to authenticate on user of your bot.
    """

    # anonymous
    if chat.username is not None:
        if chat.username == 'GroupAnonymousBot':
            return None, True

    # not anonymous
    user, _ = models.BotUser.objects.get_or_create(chat_id=chat['id'])

    user.chat_id = chat['id']

    # get username
    try:
        user.username = chat.username
    except Exception as e:
        user.username = None

    # get first name
    try:
        user.first_name = chat.first_name
    except Exception as e:
        user.first_name = None

    # get last name
    try:
        user.last_name = chat.last_name
    except Exception as e:
        user.last_name = None

    # get language preferences
    try:
        user.language = chat.language_code.upper()
    except Exception as e:
        user.language = None

    user.report_last_action()
    user.save()

    return user, False
