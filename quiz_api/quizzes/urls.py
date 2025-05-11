from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet
from categories.views import CategoryViewSet, TagViewSet
from user.views import QuizAttemptViewSet, ProfileViewSet, UserViewSet
from quiz_analysis.views import QuestionStatViewSet,QuizActivityViewSet

# Definición de los routers para las vistas basadas en ViewSets
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'tag', TagViewSet)
router.register(r'quizattempt', QuizAttemptViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'question-stats', QuestionStatViewSet, basename='question-stat')
router.register(r'quiz-activities', QuizActivityViewSet, basename='quiz-activity')


# Definir las rutas de la API
urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del router bajo el prefijo 'api/'  # Ruta para refrescar el token
]
