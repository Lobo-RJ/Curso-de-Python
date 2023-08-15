from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # contact SEARCH
    path('search/',
         views.search, name='contact_search'),
    # contact LIST
    path('',
         views.index, name='contact_list'),

    # contact CRUD
    path('contact/create/',
         views.create, name='contact_create'),
    path('contact/<int:contact_id>',
         views.detail, name='contact_detail'),
    path('contact/<int:contact_id>/update/',
         views.update, name='contact_update'),
    path('contact/<int:contact_id>/delete/',
         views.delete, name='contact_delete'),
]
