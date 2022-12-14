from django.contrib import admin
from .models import Book, Category, BorrowedBook, Borrower
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Borrower)
admin.site.register(BorrowedBook)
# admin.site.register(BookImages)