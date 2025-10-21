from django.urls import path
from .views import DashboardView, ContractUploadView, ContractReportView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("upload/", ContractUploadView.as_view(), name="contracts_upload"),
    path("report/", ContractReportView.as_view(), name="contracts_report"),
]