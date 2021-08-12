from django.shortcuts import render, redirect
from posts.models import Category , Posts, Likes
from posts.forms import PostsForm, PostFormEdit, LikeForm
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomeView(LoginRequiredMixin, ListView):
    template_name = "posts/home.html"
    model = Posts
    context_object_name = "posts"


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

def detail(request, post_id, context = {}):
    post = Posts.objects.get(id = post_id)
    have_like = Likes.objects.filter(post_id = post_id, user_id = request.user.id).exists()

    can_edit = False
    if post.user.id == request.user.id:
        can_edit = True
        
    return render(request, "posts/detail.html",  
            {
                "post" : post, 
                "can_edit" : can_edit, 
                "have_like" : have_like,
                **context
            },
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


    
def like(request, post_id):
    form = LikeForm({"post_id" : post_id})
    if form.is_valid():
        have_like =  Likes.objects.filter(post_id = post_id, user_id = request.user.id).exists()
        if not have_like:
            form.save(request.user.id)

    return detail(request, post_id, {"form" : form})
    



        

