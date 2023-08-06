from django.shortcuts import render


def index(request):
    return render(
        request,
        template_name='contact/index.html',
        context={'title': 'Agenda'}
    )
