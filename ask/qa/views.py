from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .forms import AskForm, AnswerForm
from .models import Question, Answer


class IndexView(View):
    def get(self, request, *args, **kwargs):
        try:
            page = int(request.GET.get('page', 1))
        except TypeError:
            page = 1
        try:
            limit = int(request.GET.get('limit', 10))
        except TypeError:
            limit = 10

        paginator = Paginator((Question.objects.new()), limit)
        # paginator = Paginator(Question.objects.all(), limit)
        paginator.baseurl = '/?page='
        page = paginator.page(page)

        return render(request, 'templates/main.html',
                      {
                          'questions': page.object_list,
                          'paginator': paginator,
                          'page': page,
                      })


class QuestionView(View):
    def get(self, request, question_number, *args, **kwargs):
        question = get_object_or_404(Question, id=question_number)
        answers = Answer.objects.filter(question=question)
        form = AnswerForm()
        return render(request, 'templates/question.html',
                      {'question': question,
                       'answers': answers,
                       'form': form})

    def post(self, request, question_number, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():

            question = get_object_or_404(Question, id=question_number)
            form.save(question=question)
            return HttpResponseRedirect(question.get_absolute_url())
        else:
            question = get_object_or_404(Question, id=form.question_number)
            answers = Answer.objects.filter(question=question)
            return render(request, 'templates/question.html',
                          {'question': question,
                           'answers': answers,
                           'form': form})


class PopularView(View):
    def get(self, request, *args, **kwargs):
        try:
            page = int(request.GET.get('page', 1))
        except TypeError:
            page = 1
        try:
            limit = int(request.GET.get('limit', 10))
        except TypeError:
            limit = 10

        paginator = Paginator((Question.objects.popular()), limit)
        # paginator = Paginator(Question.objects.all(), limit)
        paginator.baseurl = '/popular/?page='
        page = paginator.page(page)

        return render(request, 'templates/main.html',
                      {
                          'questions': page.object_list,
                          'paginator': paginator,
                          'page': page,
                      })


class AskView(View):
    def get(self, request, *args, **kwargs):

        form = AskForm()
        return render(request, 'templates/ask.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(post.get_absolute_url())
        else:
            return render(request, 'templates/ask.html', {'form': form})