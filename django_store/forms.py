from django import forms 
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username= forms.CharField(label= 'Nombre de usuario',min_length=4, max_length=20, required=True, widget=forms.TextInput(attrs={
        'id':'username',
        'class': 'p-1 mt-1 w-72 mb-2 | border-2 border-blue-icons rounded-md | transition-shadow | focus:shadow-lg focus:outline-none focus:ring-4 focus:ring-blue-300 focus:ring-opacity-50',
        'placeholder': 'Escriba su nombre de usuario'}))
    email=  forms.EmailField(label= 'Email',required=True, widget=forms.EmailInput(attrs={
        'id':'email',
        'class': 'p-1 mt-1 w-72 mb-2 | border-2 border-blue-icons rounded-md | transition-shadow | focus:shadow-lg focus:outline-none focus:ring-4 focus:ring-blue-300 focus:ring-opacity-50',
        'placeholder': 'ejemplo@ejemplo.com'
        }))
    password= forms.CharField(label= 'Contraseña',min_length=4, max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'id':'password',
        'class': 'p-1 mt-1 w-72 mb-2 | border-2 border-blue-icons rounded-md | transition-shadow | focus:shadow-lg focus:outline-none focus:ring-4 focus:ring-blue-300 focus:ring-opacity-50',
        'placeholder': 'Escriba su contraseña',
        }))
    repeated_password= forms.CharField(label='Confirmar contraseña',min_length=4, max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'id':'repeated_password',
        'class': 'p-1 mt-1 w-72 mb-2 | border-2 border-blue-icons rounded-md | transition-shadow | focus:shadow-lg focus:outline-none focus:ring-4 focus:ring-blue-300 focus:ring-opacity-50',
        'placeholder': 'Repita la contraseña',
        }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError("El nombre de usuario ingresado ya se encuentra en uso.")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("El email ingresado ya se encuentra en uso.")

        return email

    def clean(self): # 'clean' Se usa para validar campos que dependan de otro
        cleaned_data = super().clean()

        if cleaned_data.get('repeated_password') != cleaned_data.get('password'):
            self.add_error('repeated_password', 'Las contraseñas ingresadas no coinciden, verifique los campos y vuelva a intentarlo.')