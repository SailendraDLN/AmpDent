from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from questions.models import Question

def home_view(request):
    question_obj = Question.objects.all()
    context = {
        "objects": question_obj
    }
    return render(request, "home_view.html", context=context)