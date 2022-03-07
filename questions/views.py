from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Question
# Create your views here.
def question_view(request, id=None):
    question_obj = None
    if id is not None:
        question_obj = Question.objects.get(id=id)
    context = { "object": question_obj }
    return render(request, "qa/question.html", context=context)