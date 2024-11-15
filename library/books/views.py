from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request, 'home.html')

from books.models import Book


@login_required
def view(request):
    k = Book.objects.all()     #reads all records from the book table
    context = {'book': k}      #sends data from view function to html page
    return render(request, 'view.html',context)


@login_required
def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        pa = request.POST['pa']
        l = request.POST['l']
        i=request.FILES['i']
        f=request.FILES['f']
        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=i,pdf=f)
        b.save()
        return view(request)

    return render(request,'add.html')

def viewdetails(request,p):
    print(p)
    k=Book.objects.get(id=p)      #Reads a perticular record
    context={'book':k}

    return render(request, 'viewdetails.html',context)

def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return redirect('books:view')

def edit(request,p):
    k=Book.objects.get(id=p)
    if (request.method == "POST"):
        k.title = request.POST['t']
        k.author = request.POST['a']
        k.price = request.POST['pr']
        k.pages = request.POST['pa']
        k.language = request.POST['l']
        if (request.FILES.get('c') == None):
            k.save()
        else:
            k.cover = request.FILES.get("c")
        if (request.FILES.get('p') == None):
            k.save()
        else:
            k.pdf = request.FILES.get("p")
        k.save()
        return redirect('books:view')
    context={'book':k}
    return render(request,'edit.html',context)


