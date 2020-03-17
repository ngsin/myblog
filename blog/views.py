from django.shortcuts import render
from django.http import  HttpResponse
from . import models
# Create your views here.
import markdown


def index(request):
    articles = models.ExampleModel.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.ExampleModel.objects.get(pk=article_id)
    # article.content = markdown.markdown(article.content)

    article.content = markdown.markdown(article.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.ExampleModel.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST['title']
    content = request.POST['content']
    article_id = request.POST.get('article_id', '0')
    if article_id == "0":
        models.ExampleModel.objects.create(name=title, content=content)
        articles = models.ExampleModel.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    article = models.ExampleModel.objects.get(pk=article_id)
    article.name = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})


def blog_templates(request):
    return render(request, 'blog_template01/index.html')