from django import forms
from django.db import models
from django.forms import ModelForm

from article.models import Article


# Create your models here.
class Comment(models.Model):
  author = models.EmailField(max_length=254)
  created = models.DateTimeField(auto_now_add=True)
  content = models.TextField()
  status = models.BooleanField(default=False)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['author', 'content']