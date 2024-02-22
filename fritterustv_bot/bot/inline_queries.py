from telegram import InlineQueryResultArticle, Update, InputTextMessageContent
from fritterustv_bot.queries.models import Query, QueryAnswer
from uuid import uuid4
import random


def inline_query(update: Update, context) -> None:
    query_text = update.inline_query.query
    queries = Query.objects.all()
    results = []
    for query in queries:
        answer = random.choices(list(QueryAnswer.objects.filter(query=query)))[0]
        if query_text:
            pattern = answer.pattern
            if '{text}' in pattern:
                answer_text = pattern.replace('{text}', query_text)
            else:
                answer_text = pattern
        else:
            answer_text = answer.clean_text
        results.append(InlineQueryResultArticle(
            id=str(uuid4()),
            title=query.title,
            description=query.description,
            input_message_content=InputTextMessageContent(answer_text),
        ))
    update.inline_query.answer(results, cache_time=0)
