from django.shortcuts import render
from django.http import Http404
from django.views import generic
from .models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#from django.contrib.auth.decorators import permission_required

from .forms import AuthorForm
# Create your views here.

#@permission_required('catalog.can_mark_returned')
def index(request):
    #read book author to filter from form
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author_name = request.session.get('author_name', '')
            request.session['author_name'] = form.cleaned_data['author_name']
            author_name = request.session.get('author_name', '')
            book_list = Book.objects.filter(author__name__contains=author_name)
    else:
        author_name = request.session.get('author_name', '')
        book_list = Book.objects.filter(author__name__contains=author_name)
        form = AuthorForm(initial={'author_name':'Type in author name'})

    if book_list.all().count() <= 0:
        request.session['author_name'] = ''
        return render(request, 'catalog/error/oops.html', {})
    else:
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
                context={'book_list':book_list,'form':form},
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
