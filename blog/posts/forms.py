from django import forms
from posts.models import Category, Posts, Likes

class PostsForm(forms.Form):
    title = forms.CharField(required = True)
    cetegory_id = forms.IntegerField(required = True)
    content = forms.CharField(required = True)

    def clean_cetegory_id(self):
        cetegory_id = self.cleaned_data['cetegory_id']
        exist_cetegory_id = Category.objects.filter(id = cetegory_id).exists()
        if not exist_cetegory_id:
            raise forms.ValidationError("Categoria inválida")
        return cetegory_id

    def save(self,user_id):
        data = self.cleaned_data
        data['user_id'] = user_id
        Posts.objects.create(**data)


class PostFormEdit(PostsForm):
    post_id = forms.IntegerField(required = True)


    def clean_post_id(self):
        post_id = self.cleaned_data['post_id']
        exists_post = Posts.objects.filter(id = post_id).exists()
        if not exists_post:
            raise forms.ValidationError(f"El post con id {post_id} no existe")
        return post_id
        
    def save(self):
        data = self.cleaned_data
        post_id = data['post_id']
        data.pop("post_id")
        Posts.objects.filter(id = post_id).update(**data)

class LikeForm(forms.Form):
    post_id = forms.IntegerField(required = True)

    def clean_post_id(self):
        post_id = self.cleaned_data['post_id']
        exists_post = Posts.objects.filter(id = post_id).exists()
        if not exists_post:
            raise forms.ValidationError(f"El post con id {post_id} no existe")
        return post_id


    def save(self, user_id):
        data = self.cleaned_data
        data["user_id"] = user_id
        Likes.objects.create(**data)


def isset_post(post_id):
    exists_post = Posts.objects.filter(id = post_id).exists()
    if not exists_post:
        raise forms.ValidationError(f"El post con id {post_id} no existe")

