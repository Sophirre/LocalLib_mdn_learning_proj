from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre


def index(req):
    """
    Function to render home page
    """
    # Generation of count some main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.all().count()

    # HTML-Template rendering with integrated data

    return render(req, "index.html",
                  context={"num_books": num_books, "num_instances": num_instances,
                           "num_instances_available": num_instances_available, "num_authors": num_authors})