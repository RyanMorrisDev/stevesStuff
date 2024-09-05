from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Book(models.Model):
    #Attribute for book title
    title = models.CharField(max_length=200)
    
    #Attribute authors First name
    fname = models.CharField(max_length=32)
    #Attribute authors last name
    lname = models.CharField(max_length=32)

    #Attribute Location
    location = models.CharField(max_length=1)

    #Attribute Row
    row = models.IntegerField()

    #Attribute published year
    year = models.CharField(max_length=4)

    #Attribute Book type 
    bookType = models.CharField(max_length=10)

    #Override string representation of object
    def __str__(this):
        #return book title when printing book models
        return this.title
