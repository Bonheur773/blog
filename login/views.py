from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "docs/index.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myuser = User.objects.create_user(username, email, pass1)

        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your Account has been successfully created!")
        return redirect('home')

    return render(request, "docs/signup.html")

def signin(request):
    return render(request, "docs/signin.html")

def signout(request):
    pass