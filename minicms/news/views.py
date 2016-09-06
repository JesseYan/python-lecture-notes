# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from models import Column, Article

# Create your views here.


def index(request):

    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)

    # return HttpResponse(u'欢迎来minicms系统')
    columns = Column.objects.all()
    # return render(request, 'index.html', {'columns': columns})
    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
    })


def column_detail(request, column_slug):
    # return HttpResponse('column slug: ' + column_slug)
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})


def article_detail(request, article_slug):
    article = Article.objects.filter(slug=article_slug)[0]
    return render(request, 'news/article.html', {'article': article})
    # return HttpResponse('article slug: ' + article_slug)

