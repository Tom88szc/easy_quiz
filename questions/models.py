from django.db import models


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200)
    createDate = models.DateTimeField('date created')

    def __str__(self):
        return self.text

    @property
    def correct_percent(self):
        answers = self.answer_set.all()
        total = sum(a.answered_count for a in answers)

        if total > 0:
            correct = sum(a.answered_count for a in answers if a.correct)
            return round(correct / total * 100, 2)
        else:
            return None


class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    answered_count = models.IntegerField(default=0)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
