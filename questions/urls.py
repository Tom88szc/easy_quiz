from django.urls import path

from . import views

urlpatterns = [
    path('', views.answer_list, name='list'),
    path('<int:question_id>/', views.question, name='question'),
    path('<int:question_id>/answer', views.answer, name='answer'),
    path('<int:question_id>/results', views.question, name='results'),
]

app_name = 'questions'
