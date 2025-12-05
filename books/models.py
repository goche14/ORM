from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.FloatField(null=True)
    published = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    stock = models.IntegerField()

    