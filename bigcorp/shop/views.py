from django.shortcuts import render, get_object_or_404
from .models import Product, ProductManager, ProductProxy, Category


# Create your views here.
def products_view(request):
    products = ProductProxy.objects.all()
    return render(request, template_name='shop/products.html', context={'products': products})


def products_detail_view(request, slug):
    product = get_object_or_404(ProductProxy, slug=slug)
    return render(request, template_name='shop/product_detail.html', context={'product': product})


def category_list_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = ProductProxy.objects.select_related('category').filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, template_name='shop/category_list.html', context=context)