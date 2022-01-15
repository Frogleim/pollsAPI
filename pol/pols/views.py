from rest_framework import viewsets
from rest_framework.response import Response

from . import serializers
from .models import User, Choice,Polls
from .serializers import UserSerializer,ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Polls.objects.all()
    serializer_class = serializers.QuestionSerializer


    def destroy(self, request, *args, **kwargs):
        polls = self.get_object()
        polls.delete()

        return Response({'message': 'item has been deleted'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super(UserViewSet, self).get_object()

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    if Choice.ANSWER_TYPE == 'Text':
        Choice.ANSWER_CHOICES = False

