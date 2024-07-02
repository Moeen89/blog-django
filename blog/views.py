from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Post,Writer
from . import forms
from django.views import generic


class IndexView(generic.ListView):
    context_object_name = "latest_posts"
    template_name = "blog/index.html"
    paginate_by = 5

    def get_queryset(self):
        search_string = self.request.GET.get('text')
        sort = self.request.GET.get('sort')
        posts = [] 
        if search_string:
            posts = Post.objects.filter(title__contains= search_string)
        else:
            posts = Post.objects.all()
        if sort == "oldest":
            posts = posts.order_by('pub_date',)
        else:
            posts = posts.order_by('-pub_date',)
        return posts



        
""" def index(request):
    latest_posts = Post.objects.order_by('-pub_date',)[0:5]
    context = {
        "latest_posts": latest_posts,
    }
    return render(request, "blog/index.html", context) 
"""
class DetailsView(generic.DetailView):
    model = Post
    template_name = "blog/details.html" 

""" def details(request,id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404("no post exist with this ID!")
    return render(request, "blog/details.html", {"post": post}) """

class NewPostView(generic.edit.CreateView):
    template_name = "blog/post.html"
    model = Post
    success_url = reverse_lazy('blog:index')
    fields = ["title","text","image"]
    def form_valid(self, form):
        form.instance.writer =  get_object_or_404(Writer, pk=0)
        form.instance.pub_date = timezone.now()
        return super(NewPostView, self).form_valid(form)
    
class EditPostView(generic.edit.UpdateView):
    template_name = "blog/details.html"
    model = Post
    fields = ["title","text"]
    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        return super(EditPostView, self).form_valid(form)
    def get_success_url(self):
        success_url = reverse_lazy('blog:details',kwargs= {'pk' : self.kwargs.get('pk')})
        return success_url
    
class DeletePostView(generic.edit.DeleteView):
    template_name = "blog/details.html"
    model = Post
    success_url = reverse_lazy('blog:index')
    



        
    

"""     
class NewPostView(generic.edit.FormView):
    template_name = "blog/post.html"
    form_class = forms.NewPost
    success_url = "/blog"
    def form_valid(self, form):
        writer = get_object_or_404(Writer, pk=0)
        p = Post(title = form.cleaned_data.get('title')
                    , text= form.cleaned_data.get('text'),pub_date=timezone.now(),user_id = writer  )
        p.save()
        return super().form_valid(form)
  """   
""" 
def new_post(request):
    form = form.PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            try:
                writer = Writer.objects.get(pk=0)
            except Post.DoesNotExist:
                raise Http404("no user exist with this ID!")
            p = Post(title = form.cleaned_data.get('title')
                     , text= form.cleaned_data.get('text'),pub_date=timezone.now(),user_id = writer  )
            p.save()
            return HttpResponseRedirect("/blog")
        
    return render(request, "blog/post.html", {"form": form})
 """

