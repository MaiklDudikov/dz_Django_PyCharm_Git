from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/edit/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<int:pk>/', views.delete_customer, name='delete_customer'),  # Маршрут для удаления покупателя
    path('sellers/', views.seller_list, name='seller_list'),
    path('sellers/add/', views.add_seller, name='add_seller'),
    path('sellers/edit/<int:pk>/', views.edit_seller, name='edit_seller'),
    path('sellers/delete/<int:pk>/', views.delete_seller, name='delete_seller'),  # Маршрут для удаления продавца
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),  # Маршрут для удаления товара
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/add/', views.add_sale, name='add_sale'),
    path('sales/edit/<int:pk>/', views.edit_sale, name='edit_sale'),
    path('sales/delete/<int:pk>/', views.delete_sale, name='delete_sale'),  # Маршрут для удаления продажи
    path('report/customers_by_seller/<int:seller_id>/', views.customers_by_seller, name='customers_by_seller'),
    path('report/sales_by_date/<str:date>/', views.sales_by_date, name='sales_by_date'),
    path('report/top_selling_product/', views.top_selling_product, name='top_selling_product'),
    # Добавьте маршруты для других отчётов...
]
