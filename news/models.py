from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    in_menu = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Author(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars')
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    short_description = models.TextField()
    main_image = models.ImageField(upload_to='images')
    pub_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=255)
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[:20]


class Newsletter(models.Model):
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    subscribe_date = models.DateTimeField(auto_now_add=True)
    unscribe_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.name
