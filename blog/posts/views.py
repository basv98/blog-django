from django.shortcuts import render
from posts.models import Category , Posts
from posts.forms import PostsForm, PostFormEdit
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    posts = Posts.objects.all()
    return render(request, "posts/home.html", {"posts" : posts})


class PostFormView(LoginRequiredMixin,FormView):
    template_name = 'posts/create.html'
    form_class = PostsForm
    success_url = '/home'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        data['categories'] = categories
        return data

    def form_valid(self, form):
        # import pdb; pdb.set_trace()
        form.save(self.request.user.id)
        return super().form_valid(form)

def detail(request, post_id):
    post = Posts.objects.get(id = post_id)

    can_edit = False
    if post.user.id == request.user.id:
        can_edit = True
        
    return render(request, "posts/detail.html",  
            {"post" : post, "can_edit" : can_edit},
           )

class EditFormViw(LoginRequiredMixin, FormView):
    template_name = 'posts/edit.html'
    form_class = PostFormEdit

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        data['categories'] = categories
        data['post'] = Posts.objects.get(id = self.kwargs['post_id'])
        return data

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail', kwargs={'post_id': self.kwargs['post_id']})



        

