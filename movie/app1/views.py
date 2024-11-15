from django.shortcuts import render,redirect
from app1.models import Movie
from django.http import HttpResponse
# Create your views here.


def home(request):
    m=Movie.objects.all()
    context={'movie':m}  
    return render(request,'home.html',context)

def addmovie(request):
    if(request.method=="POST"):
        t = request.POST['t']
        d = request.POST['d']
        l = request.POST['l']
        y = request.POST['y']
        i = request.FILES['i']

        m=Movie.objects.create(title=t,description=d,language=l,year=y,image=i)
        m.save()
        return redirect('home')

    return render(request,'addmovie.html')

def details(request,p):
    print(p)
    k=Movie.objects.get(id=p)      #Reads a perticular record
    context={'movie':k}

    return render(request, 'details',context)
def delete(request,p):
    m=Movie.objects.get(id=p)
    m.delete()
    return redirect('home')

def edit(request,p):
    m=Movie.objects.get(id=p)  # read a particular record

    if(request.method=="POST"):
        m.title=request.POST['t']
        m.description=request.POST['d']
        m.language=request.POST['l']
        m.year=request.POST['y']
        if(request.FILES.get('i')==None):
            m.save()
        else:
            m.image=request.FILES.get('i')
        return redirect('home')

    context = {'movie':m}
    return render(request,'edit.html',context)



