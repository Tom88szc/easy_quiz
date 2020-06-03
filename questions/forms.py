from django import forms


class QuestionForm(forms.Form):
    text = forms.CharField(label="Pytanie", max_length=100, min_length=10)
