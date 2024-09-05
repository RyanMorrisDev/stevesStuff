from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

#import book model and book form
from .models import Book
from .forms import BookForm
# Create your views here.

#Homepage view
def homePage(request):
    return render(request, "homepage.html")

#book page view
def Books(request):
    #Get all books using queryset
    books = Book.objects.all()
    totalBooks = Book.objects.count()

    print(f"total books:{totalBooks}")

    context = {"page_title":"Books","books":books,"totalBooks":totalBooks,}
    
    return render(request, "books.html", context)

#add Book page
def addBookPage(request):
    #Create book from object 
    form = BookForm()

    #Check form submission
    if request.method == 'POST':
        #Create book object from form
        Book.objects.create(
            title = request.POST.get('title'),
            fname = request.POST.get('fname'),
            lname = request.POST.get('lname'),
            location = request.POST.get('location'),
            row = request.POST.get('row'),
            year = request.POST.get('year'),
            bookType = request.POST.get('bookType'),
        )
        #Redirect to book page
        #return redirect('/books')
    #Context - passing page Title and add book form
    context = {'page_title':'Add Book', 'form':form}
    return render(request, 'addbookpage.html', context)

#Author page 
def authorPage(request):
    return render(request,"authors.html")
