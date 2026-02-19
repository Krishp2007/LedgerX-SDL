from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.product_add, name='product_add'),
    path('out-of-stock/', views.product_out_of_stock, name='product_out_of_stock'), # 🟢 New URL
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('<int:product_id>/deactivate/', views.product_deactivate, name='product_deactivate'),
    path('low-stock/', views.product_low_stock, name='product_low_stock'), # 🟢 New URL for low stock products

    path('export/', views.export_inventory_csv, name='export_inventory_csv'),

]
