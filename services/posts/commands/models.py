from django.db import models
from django_extensions.db.models import TimeStampedModel


class Command(TimeStampedModel):
    name = models.CharField(max_length=64)
    command = models.CharField(max_length=512)
