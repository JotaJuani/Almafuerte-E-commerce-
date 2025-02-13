from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

def logoutUser(request):
    logout(request)
    return redirect('account:login')


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']

        user = User.objects.filter(email=username_or_email).first() or \
            User.objects.filter(username=username_or_email).first()

        if user and user.check_password(password):
            login(request, user)
            next_url = request.GET.get('next', '/shop/home')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrecta')

    return render(request, 'account/login_register.html', {'page': page})


def register_User(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()

            user = authenticate(request, username=user.username,
                                password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('shop:product_list')
            else:
                messages.error(
                    request, 'El registro falló. Por favor intentelo nuevamente.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(error)
                    messages.error(request, f"{error}")

    context = {'form': form, 'page': page}
    return render(request, 'account/login_register.html', context)

def password_reset(request):
    return render(request, 'account/password_reset_email.html')

def password_reset_form(request):
    return render(request, 'account/password_reset_form.html')