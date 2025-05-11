from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet
from categories.views import CategoryViewSet, TagViewSet

# Definición de los routers para las vistas basadas en ViewSets
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'tag', TagViewSet)

# Definir las rutas de la API
urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del router bajo el prefijo 'api/'  # Ruta para refrescar el token
]
