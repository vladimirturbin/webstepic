# This Python file uses the following encoding: utf-8

from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=128)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[-1] != '?':
            raise forms.ValidationError('Заголовок должен включать вопрос',
                                        code='No_answer_in_title')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    def save(self, question):
        self.cleaned_data['question'] = question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
