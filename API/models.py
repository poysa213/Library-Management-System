from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    serial_number = models.BigIntegerField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category)
    pages = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class BookImages(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')
    images = models.FileField(upload_to='API/images', max_length=100, null=True)


class Borrower(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length = 254, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book)
    borrower = models.ForeignKey(Borrower)
    returned = models.BooleanField(default=False)