from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters


from .models import Book, BorrowedBook, Borrower, Category
from .serializers import BorrwedBookSerializer, CategorySerializer, BookSerializer, BorrowerSerializer
from .pagination import DefaultPagination




class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_calss = DefaultPagination
    search_fields = ['title', 'publisher']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]
    

class BorrwedBookViewSet(ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrwedBookSerializer
    pagination_calss = DefaultPagination
    search_fields = ['borrower', 'book']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["returned"]
    


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['title']

class BorrowerViewSet(ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
    pagination_calss = DefaultPagination
    search_fields = ['first_name', 'last_name']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["banned"]
    

