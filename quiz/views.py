from django.shortcuts import render, redirect
from .models import Quiz, Question, Choice, Player, PlayerScore

def home(request):
    return render(request, 'quiz/home.html')

def start_quiz(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        player, created = Player.objects.get_or_create(name=player_name)
        return redirect('quiz_page', player_id=player.id)
    return render(request, 'quiz/start_quiz.html')

def quiz_page(request, player_id):
    player = Player.objects.get(id=player_id)
    quiz = Quiz.objects.first()
    questions = Question.objects.filter(quiz=quiz)[:5]
    return render(request, 'quiz/quiz_page.html', {'questions': questions, 'player': player})

def submit_quiz(request, player_id):
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
