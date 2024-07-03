from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Post, Writer
from . import forms
from django.views import generic


class IndexView(generic.ListView):
    context_object_name = "latest_posts"
    template_name = "blog/index.html"
    paginate_by = 5

    def get_queryset(self):
        search_string = self.request.GET.get('title')
        sort = self.request.GET.get('sort')
        posts = []
        if search_string:
            posts = Post.objects.filter(title__icontains=search_string)
        else:
            posts = Post.objects.all()
        if sort == "oldest":
            posts = posts.order_by('pub_date', )
        else:
            posts = posts.order_by('-pub_date', )
        return posts


class DetailsView(generic.DetailView):
    model = Post
    template_name = "blog/details.html"


class NewPostView(generic.edit.CreateView):
    template_name = "blog/post.html"
    model = Post
    success_url = reverse_lazy('blog:index')
    fields = ["title", "text", "image"]

    def form_valid(self, form):
        form.instance.writer = get_object_or_404(Writer, pk=0)
        form.instance.pub_date = timezone.now()
        return super(NewPostView, self).form_valid(form)


class EditPostView(generic.edit.UpdateView):
    template_name = "blog/edit_post.html"
    model = Post
    fields = ["title", "text"]

    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        return super(EditPostView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:details', kwargs={'pk': self.kwargs.get('pk')})


class DeletePostView(generic.edit.DeleteView):
    template_name = "blog/delete_confirmation.html"
    model = Post
    success_url = reverse_lazy('blog:index')
