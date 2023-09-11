from django.urls import path

from .views import bookViewList , getBookDetalis , SearchList , CreateBook 

urlpatterns = [
    path('' , bookViewList.as_view() , name='book_list'),
    path('<uuid:pk>/' , getBookDetalis , name='book_detalis'),
    path('search/' , SearchList.as_view(), name='search'),
    path('create/' , CreateBook.as_view() , name='create'),
] 