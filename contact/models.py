from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    first_name = models.CharField(max_length=30, verbose_name='Nome')
    last_name = models.CharField(
        max_length=30, blank=True, verbose_name='Sobrenome')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.EmailField(max_length=255, verbose_name='Email')
    description = models.TextField(blank=True, verbose_name='Descrição')
    show = models.BooleanField(default=True, verbose_name='Mostrar')
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name='Data de Criação')
    modified_date = models.DateTimeField(
        default=timezone.now, verbose_name='Data de Modificação')
    picture = models.ImageField(
        blank=True, upload_to='pictures/%Y/%m/%d', verbose_name='Foto')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Categoria')
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Proprietário')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
