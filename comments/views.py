from django.shortcuts import get_object_or_404
from django.views import generic

# Create your views here.
from .models import Comment
from article.models import Article

class CommentsByArticleView(generic.ListView):
    context_object_name = 'comments'
    template_name = 'comments/list.html'

    def get_queryset(self):
        self.article = get_object_or_404(Article, id=self.kwargs['pk'])
        return Comment.objects.filter(article = self.article, status = True).order_by('-created')