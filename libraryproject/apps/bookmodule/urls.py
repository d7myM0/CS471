from django.urls import path 
from apps.bookmodule import views




urlpatterns = [ 
    path('', views.index, name= "books.index"), 
    path('list_books/', views.list_books, name= "books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links, name='books.links'),
    path('html5/Text/formatting', views.Text, name='books.Text'),
    path('html5/listing', views.listing, name='books.listing'),
    path('html5/tables', views.tables, name='books.tables'),
    path('search/', views.search, name='books.search'),
    path('simple/query', views.simple_query, name='books.simple_query'),
    path('complex/query', views.complex_query, name='books.complex_query'),
    path('lab8/task1', views.task1, name='books.task1'),
    path('lab8/task2', views.task2, name='books.task2'),
    path('lab8/task3', views.task3, name='books.task3'),
    path('lab8/task4', views.task4, name='books.task4'),
    path('lab8/task5', views.task5, name='books.task5'),
    path('lab8/task7', views.task7, name='books.task7'),
    path('lab9_part1/listbooks', views.list_books_New, name='books.listbooks'),
    path('lab9_part1/addbook', views.add_book, name='books.addbook'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='books.editbook'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='books.deletebook'),
    path('lab9_part2/addbook', views.add_book_CRUD, name='books.addbook_CRUD'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_CRUD, name='books.editbook_CRUD'),
    
    



    



#     path('', views.index), Text formatters 
#     path('index2/<int:val1>/', views.index2 ) ,
#     path('<int:bookId>', views.viewbook)
] 