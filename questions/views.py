from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from urllib.parse import urlencode
# Create your views here.
from django.utils import timezone
from questions.forms import QuestionForm
from questions.models import Question, Answer


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


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Question.objects.create(text=text, created=timezone.now())
            return HttpResponseRedirect(reverse('questions:list'))
    else:
        form = QuestionForm
    return render(request, 'questions/create.html', {'form': form})


def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        answer_id = request.POST['answer']
        selected = question.answer_set.get(pk=answer_id)
    except (KeyError, Answer.DoesNotExist):
        ctx_err = {
            'questions': question,
            'error': 'Zaznacz odpowiedź!'
        }
        return render(request, 'questions/question.html', ctx_err)

    selected.answered_count += 1
    selected.save()
    url = reverse('questions:results', args=(question.id,))
    query_result = urlencode({'answer': answer_id})
    return HttpResponseRedirect(f'{url}?{query_result}')


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ctx = {
        'question': question,
        'answer_id': int(request.GET['answer']),
    }
    return render(request, 'questions/results.html', ctx)
