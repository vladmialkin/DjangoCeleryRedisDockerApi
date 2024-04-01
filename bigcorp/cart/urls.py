from django.urls import path
from .views import cart_view


app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart'),
    # path('<slug:slug>/', products_detail_view, name='product_detail'),
    # path('search/<slug:slug>/', category_list_view, name='category_list'),
]
