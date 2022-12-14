from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from .models import Book, BorrowedBook, Borrower, Category
from .serializers import BorrwedBookSerializer, CategorySerializer, BookSerializer, BorrowerSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrwedBookViewSet(ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrwedBookSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BorrowerViewSet(ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

