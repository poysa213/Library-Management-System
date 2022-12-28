from rest_framework import serializers
from .models import Category, Book, BorrowedBook, Borrower

# class BookImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookImages
#         fields = ['images']

class BookSerializer(serializers.ModelSerializer):
    # images = BookImageSerializer(many=True, read_only=True)
    # uploaded_images = serializers.ListField(
    #     child = serializers.FileField(max_length = 1000000, allow_empty_file = False, use_url = False),
    #     write_only = True
    # )
    class Meta:
        model = Book
        fields = ['id','title','quantity','description','category', 'pages', 'publisher']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description']

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'date_of_birth', 'banned']

class BorrwedBookSerializer(serializers.ModelSerializer):
    # book = BookSerializer()
    # borrower = BorrowerSerializer()
    class Meta:
        model = BorrowedBook
        fields = ['book', 'borrower', 'returned']