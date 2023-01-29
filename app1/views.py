from django.shortcuts import render
from os import name
from pickle import OBJ
from django.shortcuts import redirect
from django.http import HttpResponse
from urllib import request
from app1.models import Student,Faculty,Admin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

# User = get_user_model()
# # Create your views here.
# @login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

# def login(request):
#     global username
#     global password1
#     if request.method =='POST':
#         username=request.POST.get('username')
#         password1=request.POST.get('password1')
#         my_user=Signup.objects.all()

#         my_user = authenticate(request, username=username, password=password1)

        
#         if my_user is not None:
#             login(request, my_user)
#             return redirect('HomePage')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
            
#     return render (request,'login.html')


# def signuppage(request):
#     global username
#     global password1
#     if request.method=='POST':
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         password1=request.POST.get('password1')
#         password2=request.POST.get('password2')
#         my_user = Signup(username=username,email=email,password1=password1,password2=password2)
#         my_user.save()
#         if password1!=password2:
#             return render(request,'signup.html',{'error':"Your password and confrom password are not Same!!"})
#         try:
#             User.objects.get(username=username)
#             return render(request, 'signup.html', {'error': 'Username already taken'})
#         except User.DoesNotExist:
#             pass
#         my_user = User.objects.create_user(username=username, email=email, password=password1)
#         my_user.save()

#         # login user
#         login(request, my_user)
#         return redirect('login')
#         # else:
#         #     my_user =User.objects.create_user(username=username, email=email, password=password1)
#         #     my_user.save()
#         #     login(request, my_user)
#         #     return redirect('login')

#     return render(request, 'signup.html')
def ragist(req):
    return render(req, "ragist.html")

def ragisttask(req):
    role = req.GET.get("role")
    if role == "Student":
        from . models import Student
        ob = Student()
        ob.name = req.GET.get("name")
        ob.fname = req.GET.get("fname")
        ob.email = req.GET.get("email")
        ob.password = req.GET.get("password")
        ob.gender = req.GET.get("gender")
        ob.dob = req.GET.get("dob")
        ob.mob = req.GET.get("mob")
        ob.save()
        return redirect("login")
    elif role == "Faculty":
        from . models import Faculty
        ob = Faculty()
        ob.name = req.GET.get("name")
        ob.fname = req.GET.get("fname")
        ob.email = req.GET.get("email")
        ob.password = req.GET.get("password")
        ob.gender = req.GET.get("gender")
        ob.dob = req.GET.get("dob")
        ob.mob = req.GET.get("mob")
        ob.save()
        return redirect("login")
    else:
        return HttpResponse("Please choose anyone")



def login(req):
    return render(req, "login.html")


def logintask(req):
    global email
    global password

    role = req.GET.get("role")
    if role == "Student":
        email = req.GET.get("email")
        password = req.GET.get("password")
        from app1.models import Student
        db = Student.objects.all()
        for i in db:
        #   if role==i.role:
            if email == email:
                if password == password:
                    return redirect("db")
                else:
                    return redirect("login")
            else:
                return HttpResponse("Please Select right role")
        else:
            return redirect("ragist")


def db(req):
    from app1.models import Student
    rec = Student.objects.filter(email=email)
    return render(req, "db.html", {'rec': rec})


def student(req):
    from app1.models import Student
    rec = Student.objects.filter(email=email)
    return render(req, 'student.html', {'rec': rec})


def faculty(req):
    from app1.models import Faculty
    rec = Faculty.objects.filter(email=email)
    return render(req, 'faculty.html', {'rec': rec})


def updateStudent(req):
    from . models import Student
    id = req.GET.get("id")
    ob = Student.objects.get(id=id)
    ob.name = req.GET.get("name")
    ob.fname = req.GET.get("fname")
    ob.email = req.GET.get("email")
    ob.password = req.GET.get("Password")
    ob.gender = req.GET.get("gender")
    ob.dob = req.GET.get("dob")
    ob.mob = req.GET.get("mob")
    ob.save()

    return render(request, "home.html")