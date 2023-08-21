from django.db import models

class Member(models.Model):
  football_quiz = models.CharField(max_length=255)
  general_quiz = models.CharField(max_length=255)