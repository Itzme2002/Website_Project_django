from django.conf import settings
from django.contrib import auth
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse,redirect
from .models import Students,Product,Profile
from django.contrib.auth.models import User
# Create your views here.
# def home(request):
#     return HttpResponse("enthelum content reborn")
# def home(request):
#     return render(request,'home.html',{'name':'eldhojoy'})
# def home(request):
#     a = {'first_name':'eldho','last_name':'joy'}
#     return render(request,'home.html',{"name":a})
def login(request):
    loop=[{'fname': 'alvin','lname': 'jops','place': 'erk'},{'fname': 'njanalla','lname': 'kelvin','place': 'newyork'},{'fname': 'pol','lname': 'gt','place': 'kochi'}]
    return render(request,'login.html',{"names":loop})
def about(request):
    y=['colors','paru','enthelum','kodukk']
    return render(request,'about.html',{"colors":y})
def help(request):
    return render(request,'help.html')
def contact(request):
    return render(request,'contact.html')
def home(request):
    f = Students.objects.all()
    return render(request,'home.html',{"std":f})
# def form(request):
#     if request.method == "POST":
#         x = Product()
#         x.pro_name = request.POST['pro_name']
#         x.pro_weight = request.POST['pro_weight']
#         x.pro_price = request.POST['pro_price']
#         x.pro_image = request.FILES['pro_image']
#         x.save()
#         return HttpResponse(' successfully saved ')
#     else:
#         return render(request,'form.html')
def form(request):
    k = Product.objects.filter(pro_price__lte=1999)
    return render(request,'form.html',{'Pro': k})
def registration(request):
    if request.method == "POST":
        username = request.POST['user_name']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
                return redirect('registration')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=firstname,
                    last_name=lastname,
                    password=password
                )
                subject = 'welcome to vintage info solution'
                message = '{ user.firstname , user.lastname }, thankyou for registation mariyathekk website vist cheytholanam'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email,]
                send_mail(subject,message,email_from,recipient_list)
                c = Profile()
                c.user = user
                c.gender = request.POST['my_gender']
                c.phone_number = request.POST['phone_number']
                c.place = request.POST['place']
                c.save()
                return redirect('login_user')
        else:
            return redirect('registration')
    else:
        return render(request,'registration.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST['user_name']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.check_password(password):
                if user:
                    auth.login(request,user)
                    return redirect('dash_board')
            else:
                return render(request,'login_user.html')
        else:
            return render(request, 'login_user.html')
    else:
        return render(request,'login_user.html')

def dash_board(request):
    return render(request,'dash_board.html')

def logout(request):
    auth.logout(request)
    return redirect("registration")