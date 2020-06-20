from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('question/<int:question_id>/',
         views.IndexView.as_view(), name='question')
]
