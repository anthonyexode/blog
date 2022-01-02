from django.contrib.auth.management import commands
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Article
from comments.models import CommentForm

class IndexView(ListView):
    template_name = 'article/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        """Return the last five published articles."""
        return Article.objects.filter(status = True).order_by('-created')[:5]

class ArticleDetailView(FormMixin, DetailView):
    model = Article
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article:detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['comment_list'] = self.object.comment_set.filter(status = True)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit = False)
        comment.article = self.object
        comment.status = True
        comment.save()
        return super(ArticleDetailView, self).form_valid(form)