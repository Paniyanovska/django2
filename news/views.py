from django.shortcuts import render
from .models import Article, Category
from django.core.exceptions import ObjectDoesNotExist


def index_hendler(request):
    articles = Article.objects.all().order_by(
        '-pub_date')[:25].prefetch_related('categories')
    first_slider_articles = articles[:3]
    side_slider_articles = articles[3:7]
    first_2_article = articles[7:9]
    last_2_article = articles[9:11]
    first_2_small_article = articles[11:13]
    last_2_small_article = articles[13:15]
    one_big_article = articles[15:16]
    lower_first_2_article = articles[16:18]
    lower_last_2_article = articles[18:20]
    trading_news = articles[20:25]

    context = {
        'first_slider_articles': first_slider_articles,
        'side_slider_articles': side_slider_articles,
        'first_2_article': first_2_article,
        'last_2_article': last_2_article,
        'first_2_small_article': first_2_small_article,
        'last_2_small_article': last_2_small_article,
        'one_big_article': one_big_article,
        'lower_first_2_article': lower_first_2_article,
        'lower_last_2_article': lower_last_2_article,
        'trading_news': trading_news
    }
    return render(request, 'news/index.html', context)


def blog_hendler(request, **kwargs):
    cat_slug = kwargs.get('cat_slug')
    if cat_slug:
        category = Category.objects.get(slug=cat_slug)
        last_articles = Article.objects.filter(
            categories__slug=cat_slug).order_by(
            '-pub_date')[:13].prefetch_related('categories')
    else:
        last_articles = Article.objects.all().order_by(
            '-pub_date')[:13].prefetch_related('categories')
        category = None

    treiding_article = last_articles[:5]
    top_article = last_articles[5:]
    context = {
        'last_articles': last_articles,
        'treiding_article': treiding_article,
        'top_article': top_article,
        'category': category
    }
    return render(request, 'news/blog.html', context)


def page_hendler(request, post_slug):
    main_article = Article.objects.get(slug=post_slug)
    try:
        prev_article = Article.objects.get(id=main_article.id-1)
    except ObjectDoesNotExist:
        prev_article = None
    try:
        next_article = Article.objects.get(id=main_article.id+1)
    except ObjectDoesNotExist:
        next_article = None
    context = {
        'article': main_article,
        'prev_article': prev_article,
        'next_article': next_article
    }
    return render(request, 'news/article.html', context)


def contact_hendler(request):
    context = {}
    return render(request, 'news/contact.html', context)


def robots_hendler(request):
    context = {}
    return render(request, 'news/robots.txt', context, content_type='text/plain')
