from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

class CustomLogoutView(LogoutView):
    next_page = "login"

User = get_user_model()

class UserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "accounts/create_user.html"
    success_url = reverse_lazy("dashboard")

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para crear usuarios.")
        return redirect("dashboard")

    def form_valid(self, form):
        messages.success(self.request, f"Usuario '{form.cleaned_data['email']}' creado exitosamente.")
        return super().form_valid(form)