from celery import shared_task
from .models import Snippet
from django.db.models import Sum


@shared_task
def sum_snippets_click():
    sum_of_clicks = Snippet.objects.aggregate(Sum("number_of_clicks", default=0))
    print(sum_of_clicks)
    return sum_of_clicks