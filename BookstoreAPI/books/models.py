from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    isbn = models.CharField(max_length=50, unique=True)
    published_date = models.DateField(auto_now=False, auto_now_add=False)