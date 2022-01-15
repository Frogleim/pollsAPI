from rest_framework import serializers
from .models import Polls,User,Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Polls


class UserSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'courses']


class ChoiceSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ('__all__')
        model = Choice

