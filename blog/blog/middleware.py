from django.shortcuts import redirect
from django.urls import reverse
from posts.models import Posts

class AccesUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.post_id = 0

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if request.path in [reverse("edit",kwargs={'post_id': self.post_id})]:
            can_edit = Posts.objects.filter(id = self.post_id, user_id = request.user.id).exists()
            if not can_edit:
                redirect("home")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'post_id' in view_kwargs:
            self.post_id = view_kwargs['post_id']

