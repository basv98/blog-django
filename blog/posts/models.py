from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 100)


# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    content = models.CharField(max_length= 100)
    cetegory = models.ForeignKey(Category, on_delete = models.DO_NOTHING)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
