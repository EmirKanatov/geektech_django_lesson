from django.shortcuts import render


# Create your views here.
def feedback_view(request):
    return render(request, "feedback.html")
