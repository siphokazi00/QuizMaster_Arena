from django.contrib import admin
from .models import Quiz, Question, Choice, Player, PlayerScore


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Player)
admin.site.register(PlayerScore)
