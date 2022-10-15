from django.shortcuts import render


def single_hendler(request):
    context = {}
    return render(request, 'news/single.html', context)


def contact_hendler(request):
    context = {}
    return render(request, 'news/contact.html', context)


def category_hendler(request):
    context = {}
    return render(request, 'news/category.html', context)


def index_hendler(request):
    context = {}
    return render(request, 'news/index.html', context)


def robots_hendler(request):
    context = {}
    return render(request, 'news/robots.txt', context, content_type='text/plain')
