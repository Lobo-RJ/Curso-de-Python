from django import forms
from django.core.exceptions import ValidationError

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
            'description', 'category',
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
            'category': forms.Select(attrs={
                'class': 'form-select',
            })
        }

    # usado para mais de um campo
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'O conteúdo do campo nome não pode ser igual ao sobrenome', code='invalid')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    # usado para campos individuais
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if len(first_name) < 3:
            self.add_error(
                'first_name',
                ValidationError(
                    'O nome deve ter no mínimo 3 caracteres',
                    code='invalid'
                )
            )

        return first_name
