from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import UploadPostForm
from django.shortcuts import redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from friend.models import Friend
from django.contrib.auth import authenticate



def user_Page(request, username):
    user_page = User.objects.get(username=username)
    posts = Post.objects.filter(user=user_page)
    if request.user.is_authenticated:
        friend_object = Friend.objects.get(user=request.user)
        friends = friend_object.friends.all()
        current_user = request.user
    else:
        friends = dict()
    return render(request, 'people/user_page.html', dict(user_page=user_page, posts=posts, friends=friends, current_user=current_user))



class UploadView(TemplateView):
    template_name = 'post/post_page.html'

    def get(self, request):
        form = UploadPostForm()
        args = dict(form=form)
        return render(request, self.template_name, args)


    def post(self, request):
        form = UploadPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            user = request.user
            username = user.username
            url = "/people/" + username +"/"
            return redirect(url)
        args = dict()
        return render(request, self.template_name, args)


