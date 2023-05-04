from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# router.register('subjects', views.SubjectViewSet, basename='subjects')
# router.register('questions', views.QuestionViewSet, basename='questions')
# router.register('answers', views.AnswerViewSet, basename='answers')

router.register('questions', views.QuestionViewSet, basename='questions')

urlpatterns = [
    
]

urlpatterns += router.urls