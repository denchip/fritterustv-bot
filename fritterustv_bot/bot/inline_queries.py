from telegram import InlineQueryResultArticle, Update, InputTextMessageContent
from fritterustv_bot.queries.models import Query, QueryAnswer
from fritterustv_bot.core.utils import format_string
from uuid import uuid4
import random


def inline_query(update: Update, context) -> None:
    query_text = update.inline_query.query
    queries = Query.objects.all()
    results = []
    for query in queries:
        answer = random.choices(list(QueryAnswer.objects.filter(query=query)))[0]
        if query_text:
            answer_text = format_string(answer.pattern, query_text)
            answer_title = format_string(query.title_pattern, query_text)
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
