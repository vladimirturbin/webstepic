from django import forms
from .models import Question


class AskForm(forms.Form):
    title = forms.CharField(max_length=128)
    text = forms.CharField(widget=forms.TextInput)

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
