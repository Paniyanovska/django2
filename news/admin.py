from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from .actions import count_words, get_fresh_news
from .models import Article, Author, Category, Newsletter, Comment, Tag


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'short_description')
    list_display = ('image_code', 'name', 'pub_date',
                    'author', 'content_words_count', 'count_unique_words')
    list_filter = ('author', 'pub_date', 'categories')
    search_fields = ('name', 'author')
    actions = (count_words, )

    def image_code(self, object):
        return format_html(
            '<img src="{}" style="max-width: 100px" />',
            object.main_image.url
        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'in_menu', 'order', 'articles_count')
    list_filter = ('in_menu', )
    search_fields = ('name', )
    list_editable = ('order', 'in_menu')
    readonly_fields = ('order', )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('article_set')

    def articles_count(selfs, object):
        return object.article_set.all().count()


class AuthorArticleInline(admin.TabularInline):
    model = Article
    exclude = ('content', 'short_description')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'ava')
    search_fields = ('name',)
    inlines = (AuthorArticleInline, )
    actions = (get_fresh_news, )

    def ava(self, object):
        return format_html(
            '<img src="{}" style="max-width: 70px" />',
            object.avatar.url
        )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Newsletter)
admin.site.register(Comment)
admin.site.register(Tag)
