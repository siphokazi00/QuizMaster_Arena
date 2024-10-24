from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('quiz/<int:player_id>/', views.quiz_page, name='quiz_page'),
    path('submit/<int:player_id>/', views.submit_quiz, name='submit_quiz'),
    path('result/<int:player_id>/', views.result, name='result'),
]
