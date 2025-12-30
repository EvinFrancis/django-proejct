from django.shortcuts import render,redirect
from LibApp.models import bookdb,userdb

# Create your views here.
def libaray(request):
    return render(request,"index.html")
def add_book(request):
    return render(request,'Add_Book.html')
def book_details(request):
    data = bookdb.objects.all()
    return render(request, 'book_details.html', {'book': data})
def save_book(request):
    if request.method=="POST":
        name1=request.POST.get("name")
        email1=request.POST.get("email")
        password1=request.POST.get("password")
        gender1=request.POST.get("gender")
        location1=request.POST.get("location1")
        address1=request.POST.get("address")
        obj=bookdb(name=name1,email=email1,password=password1,gender=gender1,location=location1,address=address1)
        obj.save()
        return redirect(add_book)
def delete_book(request,book_id):
    stud=bookdb.objects.filter(id=book_id)
    stud.delete()
    return redirect(book_details)


def edit_book(request,book):
    data=bookdb.objects.get(id=book)
    return render(request,'edit_book.html',{'book':data})


def update_book(request,book):
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("email")
        c=request.POST.get("password")
        d=request.POST.get("gender")
        e=request.POST.get("location")
        f=request.POST.get("address")
        bookdb.objects.filter(id=book).update(name=a,email=b,password=c,gender=d,location=e,address=f)
        return redirect(book_details)

def add_user(request):
    return render(request,'add_user.html')
def user_details(request):
    return render(request,'user_details.html')

def save_user(request):
    if request.method=='POST':
        name1=request.POST.get("name")
        email1=request.POST.get("email")
        mobile1=request.POST.get("mobile")
        place1=request.POST.get("place")
        address1=request.POST.get("address")
        img=request.FILES['profile_image']
        obj=userdb(Name=name1,email=email1,mobile=mobile1,place=place1,address=address1
                   ,profile_image=img)
        obj.save()
        return redirect(add_user)
def user_detail(request):
    data=userdb.objects.all()
    return render(request,"user_details.html",{'user':data})

