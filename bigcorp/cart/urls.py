from django.urls import path


app_name = 'cart'

urlpatterns = [
    path('', products_view, name='products'),
    path('<slug:slug>/', products_detail_view, name='product_detail'),
    path('search/<slug:slug>/', category_list_view, name='category_list'),
]
