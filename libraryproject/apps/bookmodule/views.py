from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 
from apps.bookmodule.models import Book
from apps.bookmodule.models import Address
from apps.bookmodule.models import Student
from django.db.models import Count ,Sum ,Avg,Max,Min
from .forms import BookForm  

from django.db.models import Q



def index(request): 
    # return HttpResponse("Hello, world!")
    name = request.GET.get("name") or "world!"  #add this line 
    # return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name 
    # return render(request, "bookmodule/index.html")
    return render(request, "bookmodule/index.html" , {"name": name})  #your render line 

def index2(request, val1 = 0):   
#add the view function (index2) 
    return HttpResponse("value1 = "+str(val1)) 



# ----------------------------------------------------
# Lab-9 [Part 1]
def list_books_New(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('books.listbooks')
    return render(request, 'bookmodule/add_book.html')


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('books.listbooks')
    return render(request, 'bookmodule/edit_book.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('books.listbooks')
    return render(request, 'bookmodule/delete_book.html', {'book': book})


# Lab-9 [Part 2]

def add_book_CRUD(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_book_CRUD.html', {'form': form})


def edit_book_CRUD(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/edit_book_CRUD.html', {'form': form})



#----------------------------------------------------

# Lab 8
def task1(request):
    mybooks = Book.objects.filter(price__lte=80)
    return render(request, 'bookmodule/task1.html', {'books': mybooks})

def task2(request):
    mybooks = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co')))
    return render(request, 'bookmodule/task2.html', {'books': mybooks})

def task3(request):
    mybooks = Book.objects.filter( Q(edition__lte=3) & ~Q(title__icontains='co') & ~Q(author__icontains='co'))
    return render(request, 'bookmodule/task3.html', {'books': mybooks})

def task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': mybooks})

def task5(request):
    mybooks = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'books': mybooks})

def task7(request):
    student_counts = Address.objects.annotate(num_students= Count('student'))
    return render(request, 'bookmodule/task7.html', {'student_counts': student_counts})

#----------------------------------------------------

# Lab 7
mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1) 
mybook.save() 
mybook = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1) 

def simple_query(request): 
    mybooks=Book.objects.filter(title__icontains='i') # <- multiple objects 
    return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 

def complex_query(request): 
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='i').filter(edition__gte = 2).exclude(price__lte = 100)[:10] 
    if len(mybooks)>=1: 
        return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 
    else: 
        return render(request, 'bookmodule/index.html') 

#---------------------------------------------------    
    

# Lab 6
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

def __getBooksList(): 
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
    return [book1, book2, book3] 
    

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
    
def search(request):
    if request.method == "POST": 
        string = request.POST.get('keyword').lower() 
        isTitle = request.POST.get('option1') 
        isAuthor = request.POST.get('option2') 
         # now filter 
        books = __getBooksList() 
        newBooks = [] 
        for item in books: 
            contained = False 
            if isTitle and string in item['title'].lower(): 
                contained = True 
            if not contained and isAuthor and string in item['author'].lower():
                contained = True 
            if contained: 
                newBooks.append(item) 
        return render(request, 'bookmodule/bookList.html', {'books':newBooks}) 
    else:
        return render(request,"bookmodule/search.html")
    

