from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    # if the button is clicked and the method received from request is POST
    if request.method == 'POST':

        # Create variables to store data from the form
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email_add = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if both passwords are the same
        if password == password2:

            # check if the email already exists in the database
            if User.objects.filter(email=email_add).exists():
                messages.info(request, 'The email address is already in use.')
                return redirect('register')
            
            #check if the username already exists in the database
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'The username is already taken.')
                return redirect('register')
            
            #if everything is False then this should be excecuted
            else:
                user = User.objects.create_user(first_name=f_name, last_name=l_name, username=username, email=email_add, password=password)
                user.save()
                return redirect('login')
        
        # if passwords don't match this should run
        else:
            messages.info(request, 'Passwords don\'t match.')
            return redirect('register')
    
    # if users is not looking to register we still render the view
    else:
        return render(request, 'register.html')