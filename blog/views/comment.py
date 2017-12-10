from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from ..models.comment import Comment
from ..models.post import Post


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['body']
    template_name = 'blog/create_comment.html'
    login_url = '/login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post', kwargs={'pk': self.kwargs['pk']})