from django.db.models import Count
from .models import Article, Category


def top_category(request):
    category_list_20 = Category.objects.annotate(
        count=Count('article__id')).order_by('-count')[:20]
    return {'top_category': category_list_20}


def last_news(request):
    last_news = Article.objects.all().order_by(
        '-pub_date')[:5].prefetch_related('categories')
    return {'last_news': last_news}
