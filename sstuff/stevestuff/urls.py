from django.urls import path

#import views
from . import views

#URL patterns - site routes
urlpatterns = [
    path('', views.homePage, name="Home Page"),
    path('books/', views.Books, name="Books"),
    path('books/add-book', views.addBookPage, name="Add Book Page"),
    path('books/authors', views.authorPage, name="authors"),
]
