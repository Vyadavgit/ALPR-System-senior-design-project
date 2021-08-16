from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .forms import *
from .forms import UserRegistrationForm
from .decorators import unauthenticated_user
from .filters import *


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

            messages.success(request, 'Account successfully created for ' + username)
    
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
    try:
        ParkingspaceObj = Parkingspace.objects.get(id=1)
    except ObjectDoesNotExist:
        ParkingspaceObj = Parkingspace.objects.create(total_space = 100)

    total_parking_slots = ParkingspaceObj.total_space
    space_occupied = Vehicle.objects.filter(parked=True).count()
    space_vacant = total_parking_slots - space_occupied
    if request.user.is_staff:
        vehicles = Vehicle.objects.all()
        residents = Customer.objects.all()

        searchFilter = VehicleFilter(request.GET, queryset=vehicles)
        searchedObjects = searchFilter.qs

        if vehicles.count() != searchedObjects.count():
            vehicles = searchedObjects
            context = {'vehicles': vehicles,'residents':residents, 'total_parking_slots': total_parking_slots, 'space_occupied':space_occupied, 'space_vacant':space_vacant, 'searchFilter': searchFilter}
            return render(request, 'accounts/dashboardPage.html', context)
        else:
            context = {'vehicles': vehicles,'residents':residents, 'total_parking_slots': total_parking_slots, 'space_occupied':space_occupied, 'space_vacant':space_vacant, 'searchFilter':searchFilter}
            return render(request, 'accounts/dashboardPage.html', context)


    else:
        curr_resident = Customer.objects.get(user=request.user)
        vehicles = Vehicle.objects.filter(owner=curr_resident)
        context = {'curr_resident': curr_resident, 'vehicles': vehicles, 'total_parking_slots': total_parking_slots, 'space_occupied':space_occupied, 'space_vacant':space_vacant}
        return render(request, 'accounts/resident_dashboardPage.html', context)

@login_required(login_url='login')
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
        else:
            messages.warning(request, 'PLease enter valid information following specified formats.')
    return render(request, 'accounts/edit_ProfilePage.html', context)

@login_required(login_url='login')
def registerVehicleFn(request):
    form = vehicleRegistrationForm()

    if request.method == 'POST':
        curr_customer = Customer.objects.get(user=request.user)
        vehicle = Vehicle.objects.create(owner=curr_customer)
        form = vehicleRegistrationForm(request.POST, instance=vehicle)

        if form.is_valid():
            form.save()
            messages.success(request, "Your vehicle registration has been submittted for approval.")
        else:
            messages.warning(request, 'PLease enter valid information in correct formats.')
    context = {'form': form}
    return render(request, 'accounts/register_vehiclePage.html', context)

@login_required(login_url='login')
def updateVehicle(request,pk):
    vehicle = Vehicle.objects.get(id=pk)
    form = updateVehicleForm(instance=vehicle)

    if request.method == 'POST':
        form = updateVehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('/')
 
    context = {'form':form}
    return render(request, 'accounts/add_vehicle.html', context)

@login_required(login_url='login')
def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)

    if request.method == "POST":
        vehicle.delete()
        return redirect('/')

    context = {'item':vehicle}
    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def deleteResident(request, pk):
    resident = Customer.objects.get(id=pk)

    if request.method == "POST":
        resident.delete()
        associatedVehicles = Vehicle.objects.filter(owner=resident)
        associatedVehicles.delete()
        return redirect('/')

    context = {'item':resident}
    return render(request, 'accounts/deleteResident.html', context)

@login_required(login_url='login')
def updateTotalSpaceFn(request):
    form = updateTotalSpaceForm()

    if request.method == 'POST':
        try:
            Parking_obj = Parkingspace.objects.get(id=1)
            form = updateTotalSpaceForm(request.POST, instance=Parking_obj)
            if form.is_valid():
                form.save()
                return redirect('/')
        except ObjectDoesNotExist:
            form = updateTotalSpaceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/update_parking_spacePage.html', context)













