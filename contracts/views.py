from django.views.generic import ListView
from django.db.models import Q
from .models import Contract
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, ListView):
    model = Contract
    template_name = "contracts/dashboard.html"
    context_object_name = "contracts"
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get("q")
        qs = Contract.objects.select_related("client", "car").order_by("id")
        if query:
            qs = qs.filter(
                Q(client__first_name__icontains=query) |
                Q(client__last_name__icontains=query) |
                Q(client__document_number__icontains=query) |
                Q(car__plate__icontains=query)
            )
        return qs