from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category


def home(request):
    return HttpResponse('home page')

def product_list(request):
    products = Product.objects.all()
    products_json = [p.to_json() for p in products]
    return JsonResponse(products_json, safe=False)

def product_details(request, product_id):
    products = Product.objects.all()
    for p in products:
        if p.id == product_id:
            return JsonResponse(p.to_json())

def category_list(request):
    categories = Category.objects.all()
    categories_json = [c.to_json() for c in categories]
    return JsonResponse(categories_json, safe=False)

def category_details(request, category_id):
    categories = Category.objects.all()

    for c in categories:
        if c.id == category_id:
            return JsonResponse(c.to_json())

def category_product_list(request, category_id):
    products = Product.objects.all()
    result = []
    for p in products:
        if p.category == category_id:
            result.append(p.to_json())
    return JsonResponse(result, safe=False)
