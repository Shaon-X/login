from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import register_form


# Create your views here.
def user_login(request):

    if request.user.is_authenticated:
        return redirect('home_url')
    if request.method == "POST":
       # print(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_url')
        else:
            messages.success(request, ("Login unsuccessful, please try again"))
            return redirect('login_url')
    else:
        return render(request, 'login.html')


def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect('login_url')

def logout_page(request):
    logout(request)
    messages.success(request, ("Logout successful"))
    return redirect('login_url')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home_url')
    if request.method == "POST":
        print(request.POST)
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('home_url')
        else:
            return render(request, '../template/register.html', {'form': form})

    else:
        form = register_form()
        context = {
            'form': form,
        }
        return render(request, '../template/register.html', context)

def profile_page(request):
    user = request.user
    if request.method == "POST":
        form = register_form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            messages.success(request, ("Changes made Successfully"))
            return redirect('profile_url')
        else:
            return render(request, '../template/profile.html', {'form': form})

    else:
        if request.user.is_authenticated:
            form = register_form(instance=user)
            context = {
                'form': form,
            }
            return render(request, '../template/profile.html', context)
        return redirect('login_url')

def delete_page(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            user=request.user
            logout(request)
            user.delete()
            messages.success(request, ("Successfully deleted user"))
            return redirect('login_url')

        else:

            context = {

            }
            return render(request, '../template/delete.html', context)
    return redirect('login_page')

def admin_page(request):
    if request.user.is_authenticated:
        return redirect('admin/')
    return redirect('login_page')

