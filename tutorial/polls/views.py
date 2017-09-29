from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'polls/index.html', context)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def vote(request, pk):
    if request.method == 'POST':
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return redirect('index')
        try:
            choice_pk = request.POST['choice']
            choice = Choice.objects.get(pk=choice_pk)
            choice.votes += 1
            choice.save()
        except MultiValueDictKeyError:
            print('Key Error!')
        except Choice.DoesNotExist:
            print('Does Not Exist!')
        return redirect('detail', pk=question.pk)
    return HttpResponse('Permission Denied', status=403)


def results(request, pk):
    return HttpResponse(f"You're looking at the results of question {pk}")
