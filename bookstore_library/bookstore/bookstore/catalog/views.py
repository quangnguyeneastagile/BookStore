from django.shortcuts import render
from django.http import Http404
from django.views import generic
from .models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()

    book_list = Book.objects.filter(Category__name__contains='Hugo CDE')

    page = request.GET.get('page', 1)
    paginator = Paginator(book_list,2) #2 items per page
    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)

    return render(request,
                'index.html',
                context={'num_books':num_books,'book_list':book_list,},
    )

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    #book_id=get_object_or_404(Book, pk=pk)
    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )

def book_list_view(request):
    if Book.objects.all().count() <= 0:
        raise Http404("No book in the store!")
    #book_id=get_object_or_404(Book, pk=pk)
    else:
        print("Catergory inside: ", category_objs)
        return render(
            request,
            'catalog/book_list.html',
            context={'category_objs':category_objs,}
        )
