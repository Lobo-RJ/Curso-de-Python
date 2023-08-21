from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid:
            form.save()
            messages.success(request, 'Registro realizado com sucesso!')

            return redirect('contact:login')

    context = {
        'page_title': 'Registro',
        'form': form
    }

    return render(
        request,
        'contact/register.html',
        context
    )


def login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso')
            return redirect('contact:list')

        messages.error(request, 'Login inválido')

    context = {
        'page_title': 'Login',
        'form': form
    }

    return render(
        request,
        'contact/login.html',
        context
    )


@login_required(login_url='contact:login')
def logout(request):
    auth.logout(request)
    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    # user = request.user

    # if not user.is_authenticated:
    #     messages.warning(
    #         request, 'É necessário estar logado para atualizar dados do usuário')
    #     return redirect('contact:login')

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'O usuário foi atualizado com sucesso')
            return redirect('contact:login')
    else:
        form = RegisterUpdateForm(instance=request.user)

    context = {
        'page_title': 'Atualiza Usuário',
        'form': form
    }

    return render(
        request,
        'contact/register.html',
        context
    )
