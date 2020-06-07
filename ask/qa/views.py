from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        try:
            page = int(request.GET.get('page', 1))
        except TypeError:
            page = 1

        return HttpResponse(page)
