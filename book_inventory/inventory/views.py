from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def index(request):
    items = Book.objects.all()

    context = {
        'items': items, #table
    }

    return render(request, 'index.html', context = context) #render table in main page

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            google_id = form.cleaned_data['google_id']   #Getting Google_ID field from the form which is automatically filled with AJAX API request
            
            if not Book.objects.filter(google_id = google_id).exists(): #Book does not exist in inventory
                #print(google_id)
                form.save()
                return redirect('index')

            else: #Book exists in inventory
                item = get_object_or_404(Book, google_id = google_id) #Get the item with corresponding GID
                additional_stock = form.cleaned_data['stock']  #Get the extra stock from the form stock field
                item.stock += additional_stock #Add to existing stock
                form = BookForm(request.POST, instance=item)  #populate instance with new updated stock
                form.save()
                return redirect('index')

    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})

def edit_book(request, pk):
    item = get_object_or_404(Book, pk=pk) #select statement with pk
    if request.method == "POST":
        form = BookForm(request.POST, instance=item)   #populate form with information with the information brought earlier
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm(instance=item)
        return render(request, 'edit_book.html', {'form':form})

def delete_book(request, pk):
    Book.objects.filter(id=pk).delete()
    
    items = Book.objects.all()

    context = {
        'items': items
    }

    return render(request, 'index.html', context)