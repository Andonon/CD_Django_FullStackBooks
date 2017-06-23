# -*- coding: utf-8 -*-
#pylint --load-plugins
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Books
# Create your views here.
def index(request):
    books = Books.objects.all()
    print "*"*50
    print (books)
    print "*"*50
    context = {"books": books}
    return render(request, 'books/index.html', context)

def addbook(request): 
    print request.POST
    Books.objects.create(title=request.POST['title'],
    author=request.POST['author'],
    category=request.POST['category']
    )
    return redirect('/')
