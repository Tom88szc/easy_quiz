from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from questions.models import Question


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ctx = {
        'question': question,
    }
    return render(request, 'questions/question.html', ctx)


def answer_list(request):
    ctx = {
        'questions': Question.objects.all()
    }
    return render(request, 'questions/list.html', ctx)


def answer(request, question_id):
    return HttpResponse(f'Odpowiedziałeś na Pytanie: {question_id}')


def results(request, question_id):
    return HttpResponse(f'Wyniki dla pytania: {question_id}')
