from django.urls import path, include
from .views import ProfileDeleteView, QuizAttemptDeleteView, ProfileUpdateView, QuizAttemptUpdateView

urlpatterns = [
    path('api/profile/<int:id>/', ProfileDeleteView.as_view(), name='profile-delete'),
    path('api/quizattempt/<int:id>/', QuizAttemptDeleteView.as_view(), name='quizattempt-delete'),
    path('api/profile/update/<int:id>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('api/quizattempt/update/<int:id>/', QuizAttemptUpdateView.as_view(), name='quizattempt-update'),
]