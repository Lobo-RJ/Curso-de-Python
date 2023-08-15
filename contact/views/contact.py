from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('id')

    paginator = Paginator(contacts, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_title': 'Contatos',
        'page_obj': page_obj
    }

    return render(
        request,
        'contact/index.html',
        context,
    )


def detail(request, contact_id):
    # contact_data = Contact.objects.filter(pk=contact_id).first()
    contact_data = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'page_title': 'Contato',
        'contact': contact_data
    }

    return render(
        request,
        'contact/detail.html',
        context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if not search_value:
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(phone__icontains=search_value)
        ) \
        .order_by('id')

    paginator = Paginator(contacts, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_title': 'Busca',
        'page_obj': page_obj
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def create(request):

    context = {
        'page_title': 'Cria Contato',
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def update(request, contact_id):
    contact_data = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'page_title': 'Atualiza Contato',
        'contact': contact_data
    }

    return render(
        request,
        'contact/update.html',
        context
    )


def delete(request, contact_id):
    contact_data = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'page_title': 'Excluir Contato',
        'contact': contact_data
    }

    return render(
        request,
        'contact/delete.html',
        context
    )
