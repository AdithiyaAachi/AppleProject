from django.shortcuts import render,redirect
from NewApp.models import BookDb,DetailsDb
from MyApp.models import contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def indexpage(request):
    return render(request,"Indexpage.html")

def add_book_page(request):
    return render(request,"AddBook.html")
def save_book(request):
    if request.method=="POST":
        bna=request.POST.get('bname')
        dfn= request.POST.get('definition')
        img=request.FILES['image']
        obj=BookDb(BookName=bna,Definition=dfn,BookImage=img)
        obj.save()
        messages.success(request, "Geners save successfully....!")
        return redirect(add_book_page)
def display_book(request):
    disp=BookDb.objects.all()
    return render(request,"DisplayBook.html",{'disp':disp})
def edit_book(request,dataid):
    edit=BookDb.objects.get(id=dataid)
    return render(request,"EditBook.html",{'edit':edit})
def update_book(request,dataid):
    if request.method=="POST":
        bkn=request.POST.get('bname')
        defn= request.POST.get('definition')
        try:
            image=request.FILES['image']
            fs=FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file=BookDb.objects.get(id=dataid).BookImage
        BookDb.objects.filter(id=dataid).update(BookName=bkn,Definition=defn,BookImage=file)
        return redirect(display_book)

def remv_book(request,dataid):
    rem=BookDb.objects.filter(id=dataid)
    rem.delete()
    messages.error(request, "Genres Delete successfully....!")
    return redirect(display_book)

def add_details(request):
    book=BookDb.objects.all()
    return render(request,"AddDetails.html",{'book':book})
def save_details(request):
    if request.method=="POST":
        gn=request.POST.get('book')
        cnt= request.POST.get('content')
        defn= request.POST.get('definition')
        pr= request.POST.get('price')
        img=request.FILES['image']
        obj=DetailsDb(Genres=gn,BookName=cnt,Definition=defn,Price=pr,Book_Image=img)
        obj.save()
        messages.success(request, "Details save successfully....!")
        return redirect(add_details)

def display_details(request):
    disp=DetailsDb.objects.all()
    return render(request,"DisplayDetails.html",{'disp':disp})

def edit_details(request,dataid):
    book=BookDb.objects.all()
    details=DetailsDb.objects.get(id=dataid)
    return render(request,"EditDetails.html",{'book':book,'details':details})

def update_details(request,dataid):
    if request.method=="POST":
        gn=request.POST.get('book')
        ct= request.POST.get('content')
        dfn= request.POST.get('definition')
        pri= request.POST.get('price')
        try:
            image=request.FILES['image']
            fs=FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file=DetailsDb.objects.get(id=dataid).Book_Image
        DetailsDb.objects.filter(id=dataid).update(Genres=gn,BookName=ct,Definition=dfn,Price=pri,Book_Image=file)
        return redirect(display_details)

def remv_details(request,dataid):
    rem = DetailsDb.objects.filter(id=dataid)
    rem.delete()
    messages.error(request, "Book Details Delete successfully....!")
    return redirect(add_details)

def adminlogin(request):
    return render(request,"AdminLogin.html")

def admin_login(request):
    if request.method=="POST":
        una=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')

        if User.objects.filter(username__contains=una).exists():
            x=authenticate(username=una,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=una
                request.session['password']=pwd
                return redirect(indexpage)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)

def display_contact(request):
    data = contactdb.objects.all()
    return render(request,"DisplayContact.html",{'data':data})

def deletecontact(a,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_contact)





