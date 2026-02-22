from django.db import models

class Author(models.Model):
    """
    Author model represents a book author.

    Fields:
        name (CharField): Stores the author's name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an author.

    Fields:
        title (CharField): Title of the book.
        publication_year (IntegerField): Year the book was published.
        author (ForeignKey): Links each book to one Author.
                            Establishes a one-to-many relationship:
                            One Author -> Many Books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',  # Enables reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
