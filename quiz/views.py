from django.shortcuts import render, redirect
from .models import Quiz, Question, Choice, Player, PlayerScore
from rest_framework import generics
from .serializers import QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
import uuid
from django.http import JsonResponse

def home(request):
    return render(request, 'quiz/home.html')


players = {}


def start_quiz(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        request.session['player_name'] = player_name
        return redirect('quiz_page')
    return render(request, 'quiz/start_quiz.html')


def quiz_page(request):
    # Fetch questions from the Trivia API
    response = requests.get('https://the-trivia-api.com/v2/questions')
    questions = response.json() if response.status_code == 200 else []

    return render(request, 'quiz/quiz_page.html', {'questions': questions})


def submit_quiz(request):
    player = Player.objects.get(id=player_id)
    if request.method == 'POST':
        score = 0
        for question in Question.objects.all():
            selected = request.POST.get(str(question.id))
            if selected:
                choice = Choice.objects.get(id=int(selected))
                if choice.is_correct:
                    score += 1
        PlayerScore.objects.create(player=player, quiz=Quiz.objects.first(), score=score)
        return redirect('result', player_id=player.id)
    return redirect('home')


def result(request, player_id):
    player = Player.objects.get(id=player_id)
    score = PlayerScore.objects.filter(player=player).last().score
    return render(request, 'quiz/result.html', {'score': score, 'player': player})


def result_page(request):
    if request.method == 'POST':
        data = request.POST
        total_questions = len(data) - 1  # excluding csrf_token
        correct_answers = 0

        for key, answer in data.items():
            if key != 'csrfmiddlewaretoken':
                choice = Choice.objects.get(id=answer)
                if choice.is_correct:
                    correct_answers += 1

        score = correct_answers / total_questions * 100
        return render(request, 'quiz/result.html', {
            'score': score,
            'correct_answers': correct_answers,
            'total_questions': total_questions
        })
    else:
        return render(request, 'quiz/home.html')

def fetch_questions(request):
    try:
        response = requests.get("https://the-trivia-api.com/v2/questions")
        questions = response.json()
        return JsonResponse(questions[:5], safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
