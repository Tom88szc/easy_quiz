from django.contrib import admin
from questions.models import Question, Answer


# Register your models here.

class AnswerInLane(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLane]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)
