from django.urls import path
from .views import products_view, products_detail_view, category_list_view

app_name = 'shop'

urlpatterns = [
    path('', products_view, app_name='products'),
    path('<slug:slug>/', products_detail_view, app_name='product_detail'),
    path('search/<slug:slug>/', category_list_view, app_name='category_list'),
]
