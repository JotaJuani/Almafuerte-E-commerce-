from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages


def logoutUser(request):
    logout(request)
    return redirect('account:login')


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        print('USER:', username)
        print('password', password)
        if user is not None:
            login(request, user)
            return redirect('shop:product_list')
        else:
            print('Authentication failed')
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'account/login_register.html', {'page': page})


def register_User(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username,
                                password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('shop:product_list')
            else:
                messages.error(
                    request, 'Registration failed. Please try again.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(error)
                    messages.error(request, f"{error}")

    context = {'form': form, 'page': page}
    return render(request, 'account/login_register.html', context)
