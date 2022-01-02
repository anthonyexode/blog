from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=250)
  created = models.DateTimeField()
  edited = models.DateTimeField()
  content = HTMLField()
  status = models.BooleanField(default=False)