from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    # 로그인 로직
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'login:index')
    else:
        form = AuthenticationForm
    
    # 회원 리스트
    users = get_user_model().objects.order_by('pk')

    context = {
        'users' : users,
        'form' : form
    }

    return render(request, 'login/index.html', context)

def signup(request):
    # 회원가입 로직
    if request.method == 'POST':
        new_form = CustomUserCreationForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            return redirect('login:index')

    else:    
        new_form = CustomUserCreationForm()

    # 로그인 로직
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'login:index')
    else:
        form = AuthenticationForm

    context = {
        'new_form' : new_form,
        'form' : form
    }

    return render(request, 'login/signup.html', context)

@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    
    context = {
        'user' : user
    }

    return render(request, 'login/detail.html', context)

def login(request):
    # 로그인 로직
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'login:index')
    else:
        form = AuthenticationForm

    context = {
        'form' : form
    }
    return render(request, 'login/index.html', context)

@login_required
def logout(request):

    auth_logout(request)

    return redirect('login:index')
    

