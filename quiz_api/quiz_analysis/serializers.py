from rest_framework import serializers
from quizzes.models import Quiz, Question
from .models import QuestionStat, QuizActivity

class QuestionStatSerializer(serializers.ModelSerializer):
    success_rate = serializers.ReadOnlyField()

    class Meta:
        model = QuestionStat
        fields = ['question', 'attempts', 'correct_attempts', 'success_rate']

class QuizActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizActivity
        fields = ['quiz', 'date', 'views', 'starts', 'completions']
