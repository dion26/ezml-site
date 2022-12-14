from email import contentmanager, message
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserForm, EzmlUserCreationForm
from .models import User

from forums.models import Thread, Subforum, Comment
from dj_rest_auth.views import LoginView

def loginPage(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User not found')
            return redirect('login')
        user = authenticate(request, email=email, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = EzmlUserCreationForm()

    if request.method == 'POST':
        form = EzmlUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registeration')


    context = {'form': form}
    return render(request, 'base/login_register.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    threads = user.thread_set.all()
    thread_comments = user.comment_set.all()

    context = {'user': user, 'threads': threads, 'thread_comments': thread_comments}
    return render(request, 'base/profile.html', context)

def home(request):
    subforum = Subforum.objects.all()
    context = {'topics': subforum,}
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update_user.html', {'form': form})


class CustomApiLoginView(LoginView):
    pass