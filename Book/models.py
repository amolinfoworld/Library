from django.db import models
from django.db.models.manager import Manager
from Book.model_enum import Math,Names

# Create your models here.

class ActiveBookManager(models.Manager):
    ''' get the Books.objects.all() objects '''
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted="N")

class InActiveBookManager(models.Manager):
    ''' get the Books.objects.all() objects '''
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted="Y")

class Book(models.Model):
    ''' class to create book table'''
    name=models.CharField(max_length=100)
    qnty=models.IntegerField()
    price=models.FloatField()
    is_published=models.BooleanField(default=False)
    published_date=models.DateField(null=True)
    is_deleted=models.CharField(max_length=1,default="N")
    active_books=ActiveBookManager()  #manager ----
    in_active_books=InActiveBookManager()
    object=Manager() #base objects

    def __str__(self):
        return f"{self.__dict__}"

    class Meta:
        db_table="book"

