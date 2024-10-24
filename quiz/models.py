from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time_limit = models.IntegerField(default=20)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)



class PlayerScore(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField()
    taken_at = models.DateTimeField(auto_now_add=True)
