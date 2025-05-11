from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionStatViewSet, QuizActivityViewSet

# Inicializamos el router
router = DefaultRouter()

# Registramos los viewsets en el router
router.register(r'question-stats', QuestionStatViewSet, basename='question-stat')
router.register(r'quiz-activities', QuizActivityViewSet, basename='quiz-activity')

# Definimos las rutas del API
urlpatterns = [
    path('api/', include(router.urls)),  # Incluir las rutas de 'quiz_analysis' bajo 'api/'
]
