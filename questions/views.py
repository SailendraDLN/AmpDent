from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Question
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm
# Create your views here.
def question_view(request, id=None):
    question_obj = None
    if id is not None:
        question_obj = Question.objects.get(id=id)
    context = { "object": question_obj }
    return render(request, "qa/question.html", context=context)

def question_search_view(request):
    query_dict = request.GET
    #print(query_dict)
    query = query_dict.get("q")
    question_objs = None
    if query is not None:
        question_objs = Question.objects.filter(marks=query)
    context = {
        "objects": question_objs
    }
    return render(request,"qa/search.html",context=context)

#@login_required
# def question_create_view(request):
#     context = {}
#     if request.method == "POST":

#         topic = request.POST.get("topic")
#         content = request.POST.get("content")
#         marks = request.POST.get("marks")
#         asked = request.POST.get("asked")
#         subject = request.POST.get("subject")

#         question_obj = Question.objects.create(
#             topic = topic,
#             content = content,
#             marks = marks,
#             asked = asked,
#             subject = subject
#         )

#         context["object"] = question_obj
#         context["created"] = True
#     return render(request, "qa/create.html", context=context)

@login_required
def question_create_view(request):
    form = QuestionForm(request.POST or None)
    context = { "form": form }
    if form.is_valid():
        question_obj = form.save()
        context["object"] = question_obj
        context["created"] = True
    return render(request, "qa/create.html", context=context)