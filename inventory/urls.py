from django.urls import path

from .views import (
    InventoryListView,
    InventoryDetailView,
    InventoryDeleteView,
    InventoryUpdateView,
    InventoryCreateView,
)

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory_list'),
    path('<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory_delete'),
    path('<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory_edit'),
    path('new/', InventoryCreateView.as_view(), name='inventory_new'),
]