from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # campos que serão apresentados na lista
    list_display = ['id', 'first_name', 'last_name', 'phone',
                    'email', 'show', 'created_date', 'modified_date']
    # campos usados para ordenação. O sinal '-' indica a ordem decrescente
    ordering = ['-id']
    # campos utilizados para filtro
    list_filter = ['created_date', 'category', 'owner']
    # campos de busca
    search_fields = ['first_name', 'last_name', 'email']
    # campos editáveis na lista
    list_editable = ['show']
    # quantidade de registros mostrados por página
    list_per_page = 10
    # quantidade de registros mostrados ao selecionar 'Mostrar tudo'
    list_max_show_all = 200


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 20
    list_max_show_all = 200
