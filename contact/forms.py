from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact


class ContactForm(forms.ModelForm):
    # primeira forma para alterar um widget
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Nome',
    )

    # segunda forma para alterar um widget
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email',
            'description', 'show', 'created_date', 'modified_date',
        )
        # terceira forma para alterar um widget
        widgets = {
            'phone': forms.TextInput(attrs={
                'input_type': 'text',
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'input_type': 'email',
                'class': 'form-control',
                'help_text': 'Nós nunca forneceremos o seu email para ninguém.'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'show': forms.CheckboxInput(),
            'created_date': forms.DateTimeInput(),
            'modified_date': forms.DateTimeInput(),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                'Mensagem de Erro',
                code='invalid'
            )
        )

        return super().clean()
