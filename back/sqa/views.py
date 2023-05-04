from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from rest_framework.generics import ListAPIView

from .models import *
from .serializers import *

# class SubjectViewSet(ModelViewSet):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer

# class QuestionViewSet(ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class AnswerViewSet(ModelViewSet):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer