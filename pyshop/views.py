from django.shortcuts import render
from .models import Product, live_search


# def index(request):
#     product_list = Product.objects.all()
#     context = {'product_list': product_list}
#     return render(request, 'pyshop/livesearch_results.html', context)

def index(request):
    product_list = Product.objects.all()
    # product_list.live_search()
    context = {'product_list': product_list}
    return render(request, 'pyshop/livesearch_results.html', context)
