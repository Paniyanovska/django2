from requests_html import HTMLSession
from slugify import slugify
from concurrent.futures import ThreadPoolExecutor
from news.models import Article, Author, Category


author = Author.objects.get(id=3)

#articles = []


def crawl_one(url):
    with HTMLSession() as session:
        response = session.get(url)

    name = response.html.xpath('//h1')[0].text
    content = response.html.xpath('//div[@data-component="text-block"]//p')
    image_url = response.html.xpath('//div[@data-component="image-block"]//img/@src')[0]
    pub_date = response.html.xpath(
        '//li[@role="listitem"]//time[@data-testid="timestamp"]/@datetime')[0]
    cats = response.html.xpath('//section[@data-component="tag-list"]//li')

    my_content = ''
    short_description = ''

    for element in content:
        my_content += f'<{element.tag}>' + element.text + f'</{element.tag}>'
        if len(short_description) < 200:
            short_description += element.text + ' '

    image_name = slugify(name)
    image_type = image_url.split('.')[-1]
    img_path = f'images/{image_name}.{image_type}'

    with open(f'media/{img_path}', 'wb') as f:
        with HTMLSession() as session:
            response = session.get(image_url)
            f.write(response.content)

    categories = []
    for cat in cats:
        categories.append(
            {
                'name': cat.text.strip(),
                'slug': slugify(cat.text)
            }
        )

    article = {
        'name': name,
        'slug': slugify(name),
        'content': my_content,
        'short_description': short_description.strip(),
        'main_image': img_path,
        'pub_date': pub_date,
        'author': author
    }
    #article = Article(**article)
    #articles.append(article)

    article, created = Article.objects.get_or_create(**article)

    for category in categories:
        cat, created = Category.objects.get_or_create(**category)
        article.categories.add(cat)

    print(article)


def get_fresh_urls():
    base_url = 'https://www.bbc.com/news/technology'

    with HTMLSession() as session:
        response = session.get(base_url)

    links = response.html.absolute_links

    fresh_news = []

    for link in links:
        try:
            if link.split('-')[-1].isdigit():
                fresh_news.append(link)
        except (Exception,):
            pass

    return fresh_news


def run():
    #Article.objects.all().delete()
    fresh_news = get_fresh_urls()
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(crawl_one, fresh_news)

    #Article.objects.bulk_create(articles, ignore_conflicts=True)


if __name__ == '__main__':
    run()
