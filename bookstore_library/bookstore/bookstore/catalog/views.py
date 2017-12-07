from django.shortcuts import render
from django.http import Http404
from django.views import generic
from .models import *

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    return render(request,
                'index.html',
                context={'num_books':num_books,'num_authors':num_authors,},
    )

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
        book_list = Book
        return render(
            request,
            'catalog/book_list.html',
            context={'book_list':book_list,}
        )

class BookListView(generic.ListView):
    template_name = 'ctalog/book_list.html'
    context_object_name = 'book_list'
