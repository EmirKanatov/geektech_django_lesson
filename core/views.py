from django.shortcuts import render, HttpResponse, redirect
from .models import Feedback
from django.contrib.auth import login, authenticate
from .forms import FeedbackCreateForm, SignInForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def feedback_view(request):
    if request.method == "POST":
        data = request.POST
        feedback = Feedback()
        feedback.first_name = data["first_name"]
        feedback.rating = data['rating']
        feedback.text = data["text"]
        feedback.contact = data["contact"]
        feedback.save()
        return HttpResponse("Ваш отзыв принят. Спасибо!!!")

    return render(request, "feedback.html")


def feedback_form_view(request):
    context = {}
    if request.method == "POST":
        feedback_create_form = FeedbackCreateForm(request.POST)
        feedback_create_form.save()
        return HttpResponse("Ваш отзыв принят. Спасибо!!!")

    feedback_create_form = FeedbackCreateForm()
    context['feedback_create_form'] = feedback_create_form
    return render(request, "feedback_form.html", context)


def sign_in(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return HttpResponse('Авторизация провалена')
    context = {"auth_form": SignInForm()}
    return render(request, 'sign-in.html', context)


def log_in(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-in')

    context = {'form': form}
    return render(request, "register_page.html", context)

