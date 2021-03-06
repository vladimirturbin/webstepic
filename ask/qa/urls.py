from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('question/<int:question_number>/',
         views.QuestionView.as_view(), name='question'),
    path('popular/', views.PopularView.as_view(), name='popular'),
    path('ask/', views.AskView.as_view(), name='ask'),
]
