from django.db.models import Count
from .models import Article, Category


def menu_categories(request):
    cat_list = Category.objects.annotate(
        count=Count('article__id')).order_by('-count')[:5]
    return {'menu_categories': cat_list}


def footer_category(request):
    category_list = Category.objects.annotate(
        count=Count('article__id')).order_by('-count')[:20]
    return {'footer_category': category_list}


def popular_news(request):
    articles = Article.objects.all().order_by(
        '-pub_date')[:3].prefetch_related('categories')
    return {'footer_articles': articles}


def last_news(request):
    last_news = Article.objects.order_by(
        '-pub_date')[:5].prefetch_related('categories')
    return {'last_news': last_news}


def tags(request):
    top_category = Category.objects.annotate(
        count=Count('article__id')).order_by('-count')[:10]
    return {'tags': top_category}
