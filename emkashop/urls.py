"""emkashop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product.views import homepage, category, pricing_table, vegetable_add, vegetable_detail, category_detail,\
    vegetable_update, vegetable_delete
from core.views import feedback_view, feedback_form_view, sign_in, log_in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('categories/', category, name='categories'),
    path('categories/<int:id>/', category_detail, name='category'),
    path('pricing_table/', pricing_table, name='homepage'),
    path('vegetables/<id>', vegetable_detail, name='vegetables'),
    path('vegetable-add/', vegetable_add, name='vegetable_add'),
    path('vegetables/update/<id>', vegetable_update, name='vegetable-update'),
    path('vegetables/delete/<id>', vegetable_delete, name='vegetable-delete'),
    path('feedback/', feedback_view, name='feedback'),
    path('feedback_form/', feedback_form_view, name='feedback_form'),
    path('sign-in/', sign_in, name="sign-in"),
    path('log-in', log_in, name='log-in')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
