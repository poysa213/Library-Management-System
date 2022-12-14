from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)

   

class Book(models.Model):
    title = models.CharField(max_length=200)
    serial_number = models.BigIntegerField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    pages = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True)
   
    class Meta:
        ordering = ['title']



class Borrower(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length = 254, unique=True, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    number_visits = models.SmallIntegerField(default=1)
    banned = models.BooleanField(default=False)

   
    class Meta:
        ordering = ['last_name', 'first_name']

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)
    returned = models.BooleanField(default=False)

    class Meta:
        ordering = ['returned']

    

  