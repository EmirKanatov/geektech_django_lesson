from django.shortcuts import render, HttpResponse
from .models import Vegetables, Categories


# Create your views here.
def homepage(request):
    products = Vegetables.objects.all()
    context = {"all_vegetables": products}
    return render(request, "product_list.html", context)


def pomidor(request):
    pomidor_object = Vegetables.objects.get(id=1)
    desc = pomidor_object.description
    return render(request, "pomidor.html")


def category(request):
    category_objects = Categories.objects.all()
    context = {"all_categories": category_objects}
    return render(request, "category_list.html", context)


def pricing_table(request):
    return render(request, "price_table.html")


def vegetable_detail(request, id):
    vegetable = Vegetables.objects.get(id=id)
    context = {'vegetable' : vegetable}
    return render(request, 'vegetable_info.html', context)


def category_detail(request, id):
    category_obj = Categories.objects.get(id=id)
    vegetable_list = Vegetables.objects.filter(category=category_obj)
    context = {'all_vegetables' : vegetable_list}
    return render(request, "product_list.html", context)
