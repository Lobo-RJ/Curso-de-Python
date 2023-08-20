from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # contact SEARCH
    path('search/',
         views.search, name='search'),
    # contact LIST
    path('',
         views.index, name='list'),

    # contact CRUD
    path('contact/create/',
         views.create, name='create'),
    path('contact/<int:contact_id>',
         views.detail, name='detail'),
    path('contact/<int:contact_id>/update/',
         views.update, name='update'),
    path('contact/<int:contact_id>/delete/',
         views.delete, name='delete'),
]
