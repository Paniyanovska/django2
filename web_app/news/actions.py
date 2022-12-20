from threading import Thread
from news.crawlers import bbc_crawler


def count_words(modeladmin, request, queryset):
    for object in queryset:
        text = object.content.replace('<p>', '').replace('</p>', '')
        words = text.split()
        object.content_words_count = len(words)
        object.save()


count_words.short_description = "Count words in article"


def get_fresh_news(modeladmin, request, queryset):
    for object in queryset:
        if object.name == 'BBC News':
            Thread(target=bbc_crawler.run, args=()).start()


get_fresh_news.short_description = "Get fresh articles"
