from django.contrib import admin
from books.models import Author, Book, Publisher
# Register your models here.

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)