from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required

from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Add your create logic here (simplified)
    return render(request, "bookshelf/create_book.html")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Add your edit logic here
    return render(request, "bookshelf/edit_book.html")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Add your delete logic here
    return render(request, "bookshelf/delete_book.html")













from .forms import ExampleForm
