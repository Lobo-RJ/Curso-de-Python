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
    # user CRUD
    path('user/register/',
         views.register, name='register'),
    path('user/login/',
         views.login, name='login'),
    path('user/logout/',
         views.logout, name='logout'),
    path('user/update/',
         views.user_update, name='user_update'),
]
