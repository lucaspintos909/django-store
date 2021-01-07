from django import forms 


class RegisterForm(forms.Form):
    username= forms.CharField(min_length=4, max_length=20, required=True, widget=forms.TextInput(attrs={
        'id':'username',
        'class': 'p-1 mt-1 w-72 mb-4 | border-2 border-blue-icons rounded-md | transition-shadow | focus:shadow-lg focus:outline-none focus:ring-4 focus:ring-blue-300 focus:ring-opacity-50',
        'placeholder': 'Escriba su nombre de usuario'
    }))
    email=  forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'id':'email',
        'class': 'p-1 mt-1 w-72 mb-4 | border-2 border-blue-icons rounded-md | transition-shadow | focus:shadow-lg focus:outline-none focus:ring-4 focus:ring-blue-300 focus:ring-opacity-50',
        'placeholder': 'ejemplo@ejemplo.com'
        }))
    password= forms.CharField(min_length=4, max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'id':'password',
        'class': 'p-1 mt-1 w-72 mb-4 | border-2 border-blue-icons rounded-md | transition-shadow | focus:shadow-lg focus:outline-none focus:ring-4 focus:ring-blue-300 focus:ring-opacity-50',
        'placeholder': 'Escriba su contraseña',
        }))