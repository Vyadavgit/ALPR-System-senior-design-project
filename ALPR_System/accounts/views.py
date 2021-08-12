from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import *
from .forms import UserRegistrationForm
from .decorators import unauthenticated_user
from .forms import AddResidentForm
from .forms import AddVehicleForm


# Create your views here.
@unauthenticated_user
def homeFn(request):
    return render(request, "accounts/homePage.html", {})

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

def logoutFn(request):
    logout(request)
    return redirect('home')

def dashboardFn(request):
    if request.user.is_staff:
        vehicles = Vehicle.objects.all()
        residents = Resident.objects.all()
        context = {'vehicles': vehicles,'residents':residents}
        return render(request, 'accounts/dashboardPage.html', context)
    else:
        curr_resident = Customer.objects.get(user=request.user)
        vehicles = Vehicle.objects.filter(owner=curr_resident)
        context = {'curr_resident': curr_resident, 'vehicles': vehicles}
        return render(request, 'accounts/resident_dashboardPage.html', context)

def editProfileFn(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)

    form = CustomerForm(instance=customer)
    context = {'form': form, 'customer': customer}

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile information has been updated successfully.")
            return redirect("/")
        else:
            messages.warning(request, 'PLease enter valid information following specified formats.')
    return render(request, 'accounts/edit_ProfilePage.html', context)

def registerVehicleFn(request):
    form = vehicleRegistrationForm()

    if request.method == 'POST':
        curr_customer = Customer.objects.get(user=request.user)
        vehicle = Vehicle.objects.create(owner=curr_customer)
        form = vehicleRegistrationForm(request.POST, instance=vehicle)

        if form.is_valid():
            form.save()
            messages.success(request, "Your vehicle registration has been submittted for approval.")
            return redirect("/")
        else:
            messages.warning(request, 'PLease enter valid information in correct formats.')
    context = {'form': form}
    return render(request, 'accounts/register_vehiclePage.html', context)









def residents(request):
    form = AddResidentForm()

    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = AddResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/add_resident.html', context)

def vehicles(request):
    form = AddVehicleForm()

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = AddVehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/add_vehicle.html', context)


def updateVehicle(request,pk):
    vehicle = Vehicle.objects.get(id=pk)
    form = AddVehicleForm(instance=vehicle)

    if request.method == 'POST':
        form = AddVehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('/')
 
    context = {'form':form}
    return render(request, 'accounts/add_vehicle.html', context)

def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    # form = AddVehicleForm(instance=vehicle)

    if request.method == "POST":
        vehicle.delete()
        return redirect('/')

    context = {'item':vehicle}
    return render(request, 'accounts/delete.html', context)








