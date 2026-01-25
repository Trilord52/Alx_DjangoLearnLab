from bookshelf.models import Book
Book.objects.all().delete()
Book.objects.all()
