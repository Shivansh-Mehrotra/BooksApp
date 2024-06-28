import datetime
from django.db import models
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Publisher(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True,default='')
    address = models.TextField(null=True,blank=True,default=datetime.datetime.now())
    website = models.URLField(null=True,blank=True,default='')

    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.CharField(max_length=255)
    published_date = models.DateField()
    type = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
       return self.book_name