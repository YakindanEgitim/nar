# comments/models.py
from django.db import models

from core.models import AbstractTimeStampedModel
from profiles.models import Profile


class Comment(AbstractTimeStampedModel):
    text = models.TextField()
    commenter = models.ForeignKey(Profile)


class Vote(AbstractTimeStampedModel):
    vote_type = models.BooleanField()
    voter = models.ForeignKey(Profile)
    comment = models.ForeignKey(Comment)
