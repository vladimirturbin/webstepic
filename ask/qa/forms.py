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

    def __init__(self, question_number, *args, **kwargs):
        self.question_number = question_number
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean_text(self):
        text = self.cleaned_data['text']
        return text

    def save(self):
        self.cleaned_data['question'] = \
            Question.objects.get(id=self.question_number)
        answer = Answer(**self.cleaned_data)
        print(answer)
        answer.save()
        return answer
