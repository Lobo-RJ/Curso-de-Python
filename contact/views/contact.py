from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from contact.models import Contact
from contact.forms import ContactForm


def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')

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
    # contact = Contact.objects.filter(pk=contact_id).first()
    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'page_title': 'Contato',
        'contact': contact
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
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()

    if form.is_valid():
        # para salvar os dados do formulário sem alterações
        contact = form.save()

        # # para salvar os dados do formulário com alterações antes do commit
        # contact = form.save(commit=False)
        # contact.show = True
        # contact.save()

        # após salvar os dados do formulário, redireciona para um formulário limpo (GET)
        return redirect('contact:update', contact_id=contact.pk)

    context = {
        'page_title': 'Cria Contato',
        'form': form,
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
    else:
        form = ContactForm(instance=contact)

    if form.is_valid():
        # para salvar os dados do formulário sem alterações adicionais nos campos
        form.save()

        # após salvar os dados do formulário, redireciona para um formulário limpo (GET)
        return redirect('contact:list')

    context = {
        'page_title': 'Cria Contato',
        'form': form,
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirmation = request.POST.get('confirmation', 'no')
    print('confirmation = ', confirmation)

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:list')

    context = {
        'page_title': 'Cria Contato',
        'contact': contact,
        'confirmation': confirmation
    }

    return render(
        request,
        'contact/detail.html',
        context
    )
