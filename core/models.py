# core/models.py
from django.db import models


class AbstractTimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating fields ``created`` and ``modified``
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
