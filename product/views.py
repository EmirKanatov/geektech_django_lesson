from django.shortcuts import render, HttpResponse, redirect
from .models import Vegetables, Categories
from .forms import VegetableCreateForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def homepage(request):
    products = Vegetables.objects.all()
    context = {"all_vegetables": products}
    return render(request, "product_list.html", context)


def category(request):
    category_objects = Categories.objects.all()
    context = {"all_categories": category_objects}
    return render(request, "category_list.html", context)


def pricing_table(request):
    return render(request, "price_table.html")


def vegetable_detail(request, id):
    try:
        vegetable = Vegetables.objects.get(id=id)
        context = {'vegetable' : vegetable}
        return render(request, 'vegetable_info.html', context)
    except ObjectDoesNotExist:
        return HttpResponse("Такой страницы не существует", status=404)


def category_detail(request, id):
    category_obj = Categories.objects.get(id=id)
    vegetable_list = Vegetables.objects.filter(category=category_obj)
    context = {'all_vegetables' : vegetable_list}
    return render(request, "product_list.html", context)


def vegetable_add(request):
    context = {}

    if request.method == "GET":
        vegetable_form = VegetableCreateForm()
        context['vegetable_form'] = vegetable_form
        return render(request, "vegetable_form.html", context)
    elif request.method == "POST":
        vegetable_form = VegetableCreateForm(request.POST)
        if vegetable_form.is_valid():
            new_vegetable = vegetable_form.save()
            return redirect(vegetable_detail, id=new_vegetable.id)
        else:
            return HttpResponse("Форма не валидна", status=400)


def vegetable_update(request, id):
    context = {}
    vegetable_obj = Vegetables.objects.get(id=id)

    if request.method == "POST":
        vegetable_form = VegetableCreateForm(request.POST, instance=vegetable_obj)
        if vegetable_form.is_valid():
            vegetable_obj = vegetable_form.save()
            return HttpResponse("Данные сохранены")

    vegetable_form = VegetableCreateForm(instance=vegetable_obj)
    context['vegetable_form'] = vegetable_form
    return render(request, 'vegetable_form.html', context)


def vegetable_delete(request, id):
    if request.method == "POST":
        vegetable_object = Vegetables.objects.get(id=id)
        vegetable_object.delete()
        return HttpResponse("Информация успешно удалена")
