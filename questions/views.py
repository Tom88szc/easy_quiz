from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    question = {
        'text': 'Jak bardzo wysoki jest Mount Everest',
        'answers': [
            {'text': '3323 m', 'correct': False},
            {'text': '8999 m', 'correct': False},
            {'text': '8848 m', 'correct': True},
            {'text': '3323 m', 'correct': False},
        ]
    }
    ctx = {
        'question': question,
    }
    return render(request, 'questions/question.html', ctx)
