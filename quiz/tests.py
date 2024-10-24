from django.test import TestCase
from .models import Quiz, Question, Choice

class QuizTestCase(TestCase):
    def setUp(self):
        quiz = Quiz.objects.create(title="Test Quiz")
        question = Question.objects.create(quiz=quiz, text="Test Question?")
        Choice.objects.create(question=question, choice_text="Test Choice", is_correct=True)

    def test_quiz_creation(self):
        quiz = Quiz.objects.get(title="Test Quiz")
        self.assertEqual(quiz.title, "Test Quiz")
