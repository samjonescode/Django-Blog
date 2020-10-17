from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 

from .models import Post 


class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'
    def test_func(self):
        post = self.get_object() 
        if self.request.user == post.author:
            return True 
        else: 
            return False 

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: 
            return True 
        else: 
            return False 

### Function views ### 
# Create your views here.
def home(request): 
    # return HttpResponse('<h1> Welcome to page </h1>')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html')
    # return HttpResponse('<h1> This is the about page for the blog. ')