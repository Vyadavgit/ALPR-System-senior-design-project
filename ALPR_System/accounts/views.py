from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *
from .forms import UserRegistrationForm
from .decorators import unauthenticated_user
from .filters import NameFilter

# Create your views here.
@unauthenticated_user
def homeFn(request):
    return render(request, "accounts/homePage.html")

@unauthenticated_user
def registerFn(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            curr_user = form.save()
            username = form.cleaned_data.get('username')

            # customer (associated with the current registered user) created with provided minimal info during registeration
            Customer.objects.create(user = curr_user, first_name=form.cleaned_data.get('first_name'), last_name=form.cleaned_data.get('last_name'), email=form.cleaned_data.get('email') )

            messages.success(request, 'Account successfully created for + ' + username)

            return redirect('login')
    
    context = {'form': form}
    return render(request, 'accounts/registerPage.html', context)

@unauthenticated_user
def loginFn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid username or password!')
    
    return render(request, 'accounts/loginPage.html', {})

@login_required(login_url='login')
def logoutFn(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboardFn(request):
    return render(request, 'accounts/dashboardPage.html', {})

# def searchfilterFn(request):
#     return render(request, 'accounts/searchfilter.html', {}

def customer(request):
    # customer=Customer.objects.get(id) 
    # fname= Customer.
    fname=Customer.objects.all()

    myFilter= NameFilter(request.GET, queryset=fname)
    fname = myFilter.qs
    
   
    context = {'fname':fname,'myFilter': myFilter}
    return render(request, 'accounts/customer.html',context)
