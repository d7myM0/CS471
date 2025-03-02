from django.shortcuts import render
from django.http import HttpResponse 


def index(request): 
    # return HttpResponse("Hello, world!")
    name = request.GET.get("name") or "world!"  #add this line 
    # return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name 
    # return render(request, "bookmodule/index.html")
    return render(request, "bookmodule/index.html" , {"name": name})  #your render line 

def index2(request, val1 = 0):   
#add the view function (index2) 
    return HttpResponse("value1 = "+str(val1)) 



def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble'}
    book2 = {'id': 456, 'title': 'Reverse Engineering', 'author': 'E. Eilam'}
    
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)
    

def index(request): 
    return render(request, "bookmodule/index.html") 

def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 

def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html') 

def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html') 


def links(request):
    return render(request,'bookmodule/links.html')

def Text(request):
    return render(request,'bookmodule/Text.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')
    

