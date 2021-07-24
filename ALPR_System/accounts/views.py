from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import *
from .forms import UserRegistrationForm
from .decorators import unauthenticated_user
from .forms import AddResidentForm
# from .forms import AddVehicleForm


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
            form.save()
            username = form.cleaned_data.get('username')

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

def logoutFn(request):
    logout(request)
    return redirect('home')

def dashboardFn(request):
    residents = Resident.objects.all()

    context = {'residents':residents}

    return render(request, 'accounts/dashboardPage.html', context)


def addResident(request):
    form = AddResidentForm()

    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = AddResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/add_resident.html', context)

# def addResident(request):
#     form = AddResidentForm()

#     if request.method == 'POST':
#         print('Printing POST:', request.POST)
#         form = AddResidentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')

#     context = {'form': form}
#     return render(request, 'accounts/add_resident.html', context)


# def addVehicle(request):
#     form = AddVehicleForm()

#     if request.method == 'POST':
#         print('Printing POST:', request.POST)
#         form = AddVehicleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form': form}
#     return render(request, 'accounts/add_vehicle.html', context)


# def updateVehicle(request, pk):

#     vehicle = Vehicle.objects.get(id=pk)
#     form = AddVehivleForm(instance=vehicle)

#     if request.method == 'POST':
#         form = AddVehivleForm(request.POST, instance=vehicle)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
 
#     context = {'form':form}
#     return render(request, 'accounts/add_vehivle.html', context)

# def deleteOrder(request, pk):
#     vehicle = Vehicle.objects.get(id=pk)
#     if request.method == "POST":
#         vehicle.delete()
#         return redirect('/')

#     context = {'item':vehicle}
#     return render(request, 'accounts/delete.html', context)








