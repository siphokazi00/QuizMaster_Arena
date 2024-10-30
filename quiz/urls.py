from django.urls import path
from . import views

urlpatterns = [
    path('start_quiz/', views.start_quiz, name='start_quiz'),
    path('quiz/', views.quiz_page, name='quiz_page'),
    path('api/fetch-questions/', views.fetch_questions, name='fetch-questions'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
    path('result/', views.result, name='result'),
]
