from .models import Profile, QuizAttempt , User
from .serializers import ProfileSerializer, QuizAttemptSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = QuizAttempt.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = QuizAttemptSerializer

class ProfileDeleteView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'

class QuizAttemptDeleteView(generics.DestroyAPIView):
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer
    lookup_field = 'id'

class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'

class QuizAttemptUpdateView(generics.UpdateAPIView):
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer
    lookup_field = 'id'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Definimos el queryset para los usuarios
    serializer_class = UserSerializer  # Usamos el serializador que creamos anteriormente
    permission_classes = [AllowAny]  # Permite que cualquier usuario acceda a esta vista

    def perform_create(self, serializer):
        # Este método crea el usuario usando el serializer
        serializer.save()