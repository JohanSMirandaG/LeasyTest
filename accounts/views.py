from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

class CustomLogoutView(LogoutView):
    next_page = "login"

def admin_required(user):
    return user.is_superuser or user.is_staff

@method_decorator(user_passes_test(admin_required), name='dispatch')
class UserCreateView(CreateView):
    form_class = CreateUserForm
    template_name = "accounts/create_user.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        messages.success(self.request, "Usuario creado exitosamente ✅")
        return super().form_valid(form)