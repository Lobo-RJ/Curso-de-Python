from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # campos que serão apresentados na lista
    list_display = ['id', 'first_name', 'last_name', 'phone',
                    'email', 'created_date', 'modified_date']

    # campos usados para ordenação. O sinal '-' indica a ordem decrescente
    ordering = ['-id']

    # campos utilizados para filtro
    list_filter = ['created_date']

    # campos de busca
    search_fields = ['first_name', 'last_name', 'email']

    # quantidade de registros mostrados por página
    list_per_page = 20

    # quantidade de registros mostrados ao selecionar 'Mostrar tudo'
    list_max_show_all = 200
