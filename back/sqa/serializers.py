from rest_framework import serializers
from .models import *

# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields = ['id', 'name', 'is_true']

# class QuestionSerializer(serializers.ModelSerializer):
#     answers = AnswerSerializer(many=True, read_only=True)
#     class Meta:
#         model = Question
#         fields = ['id', 'name', 'answers']

# class SubjectSerializer(serializers.ModelSerializer):
#     questions = QuestionSerializer(many=True, read_only=True)
#     class Meta:
#         model = Subject
#         fields = ['id', 'name', 'questions']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'