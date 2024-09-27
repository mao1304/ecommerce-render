from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account

class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_admin', 'is_staff')

    def clean_password2(self):
        # Verifica que las dos contraseñas ingresadas coincidan
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Guarda la contraseña proporcionada en forma hasheada
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AccountChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin', 'is_staff')

    def clean_password(self):
        # Retorna el valor inicial del campo de contraseña
        return self.initial["password"]