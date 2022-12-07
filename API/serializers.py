from rest_framework import serializers
from .models import Category, Book, BookImages, BorrowedBook, Borrower

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImages
        fields = ['images']

class BookSerializer(serializers.ModelSerializer):
    images = BookImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.FileField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only = True
    )
    class Meta:
        model = Book
        fields = ['id','title','quantity','description','category','images','uploaded_images', 'pages', 'publisher']