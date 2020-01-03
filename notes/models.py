from django.db import models
from uuid import uuid4

# Create your models here.
# this uses all the built in model classes from django.
class Note(models.Model):
    # id = models.UUIDField(...)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

class Folders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    list_notes = models.TextField(blank=True)