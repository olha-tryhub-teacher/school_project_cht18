from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


# Create your models here.

class Vote(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_by = models.TextField()
    end_date = models.DateTimeField()

class VoteOption(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    text = models.TextField()

class UserVote(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.ForeignKey(VoteOption, on_delete=models.CASCADE)
    voted_at = models.DateTimeField()
