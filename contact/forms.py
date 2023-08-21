from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        label='Foto',
        required=False
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email',
            'description', 'category', 'picture',
        )

        # terceira forma para alterar um widget
        widgets = {
            'first_name': forms.TextInput(attrs={
                'input_type': 'text',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'input_type': 'text',
                'class': 'form-control'
            }),
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
            }),
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

        if len(first_name) < 2:
            self.add_error(
                'first_name',
                ValidationError(
                    'O nome deve ter no mínimo 2 caracteres',
                    code='invalid'
                )
            )

        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        min_length=3,
        max_length=30,
        required=True,
        label='Nome',
        help_text='Obrigatório. Máximo = 30 caracteres'
    )

    last_name = forms.CharField(
        min_length=3,
        max_length=30,
        required=True,
        label='Sobrenome',
        help_text='Obrigatório. Máximo = 30 caracteres'
    )

    email = forms.EmailField(
        max_length=150,
        required=True,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                email,
                ValidationError(
                    'Já existe um registro com este e-mail', code='invalid')
            )

        return email


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        label='Nome',
        help_text='Obrigatório. Máximo = 30 caracteres'
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        label='Sobrenome',
        help_text='Obrigatório. Máximo = 30 caracteres'
    )

    email = forms.EmailField(
        max_length=150,
        required=True,
    )

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Digite a mesma senha para confirmação",
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError(
                        'As senhas devem ser iguais', code='invalid')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    email,
                    ValidationError(
                        'Já existe um registro com este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))

        return password1
