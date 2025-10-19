from django.urls import path
from .views import CustomLoginView, CustomLogoutView, UserCreateView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("create/", UserCreateView.as_view(), name="create_user"),
]