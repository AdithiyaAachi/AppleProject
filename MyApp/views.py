from django.shortcuts import render,redirect
from NewApp.models import BookDb,DetailsDb
from MyApp.models import contactdb,RegisterDb,CartDb
from django.contrib import messages

# Create your views here.
def homepage(request):
    book=BookDb.objects.all()
    return render(request,"Home.html",{'book':book})
def productpage(request):
    pro=DetailsDb.objects.all()
    return render(request,"Products.html",{'pro':pro})
def products_filter(request,book_name):
    data=DetailsDb.objects.filter(Genres=book_name)
    return render(request,"Products_Filtered.html",{'data':data})
def singlepro_page(request,proid):
    data=DetailsDb.objects.get(id=proid)
    return render(request,"SingleProduct.html",{'data':data})
def aboutpage(request):
    return render(request,"AboutUs.html")
def contactpage(request):
    return render(request,"ContactUs.html")
def save_contact(request):
    if request.method=="POST":
        fna=request.POST.get('name')
        lna=request.POST.get('lname')
        ema=request.POST.get('email')
        sub=request.POST.get('sub')
        msg=request.POST.get('message')
        obj=contactdb(FirstName=fna,LastName=lna,Email=ema,Subject=sub,Message=msg)
        obj.save()
        return redirect(contactpage)
def registerpage(request):
    return render(request,"Register.html")

def register_save(request):
    if request.method=="POST":
        na=request.POST.get('name')
        mob=request.POST.get('mobile')
        em= request.POST.get('email')
        un= request.POST.get('username')
        pwd= request.POST.get('password')
        obj=RegisterDb(Name=na,Mobile=mob,Email=em,Username=un,Password=pwd)
        obj.save()
        return redirect(registerpage)

def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('user')
        pwd=request.POST.get('passwrd')
        if RegisterDb.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username']=un
            request.session['Password']=pwd
            messages.success(request, "Welcome")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid username or password")
            return redirect(registerpage)
    return redirect(registerpage)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(registerpage)
def cartpage(request):
    data=CartDb.objects.filter(UserName=request.session['Username'])
    total_price=0
    for i in data:
        total_price=total_price+i.TotalPrice
    return render(request,"Cart.html",{'data':data,'total_price':total_price})
def save_cart(request):
    if request.method=="POST":
        unam=request.POST.get('uname')
        bnam=request.POST.get('bname')
        qty= request.POST.get('quantity')
        tpric = request.POST.get('tprice')
        desc= request.POST.get('definition')
        obj=CartDb(UserName=unam,BookName=bnam,Quantity=qty,TotalPrice=tpric,Definition=desc)
        obj.save()
        messages.success(request, "Cart save successfully..!")
        return redirect(cartpage)
def cart_delete(request,pro_id):
    pro=CartDb.objects.filter(id=pro_id)
    pro.delete()
    messages.error(request, "Cart delete successfully..!")
    return redirect(cartpage)

def checkoutpage(request):
    data = CartDb.objects.filter(UserName=request.session['Username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request,"Checkout.html",{'data':data,'total_price':total_price})