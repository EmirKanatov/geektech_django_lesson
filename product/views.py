from django.shortcuts import render, HttpResponse, redirect
from django.template.defaulttags import url

from core.decorators import should_be_staff
from .models import Vegetables, Categories
from .forms import VegetableCreateForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView


# Create your views here.


# def homepage(request):
#     products = Vegetables.objects.all()
#     context = {"all_vegetables": products}
#     return render(request, "product_list.html", context)


class VegetableListAsView(ListView):
    model = Vegetables
    template_name = "product_list.html"

    queryset = Vegetables.objects.filter(is_available=True)


class CategoryListView(ListView):
    model = Categories
    template_name = "category_list.html"


# def category(request):
#     category_objects = Categories.objects.all()
#     context = {"all_categories": category_objects}
#     return render(request, "category_list.html", context)


def pricing_table(request):
    return render(request, "price_table.html")


def vegetable_detail(request, id):
    try:
        vegetable = Vegetables.objects.get(id=id)
        context = {'vegetable': vegetable}
        return render(request, 'vegetable_info.html', context)
    except ObjectDoesNotExist:
        return HttpResponse("Такой страницы не существует", status=404)


class VegetableDetailAsView(DetailView):
    model = Vegetables
    template_name = "vegetable_info.html"


# def category_detail(request, id):
#     category_obj = Categories.objects.get(id=id)
#     vegetable_list = Vegetables.objects.filter(category=category_obj)
#     context = {'all_vegetables': vegetable_list}
#     return render(request, "product_list.html", context)


class CategoryDetailAsView(DetailView):
    model = Categories
    template_name = "product_list.html"

    def get_object(self):
        return Categories.objects.get(id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Vegetables.objects.filter(category=self.object)
        return context


@login_required(login_url='/sign-in/')
@should_be_staff
#   @permission_required("product.add_vegetables")
def vegetable_add(request):
    #   if not request.user.is_staff:
    #   return HttpResponse("У вас нет доступа!!!", status=403)
    context = {}

    if request.method == "GET":
        vegetable_form = VegetableCreateForm()
        context['vegetable_form'] = vegetable_form
        return render(request, "vegetable_form.html", context)
    elif request.method == "POST":
        vegetable_form = VegetableCreateForm(request.POST)
        if vegetable_form.is_valid():
            new_vegetable = vegetable_form.save()
            return redirect('vegetables', pk=new_vegetable.id)
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
