from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_userforeignkey.models.fields import UserForeignKey
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import usersForm


def signup(request):
    if request.method == 'POST':
        stu = usersForm(request.POST)
        if stu.is_valid():
            user = User.objects.create_user(username=stu.cleaned_data['User_Name'],
                                            password=stu.cleaned_data['Password'],
                                            email=stu.cleaned_data['Email'])

            user.save()
            stu.save()
            return redirect('login')
    else:
        stu = usersForm()
    return render(request,'signup.html',{'form':stu})
def login(request):
    if request.method == 'POST':
        user = User()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        context = {'user':request.user}
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')

@login_required(login_url='login')
def home(request):
	return render(request,'home.html')