from django.contrib import admin
from django.urls import path
from auth import views
from posts import views as views_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginView.as_view() , name = "login"),
    path('logout/', views.LogoutView.as_view() , name = "logout"),
    path('home/', views_posts.home , name = "home"),
    path('posts/create/', views_posts.PostFormView.as_view() , name = "create"),
    path('posts/detail/<int:post_id>', views_posts.detail , name = "detail"),
    path('posts/edit/<int:post_id>', views_posts.EditFormViw.as_view() , name = "edit"),
]
