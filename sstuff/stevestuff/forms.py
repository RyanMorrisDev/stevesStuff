from django import forms
from django.forms import ModelForm, PasswordInput, CharField, ValidationError, TextInput
from .models import Book

#Create Book form 
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
