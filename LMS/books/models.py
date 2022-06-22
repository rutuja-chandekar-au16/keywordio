from email.policy import default
from django.db import models

class Book(models.Model):
    book_no = models.IntegerField(default=0)
    name= models.CharField(max_length=200, blank=True, null=True)
    Author_name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self): 
        return self.name
