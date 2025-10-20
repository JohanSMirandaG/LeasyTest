from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "id_password1"}),
        help_text="Debe tener entre 4 y 15 caracteres."
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "id_password2"}),
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre",
                "id": "id_first_name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Apellido",
                "id": "id_last_name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Correo electrónico",
                "id": "id_email"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name", "").strip()
        last_name = cleaned_data.get("last_name", "").strip()
        email = cleaned_data.get("email", "").strip()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if not first_name:
            raise forms.ValidationError("El campo 'Nombre' es obligatorio.")
        if not last_name:
            raise forms.ValidationError("El campo 'Apellido' es obligatorio.")
        if not email:
            raise forms.ValidationError("El campo 'Correo electrónico' es obligatorio.")

        if not password1 or not password2:
            raise forms.ValidationError("Debe ingresar y confirmar la contraseña.")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        if len(password1) < 4:
            raise forms.ValidationError("La contraseña debe tener al menos 4 caracteres.")
        if len(password1) > 15:
            raise forms.ValidationError("La contraseña no puede tener más de 15 caracteres.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con este correo electrónico.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user