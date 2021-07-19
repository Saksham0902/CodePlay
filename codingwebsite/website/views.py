from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm #for registration page , default given by django
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login #because the name of the method is also login which will create infinite loop
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login')
def home(request):
    return render(request,'home.html',{})

@login_required(login_url = 'login')
def contact(request):

    if request.method == 'POST' :

        message_id =  request.POST['message']
        name_id = request.POST['name']
        email_id =  request.POST['email']
        subject_id = request.POST['subject']
    #
    # send_mail(
    # full_name, #subject
    # message_id, #message
    # email_id, #from email
    # ['sakshammathur429@gmail.com'] #to email
    # )
        return render(request,'contact.html',{'name_id':name_id})
    else:
        return render(request,'contact.html',{})

@login_required(login_url = 'login')
def courses(request):
    return render(request,'courses.html',{})

@login_required(login_url = 'login')
def blog(request):
    return render(request,'blog.html',{})

@login_required(login_url = 'login')
def video(request):
    return render(request,'video.html',{})

def login(request):
    if request.user.is_authenticated:
        return redirect('home.html')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                auth_login(request,user)
                return redirect('home.html')
            else:
                messages.info(request,'Username OR password is incorrect')

        context = {}
        return render(request,'login.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home.html')
    else:
        form = CreateUserForm()

        if request.method =='POST':
            form = CreateUserForm()
            if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request,'Account was created for ' + user)
                    return redirect('login.html')
        context ={'form':form}
        return render(request,'register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login.html')

def ThreeNumberSum(request):
    return render(request,'problems/ThreeNumberSum.html',{})

def ProductSum(request):
    return render(request,'problems/ProductSum.html',{})

def RemoveKthElementFromTheEnd(request):
    return render(request,'problems/RemoveKthElementFromTheEnd.html',{})

def ValidateBST(request):
    return render(request,'problems/ValidateBST.html',{})

def MoveElementToEnd(request):
    return render(request,'problems/MoveElementToEnd.html',{})

def NumberOfWaysToMakeChange(request):
    return render(request,'problems/NumberOfWaysToMakeChange.html',{})

def SingleCycleCheck(request):
    return render(request,'problems/SingleCycleCheck.html',{})
