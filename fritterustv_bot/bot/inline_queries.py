from django.utils import timezone
from telegram import InlineQueryResultArticle, Update, InputTextMessageContent

from fritterustv_bot.queries.models import Query, QueryAnswer
from fritterustv_bot.core.utils import format_string

from uuid import uuid4
import random


def inline_query(update: Update, context) -> None:
    query_text = update.inline_query.query
    print(update.inline_query)
    queries = Query.objects.all()
    results = []
    for query in queries:
        hash_string = f"{update.inline_query.from_user.id}{timezone.now().date()}"
        print(hash_string)
        unique_daily_hash = int(hash(hash_string))
        query_answers = list(QueryAnswer.objects.filter(query=query))
        if query.is_daily:
            answer = query_answers[unique_daily_hash % len(query_answers)]
        else:
            answer = random.choices(query_answers)[0]
        if query_text:
            answer_text = format_string(pattern=answer.pattern, text=query_text, unique_hash=unique_daily_hash)
            answer_title = format_string(pattern=query.title_pattern, text=query_text, unique_hash=unique_daily_hash)
        else:
            answer_text = answer.clean_text
            answer_title = query.title
        results.append(InlineQueryResultArticle(
            id=str(uuid4()),
            title=answer_title,
            description=query.description,
            input_message_content=InputTextMessageContent(answer_text),
        ))
    update.inline_query.answer(results, cache_time=0)
