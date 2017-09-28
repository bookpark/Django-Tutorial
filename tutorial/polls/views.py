from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    question_list = Question.objects.order_by('-published_date')
    context = {
        'question_list': question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question,

    }
    return render(request, 'polls/detail.html', context)


def results(request, pk):
    return HttpResponse(f"You're looking at the results of question {pk}")


def vote(request, pk):
    return HttpResponse(f"You're voting on question {pk}")
