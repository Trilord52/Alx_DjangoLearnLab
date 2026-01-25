from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.view_books, name="view_books"),
    path("add_book/", views.create_book, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]
