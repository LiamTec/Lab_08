from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import QuestionStat, QuizActivity
from .serializers import QuestionStatSerializer, QuizActivitySerializer

class QuestionStatViewSet(viewsets.ModelViewSet):
    """ViewSet para manejar las estadísticas de las preguntas"""
    queryset = QuestionStat.objects.all()  # Definimos el queryset para obtener las estadísticas
    permission_classes = [IsAuthenticated]  # Requiere que el usuario esté autenticado
    serializer_class = QuestionStatSerializer  # Usamos el serializer correspondiente

class QuizActivityViewSet(viewsets.ModelViewSet):
    """ViewSet para manejar la actividad de los cuestionarios"""
    queryset = QuizActivity.objects.all()  # Definimos el queryset para obtener las actividades
    permission_classes = [IsAuthenticated]  # Requiere que el usuario esté autenticado
    serializer_class = QuizActivitySerializer  # Usamos el serializer correspondiente
