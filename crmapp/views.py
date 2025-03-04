from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUp, AddPerson
from .models import Data


def home(request):
    records = Data.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            messages.success(request, "You have logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error. Try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You logged out")
    return redirect('home')

def register(request):
    match request.method:
        case 'POST':
            form = SignUp(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "You created an account. Welcome")
                return redirect('home')
        
        case _:
            form = SignUp()
            return render(request, 'register.html', {'form' : form})
        
    return render(request, 'register.html', {'form' : form})

def individual_record(request, pk):
    if request.user.is_authenticated:
        individual_record = Data.objects.get(id=pk)
        return render(request, 'person.html', {'individual_record' : individual_record})
    
    else:
        messages.success(request, "You must log in first")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete = Data.objects.get(id=pk)
        delete.delete()
        messages.success(request, "Deleted Successfully")
        return redirect('home')
    
    else:
        messages.success(request, "You must log in first")
        return redirect('home')
    
def add_person(request):
    form = AddPerson(request.POST or None)
    if request.user.is_authenticated:
        match request.method:
            case 'POST':
                if form.is_valid():
                    add_person = form.save()
                    messages.success(request, "Person Added")
                    return redirect('home')   
        return render(request, 'add_person.html', {'form': form})
    
    else:
        messages.success(request, "You must log in first")
        return redirect('home')

def update(request, pk):
    if request.user.is_authenticated:
        current_data = Data.objects.get(id=pk)
        form = AddPerson(request.POST or None, instance=current_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data has been updated")
            return redirect('home')
        return render(request, 'update_person.html', {'form': form})
    
    else:
        messages.success(request, "You must log in first")
        return redirect('home')