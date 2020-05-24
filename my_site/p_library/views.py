from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
from django.template import loader
from p_library.models import Book

def get_publisher(request):
    template = loader.get_template('publisher.html')
    books = Book.objects.all()
    publisher_dict = {}
    for book in books:
        if book.publisher.name not in list(publisher_dict.keys()):
            publisher_dict.update({book.publisher.name: [{'title': book.title, 'author':book.author.full_name}]})
        else:
            publisher_dict[book.publisher.name].append({'title': book.title, 'author': book.author.full_name})
    return HttpResponse(template.render({'publisher_dict': publisher_dict}, request))


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')