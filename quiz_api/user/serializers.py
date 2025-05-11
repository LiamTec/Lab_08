from rest_framework import serializers
from .models import Profile, QuizAttempt , User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar', 'created_at']
        read_only_fields = ['id', 'created_at']

class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'score', 'max_score', 'completed_at']
        read_only_fields = ['id', 'completed_at']

class UserSerializer(serializers.ModelSerializer):
    # Agregamos los campos necesarios para crear un usuario
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Creamos un nuevo usuario con la contraseña encriptada
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
