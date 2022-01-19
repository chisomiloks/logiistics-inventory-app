from nntplib import ArticleInfo
from django.views.generic import (
    DetailView, 
    ListView,
)
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse_lazy

from .models import Inventory


# Create your views here.
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory_list.html'
    context_object_name = 'latest_inventory_list'


class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory_detail.html'


class InventoryDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Inventory
    template_name = 'inventory_delete.html'
    success_url = reverse_lazy('inventory_list')

    def test_func(self):
        obj = self.get_object()
        return obj.merchant == self.request.user or self.request.user.is_superuser


class InventoryUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Inventory
    template_name = 'inventory_edit.html'
    fields = ('title', 'description', 'specifications', 'manufacturer', 'quantity')
    context_object_name = 'updated_inventory_list'

    def test_func(self):
        obj = self.get_object()
        return obj.merchant == self.request.user or self.request.user.is_superuser


class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    template_name = 'inventory_new.html'
    fields = ('title', 'description', 'specifications', 'manufacturer', 'quantity')

    def form_valid(self, form):
        form.instance.merchant = self.request.user
        return super().form_valid(form)