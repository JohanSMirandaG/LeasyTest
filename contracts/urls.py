from django.urls import path
from .views import DashboardView, ContractUploadView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("upload/", ContractUploadView.as_view(), name="contracts_upload"),
]