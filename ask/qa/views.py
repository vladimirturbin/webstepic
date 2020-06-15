from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator

from .models import QuestionManager, Question

class IndexView(View):
    def get(self, request, *args, **kwargs):
        try:
            page = int(request.GET.get('page', 1))
        except TypeError:
            page = 1
        try:
            limit = int(request.GET.get('limit', 10))
        except TypeError:
            limit = 1

        # paginator = Paginator(QuestionManager.new(Question.objects), limit)
        paginator = Paginator(Question.objects.all(), limit)
        paginator.baseurl = '/?page='
        page = paginator.page(page)
        print()
        return render(request, 'templates/main.html',
                      {
                          'questions': page.object_list,
                          'paginator': paginator,
                          'page': page,
                      })


        # return HttpResponse(page)
