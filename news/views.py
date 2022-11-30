from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from .models import Article, Category, Comment
from .forms import CommentForm


def index_hendler(request):
    articles = Article.objects.all().order_by(
        '-pub_date')[:20].prefetch_related('categories')

    context = {
        'articles': articles,
    }
    return render(request, 'news/index.html', context)


def blog_hendler(request, **kwargs):
    cat_slug = kwargs.get('cat_slug')
    curent_page = int(request.GET.get('page', 1))
    articles_on_page = 8

    if cat_slug:
        category = Category.objects.get(slug=cat_slug)
        last_articles = Article.objects.filter(
            categories__slug=cat_slug).order_by(
            '-pub_date').prefetch_related('categories')
    else:
        last_articles = Article.objects.all().order_by(
            '-pub_date').prefetch_related('categories')
        category = None

    paginator = Paginator(last_articles, articles_on_page)
    page_obj = paginator.get_page(curent_page)

    context = {
        'category': category,
        'page_obj': page_obj,
        'paginator': paginator
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['article'] = main_article
            Comment.objects.create(**data)
            form = CommentForm()
        else:
            messages.add_message(request, messages.INFO, 'Error in FORM fields')
    else:
        form = CommentForm()

    context['form'] = form

    return render(request, 'news/article.html', context)


def contact_hendler(request):
    context = {}
    return render(request, 'news/contact.html', context)


def robots_hendler(request):
    context = {}
    return render(request, 'news/robots.txt', context, content_type='text/plain')
