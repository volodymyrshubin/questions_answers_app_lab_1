from django.db import models

# class Subject(models.Model):
#     name = models.CharField(max_length=250)

# class Question(models.Model):
#     subject = models.ForeignKey(Subject, related_name='questions', on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)

# class Answer(models.Model):
#     question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)
#     is_true = models.BooleanField(max_length=250)

class Question(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)